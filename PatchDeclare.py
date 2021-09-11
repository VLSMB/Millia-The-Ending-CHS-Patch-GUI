# _*_ coding:utf-8 _*_

def PatchDeclare(parent):
    """汉化组声明"""
    from PatchApp import PatchApp
    from PatchExit import PatchExit
    from PatchChoice import PatchChoice
    from BinFiles import declaration
    import wx
    DeclareWindow = PatchApp(parent)
    info1 = wx.StaticText(DeclareWindow.panel, label="请仔细阅读以下文档，同意则继续安装本汉化补丁：", pos=(10, 30))
    info1.SetFont(DeclareWindow.font_info)
    ctrl1 = wx.TextCtrl(DeclareWindow.panel, value=declaration, pos=(10, 60), size=(460, 250), style=wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_READONLY)
    def EXIT(self):
        """退出程序"""
        PatchExit(DeclareWindow.frame)
    def NEXT(self):
        DeclareWindow.frame.Hide()
        PatchChoice(DeclareWindow.frame)
    bt_next = wx.Button(DeclareWindow.panel, label="同意并继续", pos=(300, 320))
    bt_cancel = wx.Button(DeclareWindow.panel, label="退出", pos=(400, 320))
    bt_cancel.Bind(wx.EVT_BUTTON, EXIT)
    bt_next.Bind(wx.EVT_BUTTON, NEXT)
    DeclareWindow.MainLoop()
