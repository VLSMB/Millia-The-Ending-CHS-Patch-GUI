#include "mainwindow.h"
#include "ui_mainwindow.h"
#pragma execution_character_set("utf-8")

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QObject::connect(ui->InstallButton,SIGNAL(clicked(bool)),this,SLOT(Install_Function()));
    QObject::connect(ui->UnInstallButton,SIGNAL(clicked(bool)),this,SLOT(UnInstall_Function()));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void decompressFile(QString filePath)
{
    // https://zhuanlan.zhihu.com/p/426934200
    // QZipReader的解压函数似乎有问题，不能解压writer写进去的文件夹…不过这个方法解压不了文件……
    if (!QFile(filePath).exists()) {
    }
    QZipReader cZip(filePath);
    foreach(QZipReader::FileInfo item, cZip.fileInfoList())
    {
        if (item.isDir)
        {
            QDir d(item.filePath);
            if (!d.exists())
                d.mkpath(item.filePath);
        }

        if (item.isFile)
        {
            QString filepath = item.filePath;
            const int index = filepath.lastIndexOf("/");

            QDir dir(filepath.left(index));
            if (!dir.exists()) {
                QDir("./").mkpath(filepath.left(index));
            }
            QFile file(item.filePath);

            file.open(QFile::WriteOnly);
            file.write(cZip.fileData(item.filePath));
            file.close();
        }
    }
    cZip.close();
}


void deleteDir(const QString &path)
{
    QDir dir(path);
    dir.setFilter(QDir::AllEntries | QDir::NoDotAndDotDot);
    QFileInfoList fileList = dir.entryInfoList();
    foreach (QFileInfo file, fileList)
    {
        if (file.isFile())
        {
            file.dir().remove(file.fileName());
        }else
        {
            deleteDir(file.absoluteFilePath());
        }
    }
    dir.rmpath(dir.absolutePath());
}


void getAllFileName(QString path, QVector<QString> &path_vec)
{
    // https://blog.csdn.net/weixin_41093846/article/details/104711490?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1-104711490-blog-108450662.pc_relevant_multi_platform_whitelistv3&spm=1001.2101.3001.4242.2&utm_relevant_index=4
    QDir *dir=new QDir(path);
    QStringList filter;
    QList<QFileInfo> *fileInfo=new QList<QFileInfo>(dir->entryInfoList(filter));
    for(int i = 0;i<fileInfo->count(); ++i)
    {
        const QFileInfo info_tmp = fileInfo->at(i);
        QString path_tmp = info_tmp.filePath();
        if( info_tmp.fileName()==".." || info_tmp.fileName()=="." )
        {
        }else if(info_tmp.isFile() ){
            path_vec.push_back(path_tmp);
        }else if(info_tmp.isDir()){
            getAllFileName(path_tmp,path_vec);
        }
    }
}


void AddZip(QString filename,QZipWriter* writer)
{
    QFile file(filename);
    QFileInfo fileinfo(filename);
    file.open(QIODevice::ReadOnly);
    writer->addFile(fileinfo.filePath(),file.readAll());
    file.close();
}
void AddZip(QFileInfo fileinfo,QZipWriter* writer)
{
    QFile file(fileinfo.filePath());
    file.open(QIODevice::ReadOnly);
    writer->addFile(fileinfo.filePath(),file.readAll());
    file.close();
}


void MainWindow::Install_Function()
{
    if(QFile("MTE_CHS_config.ini").exists())
    {
        QMessageBox::critical(this,TITLE,"已经安装过汉化补丁，不能重复安装！");
        return;
    }
    QMessageBox::StandardButton choice = QMessageBox::question(this,TITLE,"确定要安装本汉化补丁吗？\n（安装过程中程序可能会未响应，耐心等待即可）");
    if (choice == QMessageBox::No)
        return;
    QFile mtegame("Millia - The ending -.exe");
    QFile mterpa("game\\archive.rpa");
    QDir mtelib("lib");
    QDir mterenpy("renpy");
    bool readme = QFile("README.html").exists();
    bool status = mtegame.exists() && mterpa.exists() && mtelib.exists() && mterenpy.exists();
    if (status)
    {
        // 先关闭已经打开的游戏
        HWND hPro = FindWindowA("SDL_app","Millia - The ending -");
        if (hPro != NULL)
        {
            int pid;
            GetWindowThreadProcessId(hPro,(LPDWORD)&pid);
            QProcess* p = new QProcess;
            p->start("taskkill",QStringList()<<"/F"<<"/PID"<<QString::number(pid));
            p->waitForFinished(-1);
        }
        // 释放资源文件
        QStringList PatchAllFiles;
        PatchAllFiles << "uvn_van.TTF" << "times.ttf" << "script.rpyc" << "script.rpy" << "screens.rpy" << "screens.rpyc" << "options.rpyc" << "options.rpy" << "arial.ttf";
        if(!QFile::copy(":/zip/PatchFile.zip","PatchFile.zip"))
        {
            QMessageBox::critical(this,TITLE,"补丁加载失败！请删除或重命名本目录下的\"PatchFile.zip\"，检查磁盘空间是否可用。");
            return;
        }
        // 备份原版文件
        QZipWriter* writer = new QZipWriter("MTE_English.pak");
        writer->setCompressionPolicy(QZipWriter::AutoCompress);
        QDir::current().mkdir("exe");
        QFile::copy("Millia - The ending -.exe","exe\\Millia - The ending -.exe");
        AddZip("exe\\Millia - The ending -.exe",writer);
        if (readme)
        {
            QFile::copy("README.html","exe\\README.html");
            AddZip("exe\\README.html",writer);
        }
        QVector<QString> libList,renpyList;
        getAllFileName("lib",libList);
        foreach (QString file,libList)
            AddZip(file,writer);
        getAllFileName("renpy",renpyList);
        foreach (QString file,renpyList)
            AddZip(file,writer);

        // 解压资源文件
        mtegame.remove();
        if(readme)
            QFile("README.html").remove();
        deleteDir("renpy");
        deleteDir("lib");
        QZipReader* reader = new QZipReader("PatchFile.zip");
        reader->extractAll(QDir::currentPath());
        QProcess* p1 = new QProcess;
        p1->start("rpatool.exe",QStringList()<<"-x"<<"game\\archive.rpa"<<PatchAllFiles<<QStringList()<<"-o"<<"game");
        p1->waitForFinished(-1);
        foreach (QString file,PatchAllFiles)
            AddZip("game\\"+file,writer);
        QFile::copy("rpatool.exe","exe\\rpatool.exe");
        AddZip("exe\\rpatool.exe",writer);
        deleteDir("exe");
        writer->close();
        reader->close();
        QProcess* p2 = new QProcess;
        p2->start("rpatool.exe",QStringList()<<"-d"<<"game\\archive.rpa"<<PatchAllFiles);
        p2->waitForFinished(-1);
        QProcess* p3 = new QProcess;
        p3->start("rpatool.exe",QStringList()<<"-a"<<"game\\archive.rpa"<<PatchAllFiles<<QStringList()<<"information_chs.jpg");
        p3->waitForFinished(-1);
        // 清理文件
        foreach (QString file,PatchAllFiles)
        {
            DeleteFileA((LPCSTR)file.toLocal8Bit());
            DeleteFileA((LPCSTR)(("game\\"+file).toLocal8Bit()));
        }
        DeleteFileA("rpatool.exe");
        DeleteFileA("information_chs.jpg");
        QFile::copy(":/zip/Document.zip","游戏相关文档.zip");
        QFile::copy(":/zip/PatchCode.zip","所有版本补丁的源码.zip");
        SetFileAttributesA("PatchFile.zip",FILE_ATTRIBUTE_NORMAL);
        DeleteFileA("PatchFile.zip");
        QFile conf("MTE_CHS_config.ini");
        conf.open(QFile::WriteOnly|QFile::Text);
        QTextStream out(&conf);
        out << "[MTE_CHS_config]\n\n[Version = V3.0]\n\n[bakfile = MTE_English.pak]";
        conf.flush();
        conf.close();
        QMessageBox::information(this,TITLE,"汉化补丁植入完成！汉化组祝您游戏愉快！");
    }
    else
        QMessageBox::critical(this,TITLE,"未找到完整的游戏程序！请将本补丁程序放在游戏目录下运行，或者检查游戏完整性！\n（提示：本游戏默认存放在steam文件夹下的“\\steamapps\\common\\Millia -The ending-”里）");
}

void MainWindow::UnInstall_Function()
{
    QFile EnglishPatch("MTE_English.pak");
    if (!EnglishPatch.exists())
    {
        QMessageBox::critical(this,TITLE,"找不到备份文件，或者备份文件已经失效！");
        return;
    }
    QMessageBox::StandardButton choice = QMessageBox::question(this,TITLE,"确定要卸载本汉化补丁吗？\n（卸载过程中程序可能会未响应，耐心等待即可）");
    if (choice == QMessageBox::No)
        return;

    deleteDir("renpy");
    deleteDir("lib");
    HWND hPro = FindWindowA("SDL_app","Millia - The ending -");
    if (hPro != NULL)
    {
        int pid;
        GetWindowThreadProcessId(hPro,(LPDWORD)&pid);
        QProcess* p = new QProcess;
        p->start("taskkill",QStringList()<<"/F"<<"/PID"<<QString::number(pid));
        p->waitForFinished(-1);
    }
    DeleteFileA("Millia - The ending -.exe");
    DeleteFileA("Millia - The ending --32.exe");
    DeleteFileA("README.html");
    DeleteFileA("MTE_CHS_config.ini");

    //QZipReader* reader2 = new QZipReader("MTE_English.pak");
    //reader2->extractAll(QDir::currentPath());
    //reader2->close();
    decompressFile("MTE_English.pak");
    QFile::copy("exe\\rpatool.exe","rpatool.exe");
    QFile::copy("exe\\README.html","README.html");
    QFile::copy("exe\\Millia - The ending -.exe","Millia - The ending -.exe");
    deleteDir("exe");
    QStringList PatchAllFiles;
    PatchAllFiles << "uvn_van.TTF" << "times.ttf" << "script.rpyc" << "script.rpy" << "screens.rpy" << "screens.rpyc" << "options.rpyc" << "options.rpy" << "arial.ttf";
    foreach (QString file,PatchAllFiles)
        MoveFileA((LPCSTR)(("game\\"+file).toLocal8Bit()),(LPCSTR)file.toLocal8Bit());
    QProcess* p2 = new QProcess;
    p2->start("rpatool.exe",QStringList()<<"-d"<<"game\\archive.rpa"<<PatchAllFiles<<QStringList()<<"information_chs.jpg");
    p2->waitForFinished(-1);
    QProcess* p3 = new QProcess;
    p3->start("rpatool.exe",QStringList()<<"-a"<<"game\\archive.rpa"<<PatchAllFiles);
    p3->waitForFinished(-1);
    foreach (QString file,PatchAllFiles)
        QFile(file).remove();
    DeleteFileA("rpatool.exe");
    DeleteFileA("MTE_English.pak");
    SetFileAttributesA("PatchFile.zip",FILE_ATTRIBUTE_NORMAL);
    DeleteFileA("PatchFile.zip");
    QMessageBox::information(this,TITLE,"汉化补丁卸载完成！");
}
