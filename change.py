from base64 import b64decode
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as msgbox
from  webbrowser import open_new
import ffmpeg
import icon
from icon import Icon
def returntomain(self):
    self.destroy()
    import gobackmain
    gobackmain.gobackmain()
class CHANGE:
    # construct
    def selectPath(changeroot):
        path_=askopenfilename()
        changeroot.path.set(path_)
    

    def __init__(changeroot, width=550, height=170):
        global hflipset
        global vflipset

        changeroot.w = width
        changeroot.h = height
        changeroot.title = '马哥视频转码GUI1.1'
        changeroot.root = tk.Tk(className=changeroot.title)
        try:
            with open('tmp.ico','wb') as tmp:
                tmp.write(b64decode(icon.Icon().ig))
            changeroot.iconbitmap('tmp.ico')
            os.remove("tmp.ico")
        except Exception:
            print("logo load error")
        changeroot.url = tk.StringVar()
        changeroot.start = tk.IntVar()
        changeroot.end = tk.IntVar()
        changeroot.path = tk.StringVar()
        hflipset = tk.IntVar()
        vflipset = tk.IntVar()
        changeroot.path.set('D:/example.mp4')
        menu = tk.Menu(changeroot.root)
        changeroot.root.config(menu=menu)
        menu1 = tk.Menu(menu, tearoff=0)
        menu2 = tk.Menu(menu,tearoff=0)
        menu.add_cascade(label='下载ffmpeg', menu=menu1)
        menu1.add_command(label="GitHub官方下载(中国大陆用户可能较慢)",command=lambda:open_new("https://github.com/billma007/videodownloadergui/releases/download/download/ffmpeg.exe"))
        menu1.add_command(label="蓝奏云下载(推荐，密码ffmpeg)",command=lambda:open_new("https://wwp.lanzouq.com/i1r7701bvk5e"))
        menu1.add_command(label="GitHub中国镜像网站下载1(很不稳定,可能会被误报读)",command=lambda:open_new("https://ghproxy.com/https://github.com/billma007/videodownloadergui/releases/download/download/ffmpeg.exe"))
        menu1.add_command(label="GitHub中国镜像网站下载2(很不稳定,可能会被误报读)",command=lambda:open_new("https://github.91chi.fun/https://github.com//billma007/videodownloadergui/releases/download/download/ffmpeg.exe"))
        menu.add_command(label="前往GitHub开源地址",command=lambda:open_new("https://github.com/billma007/videodownloadergui/"))
        menu.add_command(label="查看如何使用以及范例",command=lambda:open_new("https://github.com/billma007/videodownloadergui/README_change-cn.md"))
        menu.add_cascade(label='更多功能',menu=menu2)
        menu2.add_checkbutton(label="水平翻转(视频+图像)",onvalue=1,offvalue=0,variable=hflipset)
        menu2.add_checkbutton(label="垂直翻转(视频+图像)",onvalue=1,offvalue=0,variable=vflipset)

        menu.add_command(label="返回主菜单",command=lambda:returntomain(changeroot.root))
        # define frame
        frame_1 = tk.Frame(changeroot.root)
        frame_2 = tk.Frame(changeroot.root)
        frame_3 = tk.Frame(changeroot.root)
        frame_4 = tk.Frame(changeroot.root)

        # set frame_1
        label1 = tk.Label(frame_1, text='视频输出名称(带上后缀)')
        entry_url = tk.Entry(frame_1, textvariable=changeroot.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)

        # set frame_3
        label2 = tk.Label(frame_2, text='输入视频所在路径：')
        entry_path = tk.Entry(frame_2, textvariable=changeroot.path, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        
        # set frame_2
        path = tk.StringVar()
        url_path = tk.Button(frame_3, text = "选择文件", font=('楷体', 12), fg='black', width=3, height=-1, command = changeroot.selectPath)
        down = tk.Button(frame_3, text='点击转码', font=('楷体', 12), fg='black', width=3, height=-1,
                         command=changeroot.change)
        
        label_desc = tk.Label(frame_4, fg='red', font=('楷体', 12),
                              text='本项目已在GitHub上开源,遵守GNU通用公共许可证(GPL)')
        label_jnxxhzz = tk.Label(frame_4, fg='red', font=('楷体', 10),
                              text='Copyright (C) 2022 billma007')
        ffmpeg_say = tk.Label(frame_4, fg='red', font=('楷体', 8),
                              text='开源项目声明：本软件完全开源，使用FFmpeg进行驱动，使用GNU GPL为许可证，不涉及任何商业行为！！')


        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        frame_4.pack()
        label1.grid(row=0, column=0)
        entry_url.grid(row=0, column=1)
 
        label2.grid(row=1, column=0,pady=10)
        entry_path.grid(row=1, column=1,pady=10)	
        
        url_path.grid(row=1,column=0, ipadx=20,padx = 5)
        down.grid(row=1, column=3, ipadx=20)
        label_desc.grid(row=1, column=0)
        label_jnxxhzz.grid(row=2, column=0)
        ffmpeg_say.grid(row=3,column=0)
    
    def change(changeroot):
        url = changeroot.url.get()
        path = changeroot.path.get()
        if not os.path.isfile(path):
            msgbox.showerror(title='警告', message='文件不存在！')
            changeroot.root.wm_deiconify()
        elif not os.path.isfile('ffmpeg.exe'):
            msgbox.showerror(title='警告', message='请注意:ffmpeg是本软件转码的必备依赖库，如果没有则不能转码，但是不影响下载功能。目前未查找到目录下有ffmpeg,请确保本文件同一目录下包含ffmpeg.exe，如果没有请回到上一界面进行下载。下载后，会自动安装。')
            changeroot.root.wm_deiconify()
        elif '.' not in url:
            msgbox.showerror(title='警告', message='请在输出文件名末尾填上你要输入文件格式的后缀名(例如output.mp4)!!!!!!')
            changeroot.root.wm_deiconify()
        else:
            msgbox.showwarning(title='警告', message='转码过程中窗口如果出现短暂卡顿说明文件正在转码中！技术原因，转码很慢，大约每分钟视频需要20-50s转码，请耐心等待！')
            try:
                changeroot.root.withdraw()
                os.system("attrib ffmpeg.exe +h +s")
                # stream = ffmpeg.input(path)
                # if settingsvideo.get_value("hflip") == True:
                #     stream = ffmpeg.hflip(stream)
                # if settingsvideo.get_value("vflip") == True:
                #     stream = ffmpeg.vflip(stream)
                # if int(settingsvideo.get_value("fps")) != -999:
                #     stream = ffmpeg.output(stream,r=int(settingsvideo.get_value("fps")))
                # if int(settingsvideo.get_value("bit")) != -999:
                #     stream = ffmpeg.output(stream,b=int(settingsvideo.get_value("bit")))
                # stream = ffmpeg.output(stream,url)
                # ffmpeg.run(stream)
                # output_list=[]
                # if settingsvideo.get_value("hflip") == True:
                #     output_list.append(["-vf","hflip"])
                # if settingsvideo.get_value("vflip") == True:
                #     output_list.append(["-vf","vflip"])
                # if int(settingsvideo.get_value("fs"))  != -999:
                #     output_list.append(["-fs",int(settingsvideo.get_value("fs"))])
                # else:
                #     if int(settingsvideo.get_value("fps")) != -999:
                #         output_list.append(["-r",int(settingsvideo.get_value("fps"))])
                #     if int(settingsvideo.get_value("bit")) != -999:
                #         output_list.append(["-b:v",int(settingsvideo.get_value("bit"))])
                #if int(settingsvideo.get_value("crop")) != -999:
                #    output_list.append(["-vf crop",str(settingsvideo.get_value("crop"))])
                # output_str = ""
                # for i in output_list:
                #     output_str+=(i+":")
                # stream = ffmpy.FFmpeg(
                #     inputs={path:None},
                #     outputs={url:None}
                # )
                # stream.cmd()
                print("hflipset=",hflipset.get())
                print("vflipset=",vflipset.get())
                changeroot.root.withdraw()
                stream = ffmpeg.input(path)
                if hflipset.get() == True:
                    stream = ffmpeg.hflip(stream)
                if vflipset.get() == True:
                    stream = ffmpeg.vflip(stream)
                stream = ffmpeg.output(stream,url)
                ffmpeg.run(stream)
                msgbox.showinfo(title='成功', message='转码完成！')
                changeroot.root.wm_deiconify()
            except Exception as e:
                msgbox.showerror(title='警告', message=e)
                changeroot.root.wm_deiconify()
    def center(changeroot):
        ws = changeroot.root.winfo_screenwidth()
        hs = changeroot.root.winfo_screenheight()
        x = int((ws / 2) - (changeroot.w / 2))
        y = int((hs / 2) - (changeroot.h / 2))
        changeroot.root.geometry('{}x{}+{}+{}'.format(changeroot.w, changeroot.h, x, y))
 
    def event(changeroot):
        changeroot.root.resizable(False, False)
        changeroot.center()
        changeroot.root.mainloop()
 
 
def changemain():
    app_change = CHANGE()
    app_change.event()
