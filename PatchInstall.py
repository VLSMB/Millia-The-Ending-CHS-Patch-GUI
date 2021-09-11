# _*_ coding:utf-8 _*_

def WhetherGameExist():
    """判断游戏文件是否完整"""
    import os
    from ConsolePatch import ZipError
    # 收集运行环境信息
    VERSION = "V2.0"
    mteapp = os.path.exists("Millia - The ending -.exe")
    mtechs1 = os.path.exists("MTE_PatchCHS" + VERSION + ".part1.cjxpak")
    mtechs2 = os.path.exists("MTE_PatchCHS" + VERSION + ".part2.cjxpak")
    mtechs3 = os.path.exists("MTE_PatchCHS" + VERSION + ".part3.cjxpak")
    mterpa = os.path.exists(r"game\archive.rpa")
    mterenpy = os.path.exists("renpy")
    mtelib = os.path.exists("lib")
    mtechs = mtechs1 and mtechs2 and mtechs3
    ziperror = ZipError()
    # 声明常量
    mtejudge = [mteapp, mtechs, mterpa, mterenpy, mtelib, ziperror]
    mtestring = ["缺失游戏运行程序Millia - The ending -.exe", "缺失汉化补丁MTE_PatchCHS" + VERSION + ".cjxpak(共3个)", "缺失游戏数据archive.rpa",
                 "缺失游戏引擎文件夹renpy", "缺失游戏运行库文件夹lib", "汉化补丁cjxpak文件损坏"]
    # 判断游戏是否完整
    for index, judge in enumerate(mtejudge):
        if not judge:
            return (False, mtestring[index])
    else:
        return (True, None)

def PatchInstall(parent):
    """安装汉化补丁的重要部分"""
    import wx
    from threading import Thread
    from PatchExit import PatchExit
    from PatchApp import PatchApp
    from PatchSetPath import PatchSetPath
    from ConsolePatch import ConsoleInstall
    from PatchFinish import PatchFinish
    judge = WhetherGameExist()
    if not judge[0]:
        # 定义按钮操作
        def EXIT(self):
            PatchExit(FailWindow.frame)
        def CONTINUE(self):
            FailWindow.frame.Bind(wx.EVT_CLOSE, None)
            FailWindow.frame.Destroy()
            PatchInstall(parent)
        def SET(self):
            """设置运行目录"""
            FailWindow.frame.Hide()
            PatchSetPath(FailWindow.frame)
            CONTINUE(None)
        def BACK(self):
            parent.Show()
            FailWindow.frame.Bind(wx.EVT_CLOSE, None)
            FailWindow.frame.Destroy()
        FailWindow = PatchApp(parent)
        title1 = wx.StaticText(FailWindow.panel, label="安装程序无法继续", pos=(10, 10))
        title1.SetFont(FailWindow.font_title)
        info1 = wx.StaticText(FailWindow.panel, label="原因：{}".format(judge[1]), pos=(10, 60))
        info2 = wx.StaticText(FailWindow.panel, label="请将本汉化补丁程序放在游戏目录之下运行，", pos=(10, 90))
        info3 = wx.StaticText(FailWindow.panel, label="或者点击下方的“设置目录”改变本补丁的安装位置。", pos=(10, 120))
        info4 = wx.StaticText(FailWindow.panel, label="缺失cjxpak补丁文件请选择联机下载。", pos=(10, 150))
        info1.SetFont(FailWindow.font_info)
        info2.SetFont(FailWindow.font_info)
        info3.SetFont(FailWindow.font_info)
        info4.SetFont(FailWindow.font_info)
        bt_continue = wx.Button(FailWindow.panel, label="重试", pos=(100, 320))
        bt_set = wx.Button(FailWindow.panel, label="设置目录", pos=(200, 320))
        bt_back = wx.Button(FailWindow.panel, label="上一步", pos=(300, 320))
        bt_cancel = wx.Button(FailWindow.panel, label="退出", pos=(400, 320))
        bt_set.Bind(wx.EVT_BUTTON, SET)
        bt_back.Bind(wx.EVT_BUTTON, BACK)
        bt_cancel.Bind(wx.EVT_BUTTON, EXIT)
        bt_continue.Bind(wx.EVT_BUTTON, CONTINUE)
        FailWindow.frame.Show()
        FailWindow.MainLoop()
    else:
        def CTRLTEXT():
            while True:
                from ConsolePatch import Text
                ctrl1.SetInsertionPointEnd()
                if Text == None:
                    bt_next.Enable()
                    WhyNeedCreateTheApp = wx.App()
                    InstallWindow.frame.Bind(wx.EVT_CLOSE, FINISH)
                    wx.MessageBox("汉化补丁安装成功！", "Millia -The Ending- 汉化补丁安装程序")
                    break
                ctrl1.SetValue(Text)
        def FINISH(self):
            InstallWindow.frame.Hide()
            PatchFinish("安装")
        def INSTALL(self):
            bt_install.Disable()
            info1.SetLabel("正在安装汉化补丁，请稍后：")
            ConSoleGUI1 = Thread(target=ConsoleInstall)
            ConSoleGUI2 = Thread(target=CTRLTEXT)
            ConSoleGUI1.start()
            ConSoleGUI2.start()

        InstallWindow = PatchApp(parent)
        info1 = wx.StaticText(InstallWindow.panel, label="请按“安装”键安装汉化补丁。", pos=(10, 30))
        info1.SetFont(InstallWindow.font_info)
        ctrl1 = wx.TextCtrl(InstallWindow.panel, value="", pos=(10, 60), size=(460, 250),
                            style=wx.TE_MULTILINE | wx.TE_RICH2 | wx.TE_READONLY)
        bt_install = wx.Button(InstallWindow.panel, label="安装", pos=(300, 320))
        bt_next = wx.Button(InstallWindow.panel, label="完成并退出", pos=(400, 320))
        bt_next.Bind(wx.EVT_BUTTON, FINISH)
        bt_next.Disable()
        bt_install.Bind(wx.EVT_BUTTON, INSTALL)
        InstallWindow.frame.Show()
        InstallWindow.MainLoop()



