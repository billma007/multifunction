import io
import multiprocessing
import os
import sys
from urllib.request import urlopen
import icon
import tkinter as tk
from os import remove
from base64 import b64decode
from PIL import Image,ImageTk
from chatmain import cometochat
from weather_tkinter import gotoweather
from translategui import translateguimain
from video import videodownloadmain
from covid import createcovidtoplevel
from webbrowser import open_new
from playsound import playsound,PlaysoundException
import urllib.request
import tkinter.messagebox
import htmltest
def getHtml(url):
    
    response = urllib.request.urlopen(url)
    html = response.read()
    html=html.decode("utf-8")
    return html 
def callbackClose():

    destroyask=tkinter.messagebox.askokcancel(title="提示",message="真的要退出吗？")
    if destroyask ==True:
        musicplay.terminate()
        os._exit(0x0)
def playmusic():
    try:
        while True:
            playsound("https://cdn.jsdelivr.net/gh/billma007/imagesave/multimusic.mp3")
    except PlaysoundException or Exception:
        print("PLAY ERROR")
        
def go_to_chatrobot():
    print("go to chatrobot...")
    cometochat()
def go_to_weather():
    print("go to weather...")
    gotoweather()
def go_to_transgui():
    print("go to translator...")
    translateguimain()
def go_to_videodown():
    print("go to videodown...")
    videodownloadmain()
def go_to_covid():
    print("go to videochange...")
    createcovidtoplevel()

def learnmore():
    lm=tk.Toplevel()
    lm.geometry('500x500')
    lmtext="""有关本软件的使用

特别通知：在新版本中已经不再支持ffmpeg驱动的视频转码
如果您要视频转码请选择其他软件。

0.目前存在的bug

|-1.在强制关闭该软件时音乐播放进程无法关闭
|   解决办法：请通过正常方法关闭软件
|   如果发生了此事，请通过任务管理器关闭进程
|
|-2.在下载视频时会出现进程卡死的情况
    原因：Threading不支持mainloop的线程多开
    multiprocessing只能在__name__=="__main__"进行
    解决办法：别急，过一会会自动开始的
    （在此之间不要使用其他功能）

1.如果您有任何问题，请通过以下形式联系我：
QQ：36937975
Twitter：@billma007cool
Facebook:billma007
Email:maboning237103015@163.com
Website:https://billma.top
Github Issues:https://github.com/billma007/multifunction/issues

2.使用前必看
本软件集成了查天气，中英互译，AI聊天，视频下载，视频/图像/音频的转码与转换
其中转码需要下载ffmpeg插件，在下载完以后本软件会自动安装与删除
由于调用堆栈的问题,请勿在主页与分功能页面之间连续切换超过6次
如果该软件停止工作，直接关闭即可（可以打开任务管理器）
如果本软件发生了bug，可以通过以上联系方式来联系我。
如果您对本软件优化有好建议，欢迎联系我。
本软件由作者一己之力完成全部代码，请原谅一下bug吧....
人生苦短，我用Python！

3.关于作者
高中牲，坐标中国苏州工业园区，热爱编程，擅长的语言有C/C++,Python,略懂Shell,JavaScript,Nodejs
此外，作者还擅长小提琴，口琴，魔方，摄影，音游（划去）等
信息学奥林匹克竞赛(中国)选手，只打到了NoiP的蒟蒻
欢迎联系我，和我探讨更多兴趣

4.更新日志
|-2022年3月28日--1.2.5版本：
|   |-1.取消了转码功能
|   |-2.增加了新冠疫情查询功能
|   |-3.修复了翻译、聊天、天气查询的bug
|-2022年3月25日--1.2.4版本：
|   |-1.更新了更新系统
|   |2.修复了ffmpeg的相关bug，增加了批量转码功能
|   |-3.优化了聊天系统
|-2022年3月24日--1.2.3dev1版本：
|   |-1.将sys.exit(0)改成了os._exit(0)使所有进程退出
|   |-2.修改了you-get的源码来防止buffer输出缓存问题；
|   |  在you-get.common中注释掉下列表达式：
|   |sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
|-2022年3月24日--1.2.3版本：
|   |-1.再次修复了playsound函数抽风导致音乐停不下来的问题
|   |-2.谁他妈知道fastly.jsdelivr.net也抽风
|   |     所以我决定双保险，在cdn与fastly之间取最大值来保持更新
|   |-3.优化更新系统，新增cdn线路
|   |-4.修复了部分窗口部分按钮激活无效函数的bug
|-2022年3月24日--1.2.2版本：
|   |-1.重构代码，开启多线程来防止卡死
|   |-2.修复了转码功能报错的问题
|   |-3.修复了关闭程序后仍在播放音乐的bug
|   |-4.修复了使用某功能后再点击停止音乐出线bug的问题
|   |-5.代码结构改变：支持功能多开
|   |-6.修复了部分按钮不动的bug
|   |-7.由于cdn.jsdelivr.net老是抽风，决定使用fastly加速
|-2022年3月22日--1.2.1版本：
|   |-1.修复了sys.stdout没有重定向至text文本框导致无法显示进度的问题
|   |-2.将stdout改成__stdout__保证软件安全
|   |-3.将sys.stderr也重定向至文本框
|   |-4.使用sys.exit()抛出异常来结束软件，而不是os.exit()
|   |-5.[1.2.1div2]添加自动更新系统
|        |-原理：在GitHub上添加以下两个文件来进行检索更新
|        |            |-updetecheck.txt
|        |            |-xxx.exe[软件的最新版本]
|        |-将最新版本上传至updatecheck
|        |-本地使用urllib.request爬取内容
|        |-如果版本号与当前版本号不同即为更新
|        |-随后使用requests爬取文件写入本地文档
|        |-如果在中国大陆，会自动使用jsdelivr进行加速
|-2022年3月21日--1.1.0版本
|   |-推翻原代码重构，扩充了以下功能：
|   |-1.查天气
|   |-2.AI聊天
|   |-3.放音乐
|   |-4.添加了几个按钮
|   |-5.开启多线程
"""
    lmtx=tk.Text(lm,height=35,width=90)
    lmtx.insert(tk.INSERT,lmtext)
    lmtx.update()
    lmtx.config(state=tk.DISABLED)
    lmtx.pack()
    lm.mainloop()
def copyr():
    lmcp=tk.Toplevel()
    lmcp.geometry('500x500')
    crtxt='''打开本软件，意味着您已经同意了以下内容。
    
版权协议：

Copyright (C) 2022 BillMa007|BillMa007 版权所有
本软件不支持英文，但是允许开发者在保留全部信息的情况下进行翻译或本地化
This Program doesn't support English,but welcome developers from all over the world to translate it with all information included.
本软件总体采用GNU GPL3.0版权协议，请尊守版权协议
各部分采用不同的版权协议(MIT+GNU GPL2)
本软件小部分使用部分开源库且没有任何主动盈利行为
本软件可能在您知情的情况下下载本软件的最新版本
本软件使用Python3.8.10和3.10.2制作，兼容3.7-3.10
本软件开源地址：https://github.com/billma007/multifunction/
本软件内任何素材均为Billma007版权所有，未经允许禁止在任何地方他用
本软件开源，开源作者不承担您使用该软件导致的任何后果
请在遵守当地/所在国家的所有法律的前提下使用该软件
请注意：作者不承担您任何使用该软件导致的任何后果！
未经允许，本软件不可用于任何商业用途。
您一旦打开使用了该软件，说明您同意了本协议
如果您不同意，请立刻关闭、删除本软件。
本版权协议更新日期：2022年3月23日，协议更新恕不另行通知
若本版权协议与GNU GPL3.0版权协议有冲突，以本版权协议为准

贡献：

对于开源库作者和API所有者，在此表示感谢
本软件使用了以下开源库和API：
you-get，ffmpeg，ffmpeg-python，tqdm，requests，playsound，pillow
pyttsx3，Youdao Translate(China，有道翻译)，Google Translate
Turing Robot(China，图灵机器人)，weather.cn(China，中国天气网)
本软件吉祥物由RUA(免费为我)绘制并已经转让著作权，在此表示感谢
本软件背景音乐是音乐游戏Phigros的谢幕曲，由Phigros项目组版权所有'''
    lmtx=tk.Text(lmcp,height=35,width=90)
    lmtx.insert(tk.INSERT,crtxt)
    lmtx.update()
    lmtx.config(state=tk.DISABLED)
    lmtx.pack()
    lmcp.mainloop()
def mainmake():
    mainroot = tk.Tk()
    mainroot.title("马哥多功能程序-------版本1.2.5")
    mainroot.geometry('1000x673')
    mainroot.resizable(False,False)
    mainroot.protocol("WM_DELETE_WINDOW", callbackClose)

    with open('tmp.ico','wb') as tmp:
        tmp.write(b64decode(icon.Icon().ig))
    mainroot.iconbitmap('tmp.ico')
    remove("tmp.ico")

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
        command=lambda:go_to_chatrobot())

    button_weatherui = tk.Button(mainroot, 
        text='天气查询系统',
        width=50, height=2, 
        command=lambda:go_to_weather())
    button_transui = tk.Button(mainroot, 
        text='翻译机(GUI版)',      
        width=50, height=2, 
        command=lambda:go_to_transgui())
    button_videodown = tk.Button(mainroot, 
        text='**热门功能**80+网站网页视频爬取下载\n(含bilibili/Youtube等)',      
        width=50, height=2,fg="red",
        command=lambda:go_to_videodown())
    button_videochange = tk.Button(mainroot, 
        text='全国/各省疫情查询\n支持数据表格化与疫情可视化地图',      
        width=50, height=2,fg="red",
        command=lambda:createcovidtoplevel())
    button_opengithub = tk.Button(mainroot, 
        text='GitHub开源地址\n使用帮助',      
        width=14, height=2,
        command=lambda:open_new("https://github.com/billma007/multifunction"))
    button_openblog = tk.Button(mainroot, 
        text='作者博客',      
        width=14, height=2,
        command=lambda:open_new("https://billma.top"))
    button_stopmusic = tk.Button(mainroot, 
        text='停止音乐',      
        width=14, height=2,
        command=lambda:musicplay.terminate())
    button_learnmore = tk.Button(mainroot,
        text='了解更多\n如何使用',
        width=24,height=2,
        command=lambda:learnmore())
    button_copyright = tk.Button(mainroot,
        text='版权协议与许可',
        width=24,height=2,
        command=lambda:copyr())
    labelmore = tk.Label(mainroot,text="""Copyright (C) 2022 BillMa007|BillMa007 版权所有""",font=("等线",12))
    labelthank=tk.Label(mainroot,text="感谢您的使用！",fg="red",font=("等线",30))
    labelimg.place(x=400,y=0)
    labelwel.place(x=0,y=20)
    button_chat.place(x=0,y=100)
    button_weatherui.place(x=0,y=170)
    button_transui.place(x=0,y=240)
    button_videodown.place(x=0,y=310)
    button_videochange.place(x=0,y=380)
    button_openblog.place(x=120,y=450)
    button_stopmusic.place(x=240,y=450)
    button_opengithub.place(x=0,y=450)
    button_learnmore.place(x=0,y=520)
    labelmore.place(x=0,y=580)
    button_copyright.place(x=180,y=520)
    labelthank.place(x=50,y=600)
    global kkkkk
    kkkkk=True 
    mainroot.mainloop()
if __name__ == "__main__":
    multiprocessing.freeze_support()
    if (("1.2.5" not in str(max(str(getHtml("https://fastly.jsdelivr.net/gh/billma007/imagesave@latest/multifunctionaltoolsupdatecheck.html")),str(getHtml("https://cdn.jsdelivr.net/gh/billma007/imagesave@latest/multifunctionaltoolsupdatecheck.html")),str(getHtml("https://cdn.jsdelivr.net/gh/billma007/imagesave@latest/update/latest.html")),str(getHtml("https://fastly.jsdelivr.net/gh/billma007/imagesave@latest/update/latest.html"))))) and os.path.exists("cancelupdate.txt")==False and os.path.exists("cancelupdate.txt.txt")==False)==True:
        htmltest.gotoweather()
    global musicplay
    musicplay=multiprocessing.Process(target=playmusic)
    musicplay.start()

    mainmake()
