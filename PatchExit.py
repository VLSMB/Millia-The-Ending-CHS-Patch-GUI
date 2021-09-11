# _*_ coding:utf-8 _*_
def PatchExit(parent):
    """补丁通用退出界面"""

    import wx, sys, os
    from PatchApp import PatchApp
    from BinFiles import Millia
    def OUT(self):
        sys.exit()
    info_exit = wx.MessageBox("安装未完成，真的要退出吗？", "Millia -The Ending-汉化补丁安装程序", wx.YES_NO | wx.NO_DEFAULT)
    if info_exit == 2:
        parent.Hide()
        EXIT = PatchApp(None)
        title1 = wx.StaticText(EXIT.panel, label="Millia -The Ending-", pos=(130, 10))
        title2 = wx.StaticText(EXIT.panel, label="汉化补丁安装程序", pos=(130, 40))
        info1 = wx.StaticText(EXIT.panel, label="补丁安装程序被终止，安装未成功。", pos=(130, 90))
        info2 = wx.StaticText(EXIT.panel, label="请按”完成“退出。", pos=(130, 120))
        coder = wx.StaticText(EXIT.panel, label="Designed by VLSMB", pos=(130, 320))
        title1.SetFont(EXIT.font_title)
        title2.SetFont(EXIT.font_title)
        info1.SetFont(EXIT.font_info)
        info2.SetFont(EXIT.font_info)
        with open("temp.jpg", "wb") as file:
            file.write(Millia)
        image = wx.Image("temp.jpg", wx.BITMAP_TYPE_JPEG)
        image.Rescale(130, 300)
        mypic = image.ConvertToBitmap()
        wx.StaticBitmap(EXIT.panel, bitmap=mypic, pos=(0, 40))
        os.remove("temp.jpg")
        bt_cancel = wx.Button(EXIT.panel, label="完成", pos=(400, 310))
        bt_cancel.Bind(wx.EVT_BUTTON, OUT)
        EXIT.frame.Bind(wx.EVT_CLOSE, OUT)
        EXIT.MainLoop()
        sys.exit()

