# _*_ coding:utf-8 _*_
if __name__ == "__main__":
    import os,wx,datetime,platform
    from PatchExit import PatchExit
    from PatchApp import PatchApp
    from PatchDeclare import PatchDeclare
    from BinFiles import Millia
    # 控制台输出信息
    os.system("title Millia -The Ending- 简体中文补丁V2.0 控制台部分 （请不要关闭本窗口！！！）")
    print("Millia -The Ending-游戏汉化补丁V2.0 超巨星汉化组测试版")
    now = datetime.datetime.now()
    print("当前时间：", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("计算机操作系统信息：", platform.platform(), platform.machine())
    print("\n强烈声明：本汉化补丁仅供学习交流，任何人、任何组织均不可以拿本补丁或打好补丁的游戏进行任何以谋取利益的买卖交易！")
    print("本补丁是免费资源！若您是购买而来，请及时举报商家！")
    print("请大家自觉保护GalGame资源，如果有人拿此买卖，请大家及时举报！")
    print("=" * 50)
    print("本窗口是汉化补丁的控制台部分，在补丁程序未结束之前请不要关闭本窗口！！！")
    print("（本补丁程序可能在Windows 7系统中输出大量的”unsupported local setting“，忽略即可。）")
    print("=" * 50)
    MainWindow = PatchApp(None)

    def EXIT(self):
        """退出程序"""
        PatchExit(MainWindow.frame)


    def DECLARE(self):
        """汉化组声明"""
        MainWindow.frame.Hide()
        PatchDeclare(MainWindow.frame)


    # 初始化主窗口
    title1 = wx.StaticText(MainWindow.panel, label="Millia -The Ending-", pos=(130, 10))
    title2 = wx.StaticText(MainWindow.panel, label="汉化补丁安装程序", pos=(130, 40))
    info1 = wx.StaticText(MainWindow.panel, label="请根据安装向导的提示完成补丁的安装，", pos=(130, 90))
    info2 = wx.StaticText(MainWindow.panel, label="继续请按“下一步”，退出则按“退出”", pos=(130, 120))
    coder = wx.StaticText(MainWindow.panel, label="Designed by VLSMB", pos=(130, 320))
    title1.SetFont(MainWindow.font_title)
    title2.SetFont(MainWindow.font_title)
    info1.SetFont(MainWindow.font_info)
    info2.SetFont(MainWindow.font_info)
    bt_next = wx.Button(MainWindow.panel, label="下一步", pos=(300, 310))
    bt_cancel = wx.Button(MainWindow.panel, label="退出", pos=(400, 310))
    bt_cancel.Bind(wx.EVT_BUTTON, EXIT)
    bt_next.Bind(wx.EVT_BUTTON, DECLARE)
    with open("temp.jpg", "wb") as file:
        file.write(Millia)
    image = wx.Image("temp.jpg", wx.BITMAP_TYPE_JPEG)
    image.Rescale(130, 300)
    mypic = image.ConvertToBitmap()
    wx.StaticBitmap(MainWindow.panel, bitmap=mypic, pos=(0, 40))
    os.remove("temp.jpg")
    MainWindow.MainLoop()