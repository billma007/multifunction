import multiprocessing
import re
import sys
import threading
import tkinter as tk
from tkinter.filedialog import askdirectory
import tkinter.messagebox as msgbox
from webbrowser import open_new
import you_get 
from pyperclip import paste
 
import os
import base64
import sys
import tkinter



class Download():

    # construct
    def selectPath(self):
        path_=askdirectory()
        self.path.set(path_)
    def write(self, info):
            # info信息即标准输出sys.stdout和sys.stderr接收到的输出信息
            self.t.delete('1.0','end')
            self.t.insert('end', info)	# 在多行文本控件最后一行插入print信息
            self.t.update()	# 更新显示的文本，不加这句插入的信息无法显示
            self.t.see(tkinter.END)	# 始终显示最后一行，不加这句，当文本溢出控件最后一行时，不会自动显示最后一行

    def flush(self):
        pass
    def isatty(self):
        pass
    def __init__(self, width=700, height=330):

        self.w = width
        self.h = height
        self.title = '马哥视频下载GUI1.1'
        self.root = tk.Toplevel()
        self.root.title(self.title)
        self.root.iconbitmap('ico.ico')
        self.url = tk.StringVar()
        self.start = tk.IntVar()
        self.end = tk.IntVar()
        self.path = tk.StringVar()
        self.path.set('D:/')
        # 将其备份
        self.stdoutbak = sys.__stdout__
        self.stderrbak = sys.__stderr__
        # 重定向
        sys.stdout = self
        # define frame
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        frame_3 = tk.Frame(self.root)
        frame_4 = tk.Frame(self.root)
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        # menu1 = tk.Menu(menu, tearoff=0)
        # menu.add_cascade(label='帮助', menu=menu1)
        # menu1.add_command(label='GitHub开源地址', command=lambda: open_new('https://github.com/billma007/videodownloadergui'))
        # menu1.add_command(label="对软件有疑问",command=lambda: open_new('https://github.com/billma007/videodownloadergui/blob/main/xiaobaiQuestions_Chinese.md'))
        # menu1.add_command(label='退出', command=lambda: self.root.quit())

        menu.add_command(label="*粘贴*",command=lambda: self.url.set(paste()))
        menu.add_command(label='GitHub开源地址', command=lambda: open_new('https://github.com/billma007/videodownloadergui'))
        menu.add_command(label='*帮助*', command=lambda: open_new('https://github.com/billma007/videodownloadergui/blob/main/xiaobaiQuestions_Chinese.md'))
        # set frame_1
        label1 = tk.Label(frame_1, text='输入视频链接：')
        entry_url = tk.Entry(frame_1, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)

        # set frame_3
        label2 = tk.Label(frame_2, text='视频输出地址：')
        entry_path = tk.Entry(frame_2, textvariable=self.path, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        
        # set frame_2
        path = tk.StringVar()
        url_path = tk.Button(frame_3, text = "路径选择", font=('楷体', 12), fg='black', width=3, height=-1, command = self.selectPath)
        down = tk.Button(frame_3, text='下载', font=('楷体', 12), fg='black', width=3, height=-1,
                         command=self.video_download)
        
        label_desc = tk.Label(frame_4, fg='red', font=('楷体', 12),
                              text='本项目已在GitHub上开源,遵守GNU通用公共许可证(GPL)')
        label_jnxxhzz = tk.Label(frame_4, fg='red', font=('楷体', 10),
                              text='Copyright (C) 2022 billma007')
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        frame_4.pack()
#        label_img.pack(side=tk.RIGHT)
#        label_img.pack(ipadx=100,ipady=0)
        label1.grid(row=0, column=0)
        entry_url.grid(row=0, column=1)

        label2.grid(row=1, column=0,pady=10)
        entry_path.grid(row=1, column=1,pady=10)	
        
        url_path.grid(row=1,column=0, ipadx=20,padx = 5)
        down.grid(row=1, column=3, ipadx=20)
        label_desc.grid(row=1, column=0)
        label_jnxxhzz.grid(row=2, column=0)
        
        self.t = tkinter.Text(self.root)	# 创建多行文本控件
        self.t.pack()	# 布局在窗体上

    
    def video_download(self):
        url = self.url.get()
        path = self.path.get()
        if re.match(r'^https?:/{2}\w.+$', url):
            if path != '':
                try:
                    msgbox.showwarning(title='警告', message='下载过程中窗口如果出现短暂卡顿说明文件正在下载中！')
#                        self.root.withdraw()
                    sys.argv = ['you-get', '-o', path, url,'--debug']    #sys传递参数执行下载
                    you_get.main()
                except Exception as e:
                    msgbox.showerror(title='警告', message=e)

                msgbox.showinfo(title='成功', message='下载完成！')
            else:
                msgbox.showerror(title='警告', message='输出地址错误！')
        else:
            msgbox.showerror(title='警告', message='视频地址错误！')
    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int((ws / 2) - (self.w / 2))
        y = int((hs / 2) - (self.h / 2))
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

    def event(self):
        self.root.resizable(False, False)
        self.center()

        self.root.mainloop()


def main():
    app = Download()
    app.event()

def videodownloadmain():
    main()
if __name__=="__main__":
    main()