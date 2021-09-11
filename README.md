# Millia-The-Ending-CHS-Patch-GUI
带图形界面的Millia - The Ending- 汉化补丁

运行本汉化补丁最低操作系统要求为Microsoft Windows 7 x32且仅限Windows，

本汉化补丁只需要按照程序的提示即可，但一定要注意，不要把后面的控制台窗口关掉！

（因为Python本身并不带图形编程的模块，控制台才是补丁运行的灵魂。）

本汉化补丁需要放在游戏程序本体的目录中运行，如果你不知道游戏目录，

本汉化补丁可以在游戏运行时搜索目录，也可以自行设定目录

（在Win7x64位中如果有*32程序正在运行会无法找到）。

以下是本补丁程序所用到的Python模块：

自带模块：os,sys,zipfile,shutil,platform,datetime,re,time,threating

需自行安装的模块：requests,psutil,wx


本补丁源代码的简单说明：

BinFiles.py —— 一些临时文件的二进制数据

ConsolePatch.py —— 之前的补丁程序还能直接拿来用的代码合集

Main_MTE_PatchCHS_GUI.py —— 整个程序的主脚本

PatchApp.py —— 补丁通用GUI程序的类

PatchChoice.py —— 让用户选择程序所执行的事件

PatchDeclare.py —— 汉化组声明

PatchDownload.py —— 联机下载补丁文件

PatchExit.py —— 补丁通用退出界面

PatchFinish.py —— 补丁通用结束界面

PatchInstall.py —— 补丁安装

PatchSetPath.py —— 寻找或设置游戏路径

PatchUninstall.py ——卸载汉化补丁
