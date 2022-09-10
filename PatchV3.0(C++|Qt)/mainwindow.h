#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QMessageBox>
#include <QFile>
#include <QDir>
#include <QStringList>
#include <QProcess>
#include <windows.h>
#include <private/qzipreader_p.h>
#include <private/qzipwriter_p.h>
#include <QFileInfoList>
#include <QFileInfo>
#include <QString>
#include <QStringList>
#include <QVector>
#include <QTextStream>
#define TITLE "Millia -The ending- ºº»¯²¹¶¡³ÌÐò"

void AddZip(QString filename,QZipWriter* writer);
void AddZip(QFileInfo fileinfo,QZipWriter* writer);

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
public slots:
    void Install_Function();
    void UnInstall_Function();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
