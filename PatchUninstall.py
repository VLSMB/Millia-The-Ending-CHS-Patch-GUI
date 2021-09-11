# _*_ coding:utf-8 _*_
def PatchUninstall(parent):
    """卸载汉化补丁"""
    import wx, os, time
    from PatchExit import PatchExit
    from PatchApp import PatchApp
    from ConsolePatch import ConsoleUninstall, UninstallZip
    from PatchFinish import PatchFinish
    from threading import Thread
    def UnintallError(reason):
        def EXIT(self):
            PatchExit(FailWindow.frame)
        def BACK(self):
            parent.Show()
            FailWindow.frame.Bind(wx.EVT_CLOSE, None)
            FailWindow.frame.Destroy()
        FailWindow = PatchApp(parent)
        title1 = wx.StaticText(FailWindow.panel, label="安装程序无法继续", pos=(10, 10))
        title1.SetFont(FailWindow.font_title)
        info1 = wx.StaticText(FailWindow.panel, label="原因：{}".format(reason), pos=(10, 60))
        info2 = wx.StaticText(FailWindow.panel, label="只有安装过汉化补丁，才能卸载汉化补丁。", pos=(10, 90))
        info1.SetFont(FailWindow.font_info)
        info2.SetFont(FailWindow.font_info)
        bt_back = wx.Button(FailWindow.panel, label="上一步", pos=(300, 320))
        bt_cancel = wx.Button(FailWindow.panel, label="退出", pos=(400, 320))
        bt_back.Bind(wx.EVT_BUTTON, BACK)
        bt_cancel.Bind(wx.EVT_BUTTON, EXIT)
        FailWindow.frame.Show()
        FailWindow.MainLoop()
    if not os.path.exists("MTE_PatchENG.cjxpak"):
        UnintallError("未找到备份文件MTE_PatchENG.cjxpak")
    elif not UninstallZip():
        UnintallError("备份文件MTE_PatchENG.cjxpak损坏")
    else:
        def CTRLTEXT():
            while True:
                from ConsolePatch import Text
                ctrl1.SetInsertionPointEnd()
                if Text == None:
                    bt_next.Enable()
                    WhyNeedCreateTheApp = wx.App()
                    UninstallWindow.frame.Bind(wx.EVT_CLOSE, FINISH)
                    wx.MessageBox("汉化补丁卸载成功！", "Millia -The Ending- 汉化补丁安装程序")
                    break
                ctrl1.SetValue(Text)
        def FINISH(self):
            UninstallWindow.frame.Hide()
            PatchFinish("卸载")
        def UNINSTALL(self):
            bt_install.Disable()
            info1.SetLabel("正在卸载汉化补丁，请稍后：")
            ConSoleGUI1 = Thread(target=ConsoleUninstall)
            ConSoleGUI2 = Thread(target=CTRLTEXT)
            ConSoleGUI1.start()
            ConSoleGUI2.start()
        UninstallWindow = PatchApp(parent)
        info1 = wx.StaticText(UninstallWindow.panel, label="请按“卸载”键卸载汉化补丁。", pos=(10, 30))
        info1.SetFont(UninstallWindow.font_info)
        ctrl1 = wx.TextCtrl(UninstallWindow.panel, value="", pos=(10, 60), size=(460, 250),
                            style=wx.TE_MULTILINE | wx.TE_RICH2 | wx.TE_READONLY)
        bt_install = wx.Button(UninstallWindow.panel, label="卸载", pos=(300, 320))
        bt_next = wx.Button(UninstallWindow.panel, label="完成并退出", pos=(400, 320))
        bt_next.Bind(wx.EVT_BUTTON, FINISH)
        bt_next.Disable()
        bt_install.Bind(wx.EVT_BUTTON, UNINSTALL)
        UninstallWindow.frame.Show()
        UninstallWindow.MainLoop()
