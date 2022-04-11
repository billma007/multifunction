import base64
import sys
import tkinter as tk
import webbrowser
from requests import get
import os
# 注意：pyttsx3一定要是2.72版本，高于2.72版本一定会出错！
import pyttsx3 # 语音
import time
# speaking_open:判断用户是否打开了语音输出功能
# speaking_open=False
# # 判断settings.txt是否存在
# def setting_if_exist():
#     filename="settings.txt"
#     if not os.path.exists(filename):
#         return False
#     else :
#         return True
# writingdata函数用法：
# 无入参
# 无返回值
# 导入settings.txt中用户保存的speaking_open数据，并在settings.txt没有数据的时候进行数据初始化
# def writingdata():
#     global speaking_open
#     if setting_if_exist():
#         with open("settings.txt","r",encoding="utf-8") as settings_read:
#             s=settings_read.read()
#             settings_read.close()
#         if s=="SPEAKING=TRUE":
#             speaking_open=True
#             return
#         elif s=="SPEAKING=FALSE":
#             speaking_open=False
#             return
#         else :
#             with open("settings.txt","w",encoding="utf-8") as settings:
#                 s_input=input("数据文件读取出现错误，请输入你是否要开启语音输入？y/n,非法输入则为n")
#                 if s_input in ['y','yes','是','True','true','Yes']:
#                     settings.write("SPEAKING=TRUE")
#                     speaking_open=True
#                     settings.close()
#                     return
#                 else :
#                     settings.write("SPEAKING=FALSE")
#                     speaking_open=False
#                     settings.close()
#                     return
#     else:
#         with open("settings.txt","w",encoding="utf-8") as settings:
#             s_input=input("首次使用该软件，请输入你是否要开启语音输入？y/n,非法输入则为n")
#             if s_input in ['y','yes','是','True','true','Yes']:
#                 settings.write("SPEAKING=TRUE")
#                 speaking_open=True
#                 settings.close()
#                 return
#             else :
#                 settings.write("SPEAKING=FALSE")
#                 speaking_open=False
#                 settings.close()
#                 return
# # 在用户输入-c即主动要求修改语音输出配置时进行修改
# def changedata():
#         with open("settings.txt","w",encoding="utf-8") as settings:
#             s_input=input("请输入你是否要开启语音输入？y/n,非法输入则为n：")
#             if s_input in ['y','yes','是','True','true','Yes']:
#                 settings.write("SPEAKING=TRUE")
#                 speaking_open=True
#                 settings.close()

#                 return
#             else :
#                 settings.write("SPEAKING=FALSE")
#                 speaking_open=False
#                 settings.close()
#                 return
class chatmainclass:
    def openclose(self):
        if self.openfinal==True:
            self.openfinal=False
        else:
            self.openfinal=True
    def apimake(self):
        self.write()
        self.data='''本部分采用GNU GPL2.0 LICENSE
软件架构由Billma007版权所有
人工智能聊天API所有者为图灵机器人
在此表示感谢。'''

    def __init__(self):
        self.title = '马哥聊天机器人GUI1.1'
        self.root = tk.Toplevel()
        self.root.title(self.title) 

        self.a = tk.StringVar()
        self.openfinal = False
        self.root.resizable(False, False)
        self.data=""
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        menu.add_command(label='GitHub开源地址', command=lambda:webbrowser.open_new('https://github.com/billma007/mgchatrobot2'))
        menu.add_command(label="API",command=self.apimake)
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        frame_3 = tk.Frame(self.root)
        frame_4 = tk.Frame(self.root)
        # set frame_1
        label1 = tk.Label(frame_1, text='您的话：')
        self.entry_url = tk.Entry(frame_1, textvariable=self.a, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        self.entry_url.bind("<Return>", func=self.gotorobotmain) 
        # set frame_3
        label2 = tk.Label(frame_2, text='回答：')
        self.entry_path = tk.Text(frame_2,highlightcolor='Fuchsia', highlightthickness=1, width=35)
        
        # set frame_2
        url_path = tk.Button(frame_3, text = "音频开关", font=('楷体', 12), fg='black', width=3, height=-1, command =self.openclose)
        down = tk.Button(frame_3, text='发送', font=('楷体', 12), fg='black', width=3, height=-1,
                         command=self.robot_main)
        
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
        self.entry_url.grid(row=0, column=1)

        label2.grid(row=1, column=0,pady=10)
        self.entry_path.grid(row=1, column=1,pady=10)	
        
        url_path.grid(row=1,column=0, ipadx=20,padx = 5)
        down.grid(row=1, column=3, ipadx=20)
        label_desc.grid(row=1, column=0)
        label_jnxxhzz.grid(row=2, column=0)
    def write(self,info):
        # info信息即标准输出sys.stdout和sys.stderr接收到的输出信息
        self.entry_path.insert('end', info)	# 在多行文本控件最后一行插入print信息
        self.entry_path.update()	# 更新显示的文本，不加这句插入的信息无法显示
        self.entry_path.see(tk.END)	# 始终显示最后一行，不加这句，当文本溢出控件最后一行时，不会自动显示最后一行
    def gotorobotmain(self,event):
        self.robot_main()
    def robot_main(self):
        try:
            self.write(str('\n您 '+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+":\n"+self.a.get()))
            url='https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s'%self.a.get()
            te=get(url).json()
            self.data=te['data']['info']['text']
            if "马哥" in self.a.get() or "马泊宁" in self.a.get() or "马导" in self.a.get():
                self.data="马哥是我主人~"
            if "小思" in self.data:
                self.data=self.data.replace("小思","马哥聊天机器人")
            self.write(str('\n回答 '+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+":\n"+self.data))
            if self.openfinal ==True:
                self.speak=pyttsx3.init()
                self.speak.say(self.data)
                self.speak.runAndWait()
        except Exception as eeee:
            pass
    def cometohere(self):
        self.root.mainloop()

def cometochat():
    aaaaa=chatmainclass()
    aaaaa.cometohere()

if __name__=="__main__":
    cometochat()