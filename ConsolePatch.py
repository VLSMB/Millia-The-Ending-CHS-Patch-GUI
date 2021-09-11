# _*_ coding:utf-8 _*_
# 老版本控制台的一些源代码，其实可以进行许多优化，但由于时间关系，直接拿来用了
import time

Text = ""
def ConsoleInstall():
    """安装汉化补丁的过程"""
    import os, zipfile, shutil, wx, time
    temp = wx.App()
    CurrentPath = os.getcwd()
    VERSION = "V2.0"
    PatchAllFiles = ["uvn_van.TTF", "times.ttf", "script.rpyc", "script.rpy", "screens.rpy", "screens.rpyc",
                     "options.rpyc", "options.rpy", "arial.ttf"]
    os.system("C:\\Windows\\System32\\taskkill.exe /im \"Millia - The ending -.exe\" /f")
    # 操作：打包英文版文件
    print("即将开始备份原版文件...")
    global Text
    Text = "即将开始备份原版文件..." + "\n"
    patcheng = zipfile.ZipFile("MTE_PatchENG.cjxpak", "w", zipfile.ZIP_DEFLATED)
    patcheng.write("Millia - The ending -.exe", "Millia - The ending -.exe", zipfile.ZIP_DEFLATED)
    print("打包：" + CurrentPath + "\\Millia - The ending -.exe")
    Text += "打包：" + CurrentPath + "\\Millia - The ending -.exe" + "\n"
    patcheng.write("lib", "lib", zipfile.ZIP_DEFLATED)
    patcheng.write("renpy", "renpy", zipfile.ZIP_DEFLATED)
    if os.path.exists("README.html"):
        patcheng.write("README.html", "README.html", zipfile.ZIP_DEFLATED)
        print("打包：" + CurrentPath + "\\README.html")
        Text += "打包：" + CurrentPath + "\\README.html" + "\n"
    # 将原引擎的文件打包成对应的列表
    for filepathA, dirnamesA, filenamesA in os.walk(CurrentPath + "\\renpy"):
        for filenameA in filenamesA:
            dirnameA = os.path.join(filepathA, filenameA)
            dirnamezipA = dirnameA[len(CurrentPath) + 1:len(dirnameA)]
            patcheng.write(dirnameA, dirnamezipA, zipfile.ZIP_DEFLATED)
            print("打包：" + dirnameA)
            Text += "打包：" + dirnameA + "\n"
    for filepathB, dirnamesB, filenamesB in os.walk(CurrentPath + "\\lib"):
        for filenameB in filenamesB:
            dirnameB = os.path.join(filepathB, filenameB)
            dirnamezipB = dirnameB[len(CurrentPath) + 1:len(dirnameB)]
            patcheng.write(dirnameB, dirnamezipB, zipfile.ZIP_DEFLATED)
            print("打包：" + dirnameB)
            Text += "打包：" + dirnameB + "\n"
    # 删除原版文件
    shutil.rmtree(CurrentPath + "\\renpy")
    print("删除：" + CurrentPath + "\\renpy")
    Text += "删除：" + CurrentPath + "\\renpy" + "\n"
    shutil.rmtree(CurrentPath + "\\lib")
    print("删除：" + CurrentPath + "\\lib")
    Text += "删除：" + CurrentPath + "\\lib" + "\n"
    os.remove(CurrentPath + "\\Millia - The ending -.exe")
    print("删除：" + CurrentPath + "\\Millia - The ending -.exe")
    Text += "删除：" + CurrentPath + "\\Millia - The ending -.exe" + "\n"
    if os.path.exists("README.html"):
        os.remove(CurrentPath + "\\README.html")
        print("删除：" + CurrentPath + "\\README.html")
        Text += "删除：" + CurrentPath + "\\README.html" + "\n"
    print("原版文件备份成功！")
    Text += "原版文件备份成功！" + "\n"
    # 解压缩cjxpak(其实就是zip文件啦)
    patchchs1 = zipfile.ZipFile("MTE_PatchCHS" + VERSION + ".part1.cjxpak")
    patchchs1.extractall()
    for tempfn in patchchs1.namelist():
        print("解压缩：" + CurrentPath + "\\" + tempfn)
        Text += "解压缩：" + CurrentPath + "\\" + tempfn + "\n"
    patchchs2 = zipfile.ZipFile("MTE_PatchCHS" + VERSION + ".part2.cjxpak")
    patchchs2.extractall()
    for tempfn in patchchs2.namelist():
        print("解压缩：" + CurrentPath + "\\" + tempfn)
        Text += "解压缩：" + CurrentPath + "\\" + tempfn + "\n"
    patchchs3 = zipfile.ZipFile("MTE_PatchCHS" + VERSION + ".part3.cjxpak")
    patchchs3.extractall()
    for tempfn in patchchs3.namelist():
        print("解压缩：" + CurrentPath + "\\" + tempfn)
        Text += "解压缩：" + CurrentPath + "\\" + tempfn + "\n"
    shutil.move("windows-x86_64", "lib\\windows-x86_64")
    shutil.move("windows-i686", "lib\\windows-i686")
    print("解压缩完成！")
    Text += "解压缩完成！" + "\n"
    # 备份archive.rpa中部分文件
    print("正在备份archive.rpa中部分数据...")
    Text += "正在备份archive.rpa中部分数据..." + "\n"
    os.system(
        "rpatool.exe -x game\\archive.rpa arial.ttf options.rpy options.rpyc screens.rpy screens.rpyc script.rpy script.rpyc times.ttf uvn_van.TTF -o game")
    for PatchFile in PatchAllFiles:
        patcheng.write(CurrentPath + "\\game\\" + PatchFile, PatchFile, zipfile.ZIP_DEFLATED)
        print("打包：" + CurrentPath + "\\game\\" + PatchFile)
        Text += "打包：" + CurrentPath + "\\game\\" + PatchFile + "\n"
    patcheng.write(CurrentPath + "\\rpatool.exe", "rpatool.exe", zipfile.ZIP_DEFLATED)
    print("打包：" + CurrentPath + "\\rpatool.exe")
    Text += "打包：" + CurrentPath + "\\rpatool.exe" + "\n"
    # 打入汉化补丁
    print("正在打入汉化补丁...")
    Text += "正在打入汉化补丁..." + "\n"
    os.system(
        "rpatool.exe -x game\\archive.rpa arial.ttf options.rpy options.rpyc screens.rpy screens.rpyc script.rpy script.rpyc times.ttf uvn_van.TTF -o game")
    os.system(
        "rpatool.exe -d game\\archive.rpa arial.ttf options.rpy options.rpyc screens.rpy screens.rpyc script.rpy script.rpyc times.ttf uvn_van.TTF")
    os.system(
        "rpatool.exe -a game\\archive.rpa arial.ttf options.rpy options.rpyc screens.rpy screens.rpyc script.rpy script.rpyc times.ttf uvn_van.TTF information_chs.jpg")
    for tempfn in PatchAllFiles:
        print("成功：" + CurrentPath + "\\" + tempfn)
        Text += "成功：" + CurrentPath + "\\" + tempfn + "\n"
    print("成功：" + CurrentPath + "\\information_chs.jpg")
    Text += "成功：" + CurrentPath + "\\information_chs.jpg" + "\n"
    # 清理临时文件
    print("正在清理临时文件...")
    Text += "正在清理临时文件..." + "\n"
    for delfile in PatchAllFiles:
        os.remove(CurrentPath + "\\" + delfile)
        os.remove(CurrentPath + "\\game\\" + delfile)
    os.remove(CurrentPath + "\\information_chs.jpg")
    os.remove(CurrentPath + "\\rpatool.exe")
    patcheng.close()
    patchchs1.close()
    patchchs2.close()
    patchchs3.close()
    print("汉化补丁植入完成！汉化组祝您游戏愉快！")
    Text += "汉化补丁植入完成！汉化组祝您游戏愉快！" + "\n"
    print("\n32位操作系统请运行带“-32”的应用程序，64位操作系统直接运行本体程序。\n")
    Text += "\n32位操作系统请运行带“-32”的应用程序，64位操作系统直接运行本体程序。\n"
    import time
    time.sleep(2)
    Text = None

def ZipError():
    """判断汉化包是否损坏"""

    import zipfile
    VERSION = "V2.0"
    try:
        f = zipfile.ZipFile("MTE_PatchCHS"+VERSION+".part1.cjxpak")
        f = zipfile.ZipFile("MTE_PatchCHS"+VERSION+".part2.cjxpak")
        f = zipfile.ZipFile("MTE_PatchCHS"+VERSION+".part3.cjxpak")
    except:
        return False
    else:
        return True

def ConsoleUninstall():
    """卸载汉化补丁，需要安装过补丁并留住了备份文件"""

    import os, shutil, zipfile
    CurrentPath = os.getcwd()
    PatchAllFiles = ["uvn_van.TTF", "times.ttf", "script.rpyc", "script.rpy", "screens.rpy", "screens.rpyc",
                     "options.rpyc", "options.rpy", "arial.ttf"]
    global Text
    print("正在还原英文原版，请稍后...")
    Text = "正在还原英文原版，请稍后..."
    os.remove(CurrentPath + "\\Millia - The ending -.exe")
    print("删除：" + CurrentPath + "\\Millia - The ending -.exe")
    Text += "删除：" + CurrentPath + "\\Millia - The ending -.exe" + "\n"
    if os.path.exists(CurrentPath + "\\README.html"):
        os.remove(CurrentPath + "\\README.html")
        print("删除：" + CurrentPath + "\\README.html")
        Text += "删除：" + CurrentPath + "\\README.html" + "\n"
    shutil.rmtree(CurrentPath + "\\renpy")
    print("删除：" + CurrentPath + "\\renpy")
    Text += "删除：" + CurrentPath + "\\renpy" + "\n"
    shutil.rmtree(CurrentPath + "\\lib")
    print("删除：" + CurrentPath + "\\lib")
    Text += "删除：" + CurrentPath + "\\lib" + "\n"
    patcheng = zipfile.ZipFile("MTE_PatchENG.cjxpak")
    patcheng.extractall()
    for x in patcheng.namelist():
        print("解压缩：" + CurrentPath + "\\" + x)
        Text += "解压缩：" + CurrentPath + "\\" + x + "\n"
    print("\n解压缩完成！")
    Text += "\n解压缩完成！" + "\n"
    print("正在修改archive.rpa，请稍后...")
    Text += "正在修改archive.rpa，请稍后..." + "\n"
    os.system(
        "rpatool.exe -d game\\archive.rpa arial.ttf options.rpy options.rpyc screens.rpy screens.rpyc script.rpy script.rpyc times.ttf uvn_van.TTF information_chs.jpg")
    os.system(
        "rpatool.exe -a game\\archive.rpa arial.ttf options.rpy options.rpyc screens.rpy screens.rpyc script.rpy script.rpyc times.ttf uvn_van.TTF")
    for tempfn in PatchAllFiles:
        print("成功：" + CurrentPath + "\\" + tempfn)
        Text += "成功：" + CurrentPath + "\\" + tempfn + "\n"
    print("正在清理临时文件，请稍等...")
    Text += "正在清理临时文件，请稍等..." + "\n"
    # 清理所生成的所有临时文件
    for delfn in PatchAllFiles:
        os.remove(CurrentPath + "\\" + delfn)
        print("删除：" + CurrentPath + "\\" + delfn)
        Text += "删除：" + CurrentPath + "\\" + delfn + "\n"
    os.remove(CurrentPath + "\\rpatool.exe")
    print("删除：" + CurrentPath + "\\rpatool.exe")
    Text += "删除：" + CurrentPath + "\\rpatool.exe" + "\n"
    Text += "\n汉化补丁卸载完成！"
    import time
    time.sleep(2)
    Text = None

def UninstallZip():
    import zipfile
    try:
        f = zipfile.ZipFile("MTE_PatchENG.cjxpak")
    except:
        return False
    else:
        return  True

def GetDownloadLink():
    from bs4 import BeautifulSoup
    import requests, re
    #获取ys168网盘根目录信息
    headersA = {"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"__yjs_duid=1_e53c16f308d9b8131bdc5b429c95189d1627049806932; ASP.NET_SessionId=f3safvppika35va5qrk0tvew","Host":"cb.ys168.com","Referer":"http://cb.ys168.com/f_ht/ajcx/000ht.html?bbh=1139","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"}
    responseA = requests.get("http://cb.ys168.com/f_ht/ajcx/ml.aspx?cz=ml_dq&_dlmc=vlsmb&_dlmm=",headers=headersA)
    soupA = BeautifulSoup(responseA.text,features="lxml")

    #获取二级目录
    headersB = {"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"__yjs_duid=1_e53c16f308d9b8131bdc5b429c95189d1627049806932; ASP.NET_SessionId=3jgr5biwyp4sbyeaoiel55vt","Host":"cb.ys168.com","Referer":"http://cb.ys168.com/f_ht/ajcx/000ht.html?bbh=1139","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"}
    responseB = requests.get("http://cb.ys168.com/f_ht/ajcx/wj.aspx?cz=dq&jsq=0&mlbh=2182217&wjpx=1&_dlmc=vlsmb&_dlmm=",headers=headersB)
    soupB = BeautifulSoup(responseB.text,features="lxml")

        #找到所有所需要的文件（包括文件夹）
        #提取名称，0位游戏相关介绍V1.5.pdf，1位AllCode.zip，2位MTE_PatchCHSV2.0.part3.cjxpak，
        #          3位MTE_PatchCHSV2.0.part2.cjxpak，4位MTE_PatchCHSV2.0.part1.cjxpak
    DLnames=[]
    DLlinksA=[]
    DLlinks=[]
    for tempsoup in soupB.findAll("a"):
        DLnames.append(tempsoup.text.replace(" ","").replace("\n",""))
        if re.findall(r'<a\shref=".*"\stitle',str(tempsoup),re.I)==[]:
            DLlinksA.extend(re.findall(r'<a\sclass="new"\shref=".*"\stitle',str(tempsoup),re.I))
        else:
            DLlinksA.extend(re.findall(r'<a\shref=".*"\stitle',str(tempsoup),re.I))
    Vertemp = DLnames.pop(0)

    #进行链接处理
    for link in DLlinksA:
        linkA = link.replace(' class="new"','')[9:][:-7]
        DLlinks.append(linkA)
    # 检查版本信息
    VersionOn = int(Vertemp[-4:-1]) / 100
    Version = 2.0
    WhetherNew = Version == VersionOn
    return (DLlinks[0:5], DLnames[0:5], WhetherNew)

def NetJudge():
    """判断网络状态"""

    import requests
    from requests.exceptions import ReadTimeout, HTTPError, RequestException

    try:
        trynet = requests.get("http://vlsmb.ys168.com", timeout=1)
    except ReadTimeout:
        return ("网络超时！请检查网络速度！", False)
    except HTTPError:
        return ("HTTP协议错误！", False)
    except RequestException:
        return ("请求网络服务失败！", False)
    else:
        if trynet.status_code == 403:
            return ("403：访问服务器被拒绝！", False)
        if trynet.status_code == 404:
            return ("404：找不到下载网站！请联系汉化组寻找相关信息！", False)
        else:
            return(None, True)

def ConsoleDownload(CtrlText, Choice, DownloadLinks):
    """联机下载文件"""
    import requests
    global Text
    for name in Choice:
        print(f"正在下载{name}，请稍后...")
        Text += f"正在下载{name}，请稍后..." + "\n"
        time_start = time.time()
        patch = requests.get(DownloadLinks[name])
        with open(name, "wb") as code:
            code.write(patch.content)
        time_end = time.time()
        print("下载完成！共用时{:.2f}秒！".format(time_end-time_start))
        Text += "下载完成！共用时{:.2f}秒！".format(time_end-time_start) + "\n"
    time.sleep(2)
    Text = None

def GetGamePath():
    """获取游戏运行的路径"""
    import psutil
    while True:
        try:
            for AllProcess in psutil.process_iter():
                if AllProcess.name() == "Millia - The ending -.exe":
                    return AllProcess.cwd()
            else:
                return None
        except:
            return None