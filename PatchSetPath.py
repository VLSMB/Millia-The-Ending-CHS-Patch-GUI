# _*_ coding:utf-8 _*_
def PatchSetPath(parent):
    from ConsolePatch import GetGamePath
    from PatchApp import PatchApp
    from PatchExit import PatchExit
    from PatchInstall import PatchInstall
    import wx, os, shutil
    SetPathWindow = PatchApp(parent)
    title1 = wx.StaticText(SetPathWindow.panel, label="设置游戏所在的目录。", pos=(10, 10))
    info1 = wx.StaticText(SetPathWindow.panel, label="若游戏正在运行，本补丁程序会尝试搜索游戏所在目录。", pos=(10, 50))
    info2 = wx.StaticText(SetPathWindow.panel, label="若本程序无法找到游戏目录，请点击下方的”浏览“。", pos=(10, 80))
    title1.SetFont(SetPathWindow.font_title)
    info1.SetFont(SetPathWindow.font_info)
    info2.SetFont(SetPathWindow.font_info)
    def EXIT(self):
        PatchExit(SetPathWindow.frame)

    def CONTINUE(self):
        SetPathWindow.frame.Bind(wx.EVT_CLOSE, None)
        SetPathWindow.frame.Destroy()
        if os.path.isdir(ctrl1.GetValue()):
            if os.path.exists("MTE_PatchCHSV2.0.part1.cjxpak"):
                shutil.copy(os.path.join(os.getcwd(), "MTE_PatchCHSV2.0.part1.cjxpak"),
                            os.path.join(ctrl1.GetValue(), "MTE_PatchCHSV2.0.part1.cjxpak"))
            if os.path.exists("MTE_PatchCHSV2.0.part2.cjxpak"):
                shutil.copy(os.path.join(os.getcwd(), "MTE_PatchCHSV2.0.part2.cjxpak"),
                            os.path.join(ctrl1.GetValue(), "MTE_PatchCHSV2.0.part2.cjxpak"))
            if os.path.exists("MTE_PatchCHSV2.0.part3.cjxpak"):
                shutil.copy(os.path.join(os.getcwd(), "MTE_PatchCHSV2.0.part3.cjxpak"),
                            os.path.join(ctrl1.GetValue(), "MTE_PatchCHSV2.0.part3.cjxpak"))
            os.chdir(ctrl1.GetValue())
        PatchInstall(parent)

    def SET(self):
        """设置运行目录"""
        dlg = wx.DirDialog(SetPathWindow.frame, u"选择文件夹", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            ctrl1.SetValue(dlg.GetPath())# 文件夹路径
        dlg.Destroy()
        CONTINUE(None)

    def BACK(self):
        parent.Show()
        SetPathWindow.frame.Bind(wx.EVT_CLOSE, None)
        SetPathWindow.frame.Destroy()
    bt_continue = wx.Button(SetPathWindow.panel, label="重试", pos=(100, 320))
    bt_set = wx.Button(SetPathWindow.panel, label="浏览", pos=(200, 320))
    bt_back = wx.Button(SetPathWindow.panel, label="上一步", pos=(300, 320))
    bt_cancel = wx.Button(SetPathWindow.panel, label="退出", pos=(400, 320))
    bt_set.Bind(wx.EVT_BUTTON, SET)
    bt_back.Bind(wx.EVT_BUTTON, BACK)
    bt_cancel.Bind(wx.EVT_BUTTON, EXIT)
    bt_continue.Bind(wx.EVT_BUTTON, CONTINUE)
    ctrl1 = wx.TextCtrl(SetPathWindow.panel, value="", pos=(10, 100), size=(450, 30),
                        style=wx.TE_RICH2 | wx.TE_READONLY)
    if GetGamePath() is not None:
        ctrl1.SetValue(GetGamePath())
    SetPathWindow.frame.Show()
    SetPathWindow.MainLoop()
# 改完目录后，要将cjx文件转移到新的目录