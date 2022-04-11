#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
import pyperclip
import random,readJSON
import tkinter as tk
data = readJSON.readjson()
whospeak = data["famous"] # a 代表前面垫话，b代表后面垫话
beforeit = data["before"] # 在名人名言前面弄点废话
afterit = data['after']  # 在名人名言后面弄点废话
feihua = data['bosh'] # 代表文章主要废话来源
xx = "上海"

repeatit = 2 # 重复度
resultit=''
def dfs(dfs):
    global repeatit
    hhh = list(dfs) * repeatit
    while True:
        random.shuffle(hhh)
        for data in hhh:
            yield data

nextfeihua = dfs(feihua)#下一句废话
scmrmy = dfs(whospeak)

def comeon():
    global scmrmy#名人名言
    xx = next(scmrmy)
    xx = xx.replace(  "a",random.choice(beforeit) )
    xx = xx.replace(  "b",random.choice(afterit) )
    return xx

def nextpara():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx

def goupi_main():
    m=tk.Toplevel()
    m.iconbitmap('ico.ico')
    maintheme=tk.StringVar()
    maintheme.set('上海')
    RepeatLevel=tk.IntVar()
    RepeatLevel.set(2)
    tk.Label(m,text='欢迎使用狗屁不通文章生成器！\n请输入狗屁不通文章主题：').pack()
    tk.Entry(m,textvariable=maintheme).pack()
    tk.Label(m,text='请输入重复度，建议为2').pack()
    tk.Entry(m,textvariable=RepeatLevel).pack()
    tk.Button(m,text='开始输出',command=lambda:start_main(xx=maintheme.get(),rep=RepeatLevel.get())).pack()
    tk.Button(m,text='复制到剪贴板',command=lambda:pyperclip.copy(resultit)).pack()
    global putoutgp
    putoutgp=tk.Text(m,font=('等线',9))
    putoutgp.pack()
    tk.Label(m,text='纯属娱乐！！！本人不对输出内容负责，请勿违反道德和法律，\n制作者不对输出内容负任何责任！！',fg='red').pack()
    m.mainloop()

def start_main(xx='上海',rep=2):
    for x in xx:
        tmp = str()
        while ( len(tmp) < 6000 ) :
            branch = random.randint(0,100)
            if branch < 5:
                tmp += nextpara()
            elif branch < 20 :
                tmp += comeon()
            else:
                tmp += next(nextfeihua)
        tmp = tmp.replace("x",xx)
        global resultit
        resultit=tmp
        print(tmp)
        putoutgp.delete('1.0','end')
        putoutgp.insert(tk.INSERT,tmp)


if __name__=="__main__":
    goupi_main()