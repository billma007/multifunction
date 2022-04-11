# -*- coding:utf-8 -*-

import requests
from requests.exceptions import RequestException
import tkinter as tk
import webbrowser
import pyttsx3
import pyperclip
global settings
# settings是设置pyttsx3的全局变量
settings=False
# 将输出内容继承为全局变量来粘贴到剪贴板
global paste

paste=""
class Translate():
    def gotomaain(self,event):
        self.fanyi()
    def __init__(self):
        self.window = tk.Toplevel()  #创建window窗口
        self.window.title("马哥翻译器GUI1.1")  # 定义窗口名称
        self.window.resizable(0,0)  # 禁止调整窗口大小
        self.input = tk.Entry(self.window, width=80)  # 创建一个输入框,并设置尺寸
        self.info = tk.Text(self.window, height=18)   # 创建一个文本展示框，并设置尺寸
        # 添加一个按钮，用于触发翻译功能
        self.t_button = tk.Button(self.window, text='翻译', relief=tk.RAISED, width=8, height=1, command=self.fanyi)
        # 添加一个按钮，用于触发清空输入框功能
        self.c_button1 = tk.Button(self.window, text='清空输入', relief=tk.RAISED, width=8, height=1, command=self.cle_e)
        # 添加一个按钮，用于触发清空输出框功能
        self.c_button2 = tk.Button(self.window, text='清空输出', relief=tk.RAISED,width=8, height=1, command=self.cle)
        # 添加一个按钮，用于打开GitHub仓库
        self.c_button3 = tk.Button(self.window, text='本代码开源，点击前往GitHub了解更多',relief=tk.RAISED,width=24, height=1, command=self.GoToGitHub)
        # 添加一个按钮用于将内容复制到剪贴板
        self.c_button5 = tk.Button(self.window, text='将结果复制到剪贴板',relief=tk.RAISED,width=16, height=1, command=self.copyit)
        self.input.bind("<Return>", self.gotomaain)
        # 添加一张图标
        # self.image_file = tk.PhotoImage(file='py128.png')
        # self.label_image = tk.Label(self.window, image=self.image_file)

    def gui_arrang(self):
        """完成页面元素布局，设置各部件的位置"""
        self.input.grid(row=0,sticky="W",ipadx=0)
        self.info.grid(row=1)
        self.t_button.grid(row=0,column=1,ipadx=0)
        self.c_button1.grid(row=0, column=2, ipadx=0)
        self.c_button2.grid(row=0,column=3,ipadx=0)
        self.c_button3.grid(row=1,column=1,ipadx=0)
        self.c_button5.grid(row=3,column=1,ipadx=10)
        # self.label_image.grid(row=1, column=1,columnspan=3)

    def fanyi(self):
        """定义一个函数，完成翻译功能"""
        original_str = self.input.get()  # 定义一个变量，用来接收输入框输入的值
        data = {
            'doctype': 'json',
            'type': 'AUTO',
            'i': original_str  # 将输入框输入的值，赋给接口参数
        }
        url = "http://fanyi.youdao.com/translate"
        try:
            r = requests.get(url, params=data)
            if r.status_code == 200:
                result = r.json()
                translate_result = result['translateResult'][0][0]["tgt"]
                global paste
                if settings==True:
                    pt = pyttsx3.init()
                    pt.say(translate_result)
                    pt.runAndWait()
                    global paste
                    paste=translate_result
                self.info.delete(1.0, "end")  # 输出翻译内容前，先清空输出框的内容
                self.info.insert('end',translate_result)  # 将翻译结果添加到输出框中
        except RequestException:
            self.info.delete(1.0, "end")
            self.info.insert('end', "发生错误")
    def cle(self):
        """定义一个函数，用于清空输出框的内容"""
        self.info.delete(1.0,"end")  # 从第一行清除到最后一行

    def cle_e(self):
        """定义一个函数，用于清空输入框的内容"""
        self.input.delete(0,"end")
    
    def GoToGitHub(self):
        webbrowser.open_new("https://github.com/billma007/pythontranslator/")
    
    def openpyttsx3(self):
        global settings
        settings=True
        print(settings)
    def closepyttsx3(self):
        global settings
        settings=False
        print(settings)

    def copyit(self):
        print(paste)
        pyperclip.copy(paste)# 复制到剪贴板
def translateguimain():
    t = Translate()
    t.gui_arrang()
    tk.mainloop()
if __name__=="__main__":
    translateguimain()