# _*_ coding:utf-8 _*_
def ChoiceDownload(parent):
    """联机下载汉化补丁文件"""
    import wx
    from PatchApp import PatchApp
    from ConsolePatch import GetDownloadLink, NetJudge
    from PatchExit import PatchExit
    judge = NetJudge()
    if not judge[1]:
        # 定义按钮操作
        def EXIT(self):
            PatchExit(FailWindow.frame)

        def CONTINUE(self):
            FailWindow.frame.Bind(wx.EVT_CLOSE, None)
            FailWindow.frame.Destroy()
            ChoiceDownload(parent)

        def BACK(self):
            parent.Show()
            FailWindow.frame.Bind(wx.EVT_CLOSE, None)
            FailWindow.frame.Destroy()

        FailWindow = PatchApp(parent)
        title1 = wx.StaticText(FailWindow.panel, label="安装程序无法继续", pos=(10, 10))
        title1.SetFont(FailWindow.font_title)
        info1 = wx.StaticText(FailWindow.panel, label="原因：{}".format(judge[0]), pos=(10, 60))
        info2 = wx.StaticText(FailWindow.panel, label="请检查网络连接是否正常。", pos=(10, 90))
        info1.SetFont(FailWindow.font_info)
        info2.SetFont(FailWindow.font_info)
        bt_continue = wx.Button(FailWindow.panel, label="重试", pos=(200, 320))
        bt_back = wx.Button(FailWindow.panel, label="上一步", pos=(300, 320))
        bt_cancel = wx.Button(FailWindow.panel, label="退出", pos=(400, 320))
        bt_back.Bind(wx.EVT_BUTTON, BACK)
        bt_cancel.Bind(wx.EVT_BUTTON, EXIT)
        bt_continue.Bind(wx.EVT_BUTTON, CONTINUE)
        FailWindow.frame.Show()
        FailWindow.MainLoop()
    else:
        def BACK(self):
            parent.Show()
            DownloadWindow.frame.Bind(wx.EVT_BUTTON, None)
            DownloadWindow.frame.Destroy()
        def EXIT(self):
            PatchExit(DownloadWindow.frame)
        def NEXT(self):
            finalchoice = []
            for check in checks:
                if check.IsChecked():
                    finalchoice.append(check.GetLabel())
            else:
                if finalchoice == []:
                    wx.MessageBox("请选择要下载的文件！", "Mllia -The Ending- 汉化补丁安装程序")
                else:
                    DownloadWindow.frame.Hide()
                    PatchDownload(DownloadWindow.frame, finalchoice, DownloadLinks)
        DownloadWindow = PatchApp(parent)
        info1 = wx.StaticText(DownloadWindow.panel, label="您想要下载什么？", pos=(40, 40))
        info1.SetFont(DownloadWindow.font_info)
        DownloadInfo = GetDownloadLink()
        # return (DLlinks[0:5], DLnames[0:5], WhetherNew)
        if not DownloadInfo[2]:
            info2 = wx.StaticText(DownloadWindow.panel, label="（本补丁程序不是最新版本，请获取最新版的补丁程序）", pos=(10, 60))
            info2.SetFont(DownloadWindow.font_info)
        info3 = wx.StaticText(DownloadWindow.panel, label="其中，cjxpak是运行补丁程序的必要文件。", pos=(40, 80))
        info3.SetFont(DownloadWindow.font_info)
        # 复选框
        DownloadLinks = dict(zip(DownloadInfo[1], DownloadInfo[0]))
        checks = []
        for index, name in enumerate(list(DownloadLinks.keys())):
            tempcheck = wx.CheckBox(parent=DownloadWindow.panel, label=name, size=(400, 20), pos=(40, 110+30*index)) # +30
            tempcheck.SetFont(DownloadWindow.font_info)
            checks.append(tempcheck)
            del tempcheck
        bt_back = wx.Button(DownloadWindow.panel, label="上一步", pos=(200, 320))
        bt_next = wx.Button(DownloadWindow.panel, label="下一步", pos=(300, 320))
        bt_cancel = wx.Button(DownloadWindow.panel, label="退出", pos=(400, 320))
        bt_back.Bind(wx.EVT_BUTTON, BACK)
        bt_next.Bind(wx.EVT_BUTTON, NEXT)
        bt_cancel.Bind(wx.EVT_BUTTON, EXIT)
        DownloadWindow.frame.Show()
        DownloadWindow.MainLoop()

def PatchDownload(parent, Choice, DownloadLinks):
    """下载文件"""
    from PatchFinish import PatchFinish
    from PatchApp import PatchApp
    from ConsolePatch import ConsoleDownload
    from threading import Thread
    import wx, time
    def CTRLTEXT():
        while True:
            from ConsolePatch import Text
            ctrl1.SetInsertionPointEnd()
            if Text == None:
                bt_next.Enable()
                WhyNeedCreateTheApp = wx.App()
                Downloading.frame.Bind(wx.EVT_CLOSE, FINISH)
                wx.MessageBox("文件下载成功！", "Millia -The Ending- 汉化补丁安装程序")
                break
            ctrl1.SetValue(Text)
    def FINISH(self):
        Downloading.frame.Hide()
        PatchFinish("下载")
    def TEMP():
        ConsoleDownload(None, Choice, DownloadLinks)

    def DOWNLOAD(self):
        bt_install.Disable()
        info1.SetLabel("正在下载汉化补丁，请稍后：")
        #ConsoleDownload(ctrl1, Choice, DownloadLinks)
        ConSoleGUI1 = Thread(target=TEMP)
        ConSoleGUI2 = Thread(target=CTRLTEXT)
        ConSoleGUI1.start()
        ConSoleGUI2.start()
    Downloading = PatchApp(parent)
    info1 = wx.StaticText(Downloading.panel, label="请按“下载”键下载文件。", pos=(10, 30))
    info1.SetFont(Downloading.font_info)
    ctrl1 = wx.TextCtrl(Downloading.panel, value="", pos=(10, 60), size=(460, 250),
                        style=wx.TE_MULTILINE | wx.TE_RICH2 | wx.TE_READONLY)
    bt_install = wx.Button(Downloading.panel, label="下载", pos=(300, 320))
    bt_next = wx.Button(Downloading.panel, label="完成并退出", pos=(400, 320))
    bt_next.Bind(wx.EVT_BUTTON, FINISH)
    bt_next.Disable()
    bt_install.Bind(wx.EVT_BUTTON, DOWNLOAD)
    Downloading.frame.Show()
    Downloading.MainLoop()