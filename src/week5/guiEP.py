# -*- coding: utf-8 -*-

import wx


# 实现在程序Frame中按下鼠标左键时，在鼠标按下的位置出现一个Button
class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, None, title='Hello Python')
        self.panel = wx.Panel(self)
        self.panel.Bind(wx.EVT_LEFT_UP, self.OnClick)

    def OnClick(self, event):
        posm = event.GetPosition()
        wx.Button(self.panel, label="Hi~~~", pos=(posm.x, posm.y))


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None)
    frame.Show(True)
    app.MainLoop()
