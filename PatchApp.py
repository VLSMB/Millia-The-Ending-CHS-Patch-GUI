# _*_ coding:utf-8 _*_
import wx
from PatchExit import PatchExit
class PatchApp(wx.App):
    """定义应用程序类"""
    def __init__(self, parent):
        self.parent = parent
        super().__init__()

    def PATCHEXIT(self, none):
        PatchExit(self.frame)

    def OnInit(self):
        frame = wx.Frame(parent=self.parent, title="Mllia -The Ending- 汉化补丁安装程序",
                         style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX, size=(500, 400))
        frame.SetMaxSize((500, 400))
        frame.SetMinSize((500, 400))
        frame.Show()
        frame.Bind(wx.EVT_CLOSE, self.PATCHEXIT)
        self.panel = wx.Panel(frame, size=(500, 400))
        self.frame = frame
        self.font_title = wx.Font(25, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.BOLD)
        self.font_info = wx.Font(14, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        return True