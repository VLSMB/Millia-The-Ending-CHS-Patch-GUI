# _*_ coding:utf-8 _*_

def PatchFinish(text):
    """操作结束之后的界面"""
    import wx, sys, os
    from PatchApp import PatchApp
    from BinFiles import Millia
    def OUT(self):
        sys.exit()
    FinishWindow = PatchApp(None)
    title1 = wx.StaticText(FinishWindow.panel, label="Millia -The Ending-", pos=(130, 10))
    title2 = wx.StaticText(FinishWindow.panel, label="汉化补丁安装程序", pos=(130, 40))
    info1 = wx.StaticText(FinishWindow.panel, label="补丁{}成功，汉化组祝您游戏愉快。".format(text), pos=(130, 90))
    info2 = wx.StaticText(FinishWindow.panel, label="请按”完成“退出。", pos=(130, 120))
    coder = wx.StaticText(FinishWindow.panel, label="Designed by VLSMB", pos=(130, 320))
    title1.SetFont(FinishWindow.font_title)
    title2.SetFont(FinishWindow.font_title)
    info1.SetFont(FinishWindow.font_info)
    info2.SetFont(FinishWindow.font_info)
    with open("temp.jpg", "wb") as file:
        file.write(Millia)
    image = wx.Image("temp.jpg", wx.BITMAP_TYPE_JPEG)
    image.Rescale(130, 300)
    mypic = image.ConvertToBitmap()
    wx.StaticBitmap(FinishWindow.panel, bitmap=mypic, pos=(0, 40))
    os.remove("temp.jpg")
    bt_cancel = wx.Button(FinishWindow.panel, label="完成", pos=(400, 310))
    bt_cancel.Bind(wx.EVT_BUTTON, OUT)
    FinishWindow.frame.Bind(wx.EVT_CLOSE, OUT)
    FinishWindow.MainLoop()
    sys.exit()
