from requests import get
import os
# 注意：pyttsx3一定要是2.72版本，高于2.72版本一定会出错！
import pyttsx3 # 语音
from webbrowser import open_new

# speaking_open:判断用户是否打开了语音输出功能
speaking_open=False
# 判断settings.txt是否存在
def setting_if_exist():
    filename="settings.txt"
    if not os.path.exists(filename):
        return False
    else :
        return True
# writingdata函数用法：
# 无入参
# 无返回值
# 导入settings.txt中用户保存的speaking_open数据，并在settings.txt没有数据的时候进行数据初始化
def writingdata():
    global speaking_open
    if setting_if_exist():
        with open("settings.txt","r",encoding="utf-8") as settings_read:
            s=settings_read.read()
            settings_read.close()
        if s=="SPEAKING=TRUE":
            speaking_open=True
            return
        elif s=="SPEAKING=FALSE":
            speaking_open=False
            return
        else :
            with open("settings.txt","w",encoding="utf-8") as settings:
                s_input=input("数据文件读取出现错误，请输入你是否要开启语音输入？y/n,非法输入则为n")
                if s_input in ['y','yes','是','True','true','Yes']:
                    settings.write("SPEAKING=TRUE")
                    speaking_open=True
                    settings.close()
                    return
                else :
                    settings.write("SPEAKING=FALSE")
                    speaking_open=False
                    settings.close()
                    return
    else:
        with open("settings.txt","w",encoding="utf-8") as settings:
            s_input=input("首次使用该软件，请输入你是否要开启语音输入？y/n,非法输入则为n")
            if s_input in ['y','yes','是','True','true','Yes']:
                settings.write("SPEAKING=TRUE")
                speaking_open=True
                settings.close()
                return
            else :
                settings.write("SPEAKING=FALSE")
                speaking_open=False
                settings.close()
                return
# 在用户输入-c即主动要求修改语音输出配置时进行修改
def changedata():
        with open("settings.txt","w",encoding="utf-8") as settings:
            s_input=input("请输入你是否要开启语音输入？y/n,非法输入则为n：")
            if s_input in ['y','yes','是','True','true','Yes']:
                settings.write("SPEAKING=TRUE")
                speaking_open=True
                settings.close()

                return
            else :
                settings.write("SPEAKING=FALSE")
                speaking_open=False
                settings.close()
                return


# 输出 MIT LICENSE
def mitlicense():
    print('''
Copyright (C) 2021-2022  BillMa
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
''')

# 输出作者联系方式
def contactau():
    print("""
QQ:36937975
Email: maboning237103015@163.com
GitHub/Gitee: billma007
Website:https://billma.top
""")

# 开始欢迎界面和如何使用
def help_about():
    print('''
欢迎使用马哥聊天聊天机器人2.4.2 Developer Beta！
本软件由 BillMa编写，BillMa版权所有，本项目未经允许禁止商用
本项目已经开源，开源地址：https://github.com/billma007/mgchatrobot2或者在下面输入\"-git\"到达
本项目使用MIT LICENSE协议，使用该项目的任何部分时请遵守该协议。输入\"-mit\"查看该协议完整内容。
该版本为内测版本，请及时更新，最新release版本会及时发布在GiHub上
本网站官方网站：https://robotblog.billma.top(暂时还未开发）
----------------------------------------------------------------------------------------------
输入参数：
1.正常输入则会得到正常回复
2. -c:更改语音设置
3. -git:查看项目地址
4. -mit 查看 MIT LICENSE相关内容
5. -contact 联系作者
6. -official 前往官方网站(网站暂未完全开发，暂时无法访问）
7. -help 或者 -about 本程序的帮助和关于界面
8, -cls:清除当前页面
0. -q:结束程序。
可以开始愉快的聊天了！
''')
def robot_main():
    try:
        writingdata()
        help_about()
        while True:
            a=input("你：")
            if a[0]=='-':
                if a=="-c":
                    changedata()
                elif a=="-git":
                    open_new('https://github.com/billma007/mgchatrobot2')
                elif a=="-mit":
                    mitlicense()
                elif a=="-contact":
                    contactau()
                elif a=="-official":
                    open_new('https://billma.top')
                elif a=="-help" or a=="-about":
                    help_about()
                elif a=="-cls":
                    os.system("cls")
                elif a=="-q":
                    import gobackmain
                    gobackmain.gobackmain()
                else:
                    print("Error:入参错误")
            else:
                url='https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s'%a
                te=get(url).json()
                data=te['data']['info']['text']
                print(data)
                if speaking_open==True:
                    pt = pyttsx3.init()
                    pt.say(data)
                    pt.runAndWait()
    except Exception as eeee:
        print("出现错误：",eeee,"即将返回主页面")
def cometochat():
    robot_main()