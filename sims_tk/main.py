import os
import tkinter as tk

from PIL import Image, ImageTk

from LoginPage import LoginPage

CUSTOM_ICO = 'head.ico'     # 自定义logo


def set_up_SIMS():
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    ico = os.path.join(ROOT_PATH, CUSTOM_ICO)
    root = tk.Tk()
    LoginPage(root)
    # 设置图标
    load = Image.open(ico)
    img = ImageTk.PhotoImage(load)
    root.tk.call('wm', 'iconphoto', root._w, img)
    # 设置尺寸和位置
    root.geometry('430x320+350+150')
    root.minsize(430, 320)
    root.resizable(0, 0)       # 暂时防止用户调整尺寸
    root.mainloop()


if __name__ == "__main__":
    set_up_SIMS()       # 启动信息管理系统
