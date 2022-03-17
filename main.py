import io
from urllib.request import urlopen
import icon
import tkinter as tk
import os
from base64 import b64decode
from PIL import Image,ImageTk
from chatmain import cometochat
from Weather import weathermain
from translategui import translateguimain
from video import videodownloadmain
from change import changemain
from webbrowser import open_new
import ctypes
 
def go_to_chatrobot(mainroot):
    print("go to chatrobot...")
    mainroot.destroy()
    cometochat()
def go_to_weather(mainroot):
    print("go to weather...")
    mainroot.destroy()
    weathermain()
def go_to_transgui(mainroot):
    print("go to translator...")
    mainroot.destroy()
    translateguimain()
def go_to_videodown(mainroot):
    print("go to videodown...")
    mainroot.destroy()
    videodownloadmain()
def go_to_videochange(mainroot):
    print("go to videochange...")
    mainroot.destroy()
    changemain()
def mainmake():
    mainroot = tk.Tk()
    mainroot.title("马哥多功能程序")
    mainroot.geometry('1000x673')
    mainroot.resizable(False,False)
    with open('tmp.ico','wb') as tmp:
        tmp.write(b64decode(icon.Icon().ig))
    mainroot.iconbitmap('tmp.ico')
    os.remove("tmp.ico")

    #---------------图片------------------#
    url = "https://cdn.jsdelivr.net/gh/billma007/imagesave/videodownloadimage.jpg"
    # 下载图片数据
    image_bytes = urlopen(url).read()
    # 将数据存放到data_stream中
    data_stream = io.BytesIO(image_bytes)
    # 转换为图片格式
    pil_image = Image.open(data_stream)
    # 获取图片的宽度和高度
    w, h = pil_image.size
    # 获取图片的文件名
    fname = url.split('/')[-1]
    sf = "{} ({}x{})".format(fname, w, h)
    # 将pil格式的图片转换为tk格式的image
    tk_image = ImageTk.PhotoImage(pil_image)
    # 创建个label组件, imageroot作为父节点
    labelimg = tk.Label(mainroot, image=tk_image, bg='white')
    # 设置一些padding
    #-----------------------label------------------#
    labelwel = tk.Label(mainroot,text="欢迎使用马哥多功能工具！",font=("等线",24))
    #-----------------------button-----------------#

    button_chat = tk.Button(mainroot, 
        text='马哥聊天机器人',      # 显示在按钮上的文字
        width=50, height=2, 
        command=lambda:go_to_chatrobot(mainroot))

    button_weatherui = tk.Button(mainroot, 
        text='天气查询系统',      
        width=50, height=2, 
        command=lambda:go_to_weather(mainroot))
    button_transui = tk.Button(mainroot, 
        text='翻译机(GUI版)',      
        width=50, height=2, 
        command=lambda:go_to_transgui(mainroot))
    button_videodown = tk.Button(mainroot, 
        text='**热门功能**80+网站网页视频爬取下载\n(含bilibili/Youtube等)',      
        width=50, height=2,fg="red",
        command=lambda:go_to_videodown(mainroot))
    button_videochange = tk.Button(mainroot, 
        text='视频/音频/图像转码\n(支持34种视频格式/30种音频格式/21种图像格式)',      
        width=50, height=2,fg="red",
        command=lambda:go_to_videochange(mainroot))
    button_opengithub = tk.Button(mainroot, 
        text='GitHub开源地址',      
        width=24, height=2,
        command=lambda:open_new("https://github.com/billma007/multifunction"))
    button_openblog = tk.Button(mainroot, 
        text='作者博客',      
        width=24, height=2,
        command=lambda:open_new("https://billma.top"))
    labelmore = tk.Label(mainroot,text="""Copyright (C) 2022 BillMa007|BillMa007 版权所有
本软件总体采用GNU GPL3.0版权协议
各部分采用不同的版权协议(MIT+GNU GPL2)
本软件小部分使用部分开源库且没有任何主动盈利行为
对于开源库作者和API所有者，在此表示感谢
本软件吉祥物由RUA(免费为我)绘制并已经转让著作权，在此表示感谢""",font=("等线",9))
    labelthank=tk.Label(mainroot,text="感谢您的使用！",fg="red",font=("等线",30))
    labelimg.place(x=400,y=0)
    labelwel.place(x=0,y=20)
    button_chat.place(x=0,y=100)
    button_weatherui.place(x=0,y=170)
    button_transui.place(x=0,y=240)
    button_videodown.place(x=0,y=310)
    button_videochange.place(x=0,y=380)
    button_openblog.place(x=180,y=450)
    button_opengithub.place(x=0,y=450)
    labelmore.place(x=0,y=520)
    labelthank.place(x=50,y=600)
    mainroot.mainloop()
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6)
mainmake()