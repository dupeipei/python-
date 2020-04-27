"""
目标：
    原意为色盲患者识别屏幕的颜色，识别折线图中不同的折线颜色。
原理：
    通过键盘输入按键（默认空格键）获取当前鼠标的像素值，显示在屏幕上，同时显示像素名称，方便找到一样颜色的折线。
使用方式：
    1.python GetPixel.py
    2.跳转到要识别的页面，点击选中程序框
    3.鼠标移动到要识别的颜色上
    4.按下空格键显示RGB颜色(选中程序框之后可多次识别)
    5.退出程序
参数：
    key:设定的键盘按键
    show_position:显示RGB颜色的位置

需要：
    安装tkinter, macOS建议使用python3.7.0，自带tkinter6.8，同时运行tkinker系统不会崩溃。
    pip install pillow
    pip install PyUserInput
"""

from PIL import ImageGrab
import tkinter as tk
from tkinter import *
from pymouse import PyMouse
import webcolors

key = ' '
show_position = (1000, 10)


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


def keyboard(event):
    if event.char == key:
        # print("点击键盘", repr(event.char))
        global label, label2
        # position = event.x, event.y
        position = PyMouse().position()
        img = ImageGrab.grab()
        img = img.convert("RGB").load()
        color = img[int(position[0]*2), int(position[1]*2)]
        _, color_name = get_colour_name(color)
        # print("colour name:", color_name)

        text = "R:%d   G:%d   B:%d" % (color[0], color[1], color[2])
        text2 = "%s" % color_name
        # print(text+"     position:%d %d" % (position[0], position[1]))

        # pic = ImageGrab.grab().convert("RGB")
        # x = int(position[0]*2)
        # y = int(position[1]*2)
        # croped = pic.crop((x-20, y-20, x+20, y+20))
        # croped.show()

        label.pack_forget()
        label2.pack_forget()
        label = tk.Label(frame, text=text, fg="black", bg="white")
        label2 = tk.Label(frame, text=text2, fg="black", bg="white")
        label.pack()
        label2.pack()


root=Tk(className=" RGB颜色")
root.geometry("150x40+%d+%d" % (show_position[0], show_position[1]))

# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# print(screen_width,screen_height)

#框架与键盘空格进行绑定
frame = Frame(root, width=150, height=40)
frame.bind("<Key>", keyboard)
frame.focus_set()
frame.pack()

label = tk.Label(frame, text="new start", fg="black", bg="white")
label2 = tk.Label(frame, text=" ", fg="black", bg="white")
label.pack()
label2.pack()

mainloop()


