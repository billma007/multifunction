import os
import tkinter as tk
import base64
import icon
import webbrowser
import query


class Weather:
    def __init__(self):
        self.title = '马哥天气查询'
        self.root = tk.Toplevel()
        self.root.title(self.title)
        with open('tmp.ico','wb') as tmp:
            tmp.write(base64.b64decode(icon.Icon().ig))
        self.root.iconbitmap('tmp.ico')
        os.remove("tmp.ico")
        self.a = tk.StringVar()
        self.openfinal = False
        self.root.resizable(False, False)
        self.data=""
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        menu.add_command(label='GitHub开源地址', command=lambda:webbrowser.open_new("https://github.com/billma007/weatherGUI2"))
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        frame_3 = tk.Frame(self.root)
        frame_4 = tk.Frame(self.root)
        # set frame_1
        label1 = tk.Label(frame_1, text='查询城市：')
        self.entry_url = tk.Entry(frame_1, textvariable=self.a, highlightcolor='Fuchsia', highlightthickness=1, width=35)

        # set frame_3
        label2 = tk.Label(frame_2, text='天气：')
        self.entry_path = tk.Text(frame_2,highlightcolor='Fuchsia', highlightthickness=1, width=35)
        
        # set frame_2

        down = tk.Button(frame_3, text='点击查询', font=('楷体', 12), fg='black', width=3, height=-1,
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
        
        down.grid(row=1, column=3, ipadx=20)
        label_desc.grid(row=1, column=0)
        label_jnxxhzz.grid(row=2, column=0)
    def write(self):
        self.entry_path.delete('1.0','end')
        self.entry_path.insert('end', self.data)
        self.entry_path.update()	# 更新显示的文本，不加这句插入的信息无法显示

    def robot_main(self):
        try:

            self.table = query.read_code()
            code = query.query_code(self.table, self.a.get())
            self.data=query.query_weather(code)
            print(123)
            self.write()

        except Exception as eeee:
            print(eeee)
            self.data="请输入正确的城市/区域名称"
            self.write()
    def cometohere(self):
        self.root.mainloop()
def gotoweather():
    query.TxtCreate()
    asd=Weather()
    asd.cometohere()
if __name__ == "__main__":
    gotoweather()