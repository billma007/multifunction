import multiprocessing
import os
import sys
import threading
import webbrowser
from covidworld import covidworld_main
import tkinter as tk
from PIL import ImageTk,Image
from chatmain import cometochat
from weather_tkinter import gotoweather
from translategui import translateguimain
from video import videodownloadmain
from covidcheck import createcovidtoplevel, display_provinces
from webbrowser import open_new
from playsound import playsound,PlaysoundException
import urllib.request
import tkinter.messagebox
from small import SysTrayIcon
import qrcodemake
import gnugpl3allcopyright
import goupibutong
import htmltest
import musicdlgui
def gotosmall(root):
    musicplay.terminate()
    root.destroy()
    a=Smallmake()
    a.mainmake()


def callbackClose():

    destroyask=tkinter.messagebox.askokcancel(title="提示",message="真的要退出吗？")
    if destroyask ==True:
        musicplay.terminate()
        os._exit(0x0)
def playmusic():
    try:
        while True:
            passs=''
            #passs=sys._MEIPASS+'\\'
            playsound(passs+"multimusic.mp3")
    except PlaysoundException or Exception or AttributeError:
        pass
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
def go_to_musicdownload():
    print("go to musicdown...")
    try:
        os.startfile("musicdlgui.exe")
    except:
        import musicdlgui
        threading.Thread(target=musicdlgui.mainstart).start()
def go_to_gpbt():
    print('go to gpbt')
    goupibutong.goupi_main()
def go_to_check():
    print('go to check')
    htmltest.gotoweather()
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
|   原因：Threading不支持mainloop的线程多开
|   multiprocessing只能在__name__=="__main__"进行
|   解决办法：别急，过一会会自动开始的
|   （在此之间不要使用其他功能）
|-3.最小化托盘时不支持右键快捷抵达

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
|-2022年4月8日---1.4.0版本
|   |-1.增加了会员音乐下载
|   |-2.增加了狗屁不通文章生成功能
|   |-3.增加了全球疫情地图功能
|   |-4.为了加快启动速度，取消了更新系统
|   |-5.优化内存，抛弃了pandas库和openpyxl的使用
|   |-6.修复了7个bug
|-2022年3月31日--1.3.0版本
|   |-重大更新：
|   |    |-1.支持最小化托盘
|   |    |-2.新增迷你工具箱，更加快捷
|   |    |-3.支持托盘快捷直达功能
|   |-一般更新：
|   |    |-1.支持回车键快捷触发指令
|   |    |-2.修复了部分按钮无法触发的bug
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
you-get，tqdm，requests，playsound，pillow
pyttsx3，Youdao Translate(China，有道翻译)，Google Translate
Turing Robot(China，图灵机器人)，weather.cn(China，中国天气网)
本软件吉祥物由RUA(免费为我)绘制并已经转让著作权，在此表示感谢
本软件背景音乐是音乐游戏Phigros的谢幕曲，由Phigros项目组版权所有

以下是GNU GPL Version3.0的完整版本：
'''+gnugpl3allcopyright.gnu_gpl3allcopyrigt
    lmtx=tk.Text(lmcp,height=35,width=90)
    lmtx.insert(tk.INSERT,crtxt)
    lmtx.update()
    lmtx.config(state=tk.DISABLED)
    lmtx.pack()
    lmcp.mainloop()

class Smallmake:
    def move(self, event):
        """窗口移动事件"""
        new_x = (event.x - self.x) + self.mainroot.winfo_x() - 30
        new_y = (event.y - self.y) + self.mainroot.winfo_y()
        s = f"{self.window_size}+{new_x}+{new_y}"
        self.mainroot.geometry(s)
    def __init__(self):
        self.x, self.y = 0, 0
        self.SysTrayIcon  = None
        self.mainroot = tk.Tk()
        self.mainroot.wm_attributes('-topmost',1)
        self.mainroot.attributes("-alpha", 0.7)
        self.mainroot.bind("<B1-Motion>", self.move)
        self.mainroot.title("迷你工具栏")
        self.window_size = '83x280'
        self.mainroot.geometry(self.window_size)
        self.mainroot.resizable(False,False)
        self.mainroot.protocol("WM_DELETE_WINDOW", callbackClose)
        self.mainroot.iconbitmap('ico.ico')
        #-----------------------button-----------------#
        self.label_gjl=tk.Label(self.mainroot,
            text="工具栏",font=("等线",13))
        self.button_chat = tk.Button(self.mainroot, 
            text='AI聊天',      # 显示在按钮上的文字
            width=10, height=1, 
            command=lambda:go_to_chatrobot())
        self.button_weatherui = tk.Button(self.mainroot, 
            text='天气查询系统',
            width=10, height=1, 
            command=lambda:go_to_weather())
        self.button_transui = tk.Button(self.mainroot, 
            text='翻译系统',      
            width=10, height=1, 
            command=lambda:go_to_transgui())
        self.button_videodown = tk.Button(self.mainroot, 
            text='下载视频图片',      
            width=10, height=1,fg="red",
            command=lambda:go_to_videodown())
        self.button_videochange = tk.Button(self.mainroot, 
            text='疫情查询',      
            width=10, height=1,fg="red",
            command=lambda:createcovidtoplevel())
        self.button_opengithub = tk.Button(self.mainroot, 
            text='最小化托盘',      
            width=10, height=1,
            command=lambda: self.Hidden_window())
        self.button_openmusic = tk.Button(self.mainroot, 
            text='音乐下载',      
            width=10, height=1,
            command=lambda: go_to_musicdownload())
        self.button_tran = tk.Button(self.mainroot, 
            text='传输文件',      
            width=10, height=1,
            command=lambda: qrcodemake.makemain())
        self.button_opengpbt = tk.Button(self.mainroot, 
            text='狗屁不通',      
            width=10, height=1,
            command=lambda: go_to_gpbt())
        self.label_gjl.pack()
        self.button_chat.pack()
        self.button_weatherui.pack()
        self.button_transui.pack()
        self.button_videodown.pack()
        self.button_videochange.pack()
        self.button_opengithub.pack()
        self.button_openmusic.pack()
        self.button_opengpbt.pack()
    def show_msg(self, title = '标题', msg = '内容', time = 500):
        self.SysTrayIcon.refresh(title = title, msg = msg, time = time)
    def Hidden_window(self, hover_text = "马哥多功能工具"):
        _icon='ico.ico'
        '''隐藏窗口至托盘区，调用SysTrayIcon的重要函数'''
        #托盘图标右键菜单, 格式: ('name', None, callback),下面也是二级菜单的例子
        #24行有自动添加‘退出’，不需要的可删除
        menu_options = (('聊天机器人', None, go_to_chatrobot),  
                        ('翻译机', None,go_to_transgui),
                        ('视频下载',None,go_to_videodown),
                        ('疫情查询',None,go_to_covid),
                        ('天气查询',None,go_to_weather),
                        ('狗屁不通文章生成',None,go_to_gpbt),
                        ('全网音乐下载',None,go_to_musicdownload),
                        ('传输文件',None,qrcodemake.makemain))
        self.mainroot.withdraw()   #隐藏tk窗口
        if not self.SysTrayIcon: self.SysTrayIcon = SysTrayIcon(
                                        _icon,               #图标
                                        hover_text,         #光标停留显示文字
                                        menu_options,       #右键菜单
                                        on_quit = lambda:os._exit(0x0),   #退出调用
                                        tk_window = self.mainroot, #Tk窗口
                                        )
        self.SysTrayIcon.activation()
    def mainmake(self):
        self.mainroot.bind("<Unmap>", lambda event: self.Hidden_window() if self.mainroot.state() =='iconic' else False) #窗口最小化判断，可以说是调用最重要的一步
        self.mainroot.mainloop()


class Mainmake:
    def __init__(self):
        try:
            self.passs=sys._MEIPASS+'\\'
        except:
            self.passs=''
        self.SysTrayIcon  = None  # 判断是否打开系统托盘图标
        self.mainroot = tk.Tk()
        self.mainroot.title("马哥多功能程序-------版本1.4.0")
        self.mainroot.geometry('1000x673')
        self.mainroot.resizable(False,False)
        self.mainroot.protocol("WM_DELETE_WINDOW", callbackClose)
        self.mainroot.iconbitmap('ico.ico')
        #---------------图片------------------#
        self.pil_image = Image.open(self.passs+"videodownloadimage.jpg")

        # 将pil格式的图片转换为tk格式的image
        self.tk_image = ImageTk.PhotoImage(self.pil_image)
        # 创建个label组件, imageroot作为父节点
        self.labelimg = tk.Label(self.mainroot, image=self.tk_image, bg='white')
        # 设置一些padding
        #-----------------------label------------------#
        self.labelwel = tk.Label(self.mainroot,text="欢迎使用马哥多功能工具！",font=("等线",24))
        #-----------------------button-----------------#

        self.button_chat = tk.Button(self.mainroot, 
            text='马哥聊天机器人',      # 显示在按钮上的文字
            width=50, height=2, 
            command=lambda:go_to_chatrobot())

        self.button_weatherui = tk.Button(self.mainroot, 
            text='天气查询系统',
            width=50, height=2, 
            command=lambda:go_to_weather())
        self.button_transui = tk.Button(self.mainroot, 
            text='翻译机(GUI版)',      
            width=50, height=2, 
            command=lambda:go_to_transgui())
        self.button_videodown = tk.Button(self.mainroot, 
            text='**热门功能**80+网站网页视频爬取下载\n(含bilibili/Youtube等)',      
            width=50, height=2,fg="red",
            command=lambda:go_to_videodown())
        self.button_videochange = tk.Button(self.mainroot, 
            text='全国/各省疫情查询',      
            width=16, height=2,fg="red",
            command=lambda:createcovidtoplevel())
        self.button_covidchina = tk.Button(self.mainroot, 
            text='全国疫情地图可视化',      
            width=16, height=2,fg="red",
            command=lambda:display_provinces())
        self.button_covidworld = tk.Button(self.mainroot, 
            text='全球疫情地图可视化',      
            width=16, height=2,fg="red",
            command=lambda:covidworld_main())
        self.button_qrcodemake = tk.Button(self.mainroot,
            text='跨设备高速文件传输',
            width=50, height=2,fg='red',
            command=lambda:qrcodemake.makemain())
        self.button_musicdown = tk.Button(self.mainroot,
            text='全网音乐下载\n该功能加载较慢，切勿重复点击',
            width=50,height=2,fg='red',
            command=lambda:go_to_musicdownload())
        self.button_gpbt = tk.Button(self.mainroot,
            text='狗屁不通文章生成',
            width=50,height=2,fg='red',
            command=lambda:go_to_gpbt())
        self.button_opengithub = tk.Button(self.mainroot, 
            text='GitHub开源地址',      
            width=14, height=1,
            command=lambda:open_new("https://github.com/billma007/multifunction"))
        self.button_openblog = tk.Button(self.mainroot, 
            text='作者博客',      
            width=14, height=1,
            command=lambda:open_new("https://billma.top"))
        self.button_stopmusic = tk.Button(self.mainroot, 
            text='停止音乐',      
            width=14, height=1,
            command=lambda:musicplay.terminate())
        self.button_learnmore = tk.Button(self.mainroot,
            text='了解更多',
            width=14,height=1,
            command=lambda:learnmore())
        self.button_copyright = tk.Button(self.mainroot,
            text='版权协议与许可',
            width=14,height=1,
            command=lambda:copyr())
        self.button_small = tk.Button(self.mainroot,
            text='smart精简版',
            width=14,height=1,
            command=lambda:gotosmall(self.mainroot))
        self.checkupd     = tk.Button(self.mainroot,
            text='检查更新',
            width=14,height=1,
            command=lambda:go_to_check())
        self.gotohelp     = tk.Button(self.mainroot,
            text='查看帮助（中文）',
            width=14,height=1,
            command=lambda:webbrowser.open("https://github.com/billma007/multifunction/blob/main/README-Chinese.md"))
        self.gotodoc     = tk.Button(self.mainroot,
            text='查看文档(完整)',
            width=14,height=1,
            command=lambda:webbrowser.open("https://multifunction.readthedocs.io"))
        self.labelmore = tk.Label(self.mainroot,text="""Copyright (C) 2022 BillMa007|BillMa007 版权所有""",font=("等线",  12))
        self.labelthank=tk.Label(self.mainroot,text="感谢您的使用！",fg="red",font=("等线",30))
        self.labelimg.place(x=400,y=0)
        self.labelwel.place(x=0,y=10)
        self.button_chat.place(x=0,y=66)
        self.button_weatherui.place(x=0,y=115)
        self.button_transui.place(x=0,y=164)
        self.button_videodown.place(x=0,y=213)

        self.button_videochange.place(x=0,y=262)
        self.button_covidchina.place(x=120,y=262)
        self.button_covidworld.place(x=240,y=262)

        self.button_qrcodemake.place(x=0,y=311)
        self.button_musicdown.place(x=0,y=360)
        self.button_gpbt.place(x=0,y=408)
        
        self.button_openblog.place(x=120,y=455)
        self.button_stopmusic.place(x=240,y=455)
        self.button_opengithub.place(x=0,y=455)

        self.checkupd.place(x=0,y=488 )
        self.gotohelp.place(x=120,y=488)
        self.gotodoc.place(x=240,y=488)

        self.button_learnmore.place(x=0,y=518)
        self.labelmore.place(x=0,y=580)
        self.button_copyright.place(x=120,y=518)
        self.button_small.place(x=240,y=518)
        self.labelthank.place(x=50,y=600)
    def show_msg(self, title = '标题', msg = '内容', time = 500):
        self.SysTrayIcon.refresh(title = title, msg = msg, time = time)
    def Hidden_window(self, hover_text = "马哥多功能工具"):
        '''隐藏窗口至托盘区，调用SysTrayIcon的重要函数'''
        _icon='ico.ico'
        #托盘图标右键菜单, 格式: ('name', None, callback),下面也是二级菜单的例子
        #24行有自动添加‘退出’，不需要的可删除
        menu_options = (('聊天机器人', None, go_to_chatrobot),  
                        ('翻译机', None,go_to_transgui),
                        ('视频下载',None,go_to_videodown),
                        ('疫情查询',None,go_to_covid),
                        ('天气查询',None,go_to_weather),
                        ('狗屁不通文章生成',None,go_to_gpbt),
                        ('全网音乐下载',None,go_to_musicdownload),
                        ('传输文件',None,qrcodemake.makemain))

        self.mainroot.withdraw()   #隐藏tk窗口
        if not self.SysTrayIcon: self.SysTrayIcon = SysTrayIcon(
                                        _icon,               #图标
                                        hover_text,         #光标停留显示文字
                                        menu_options,       #右键菜单
                                        on_quit = lambda:os._exit(0x0),   #退出调用
                                        tk_window = self.mainroot, #Tk窗口
                                        )
        self.SysTrayIcon.activation()
    def mainmake(self):
        self.mainroot.bind("<Unmap>", lambda event: self.Hidden_window() if self.mainroot.state() =='iconic' else False) #窗口最小化判断，可以说是调用最重要的一步
        self.mainroot.mainloop()
if __name__ == "__main__":
    multiprocessing.freeze_support()
    global musicplay
    musicplay=multiprocessing.Process(target=playmusic)
    musicplay.start()
    aaaaaaaa=Mainmake()
    aaaaaaaa.mainmake()
