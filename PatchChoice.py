# _*_ coding:utf-8 _*_
def PatchChoice(parent):
    """操作选择"""
    from PatchApp import PatchApp
    from PatchExit import PatchExit
    from PatchDownload import ChoiceDownload
    from PatchInstall import PatchInstall
    from PatchUninstall import PatchUninstall
    from BinFiles import HELPDOC
    import wx
    ChoiceWindow = PatchApp(parent)
    info1 = wx.StaticText(ChoiceWindow.panel, label="您想要做什么？", pos=(40, 40))
    info1.SetFont(ChoiceWindow.font_info)
    # 定义按钮事件
    def HELP(self):

        wx.MessageBox(HELPDOC, "Millia -The Ending-汉化补丁安装程序")

    def BACK(self):
        parent.Show()
        ChoiceWindow.frame.Bind(wx.EVT_BUTTON, None)
        ChoiceWindow.frame.Destroy()

    def NEXT(self):
        if choice.GetSelection() == 0:
            ChoiceWindow.frame.Hide()
            ChoiceDownload(ChoiceWindow.frame)
        elif choice.GetSelection() == 1:
            ChoiceWindow.frame.Hide()
            PatchInstall(ChoiceWindow.frame)
        elif choice.GetSelection() == 2:
            ChoiceWindow.frame.Hide()
            PatchUninstall(ChoiceWindow.frame)

    def EXIT(self):
        PatchExit(ChoiceWindow.frame)

    bt_help = wx.Button(ChoiceWindow.panel, label="帮助", pos=(100, 320))
    bt_back = wx.Button(ChoiceWindow.panel, label="上一步", pos=(200, 320))
    bt_next = wx.Button(ChoiceWindow.panel, label="下一步", pos=(300, 320))
    bt_cancel = wx.Button(ChoiceWindow.panel, label="退出", pos=(400, 320))
    bt_help.Bind(wx.EVT_BUTTON, HELP)
    bt_back.Bind(wx.EVT_BUTTON, BACK)
    bt_next.Bind(wx.EVT_BUTTON, NEXT)
    bt_cancel.Bind(wx.EVT_BUTTON, EXIT)
    choice = wx.RadioBox(ChoiceWindow.panel, -1, "", (40, 60), (400, 100), ["联机下载汉化补丁必要文件", "安装汉化补丁", "卸载汉化补丁"], 1, wx.RA_SPECIFY_COLS)
    choice.SetFont(ChoiceWindow.font_info)
    ChoiceWindow.frame.Show()
    ChoiceWindow.MainLoop()