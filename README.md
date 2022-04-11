# ✨✨✨multifunction✨✨✨

一个可以中英互译，聊天，查天气，下载视频，查询中华人民共和国疫情状况的软件.❤

语言/Language:简体中文/[English](README-en.md)

如果你不是开发者，或者你使用的是已经编译的exe文件，**相关问题请下滑找到“目前存在的一些问题解答✨”部分**；请确保你所获取的exe文件来自于本仓库的Release，第三方渠道获得的exe***不保证其安全性***。

![该图片著作权所有，请勿他用](https://cdn.jsdelivr.net/gh/billma007/imagesave/mainback.png)

该图片**著作权所有，请勿他用**

***请注意，本软件仅供学习交流使用，严禁用于违法用途，不要再使用本软件的时候违反你坐在国家/地区的法律！本软件作者不承担任何使用造成的后果和责任！本软件作者不承担任何使用造成的后果和责任！本软件作者不承担任何使用造成的后果和责任！***

## 目前已经实现的功能😘

1. 哔哩哔哩等80+网站视频下载（暂不支持会员下载）
2. QQ音乐，网易云音乐等6家主流音乐平台音乐下载（可以下载会员歌曲）
3. 使用免费API进行AI聊天
4. 中国天气查询
5. 全国疫情查询
6. 全国疫情数据地图可视化
7. 全球疫情数据地图可视化
8. 狗屁不通文章生成
9. 同一局域网下文件的快速传输
10. ~~视频转码（1.2.5版本后弃用ffmpeg）~~

## 目前仍然存在的bug💖

1. 视频下载时会进程卡死
2. 视频下载时无法携带cookie
3. 视频无法下载会员视频
4. 音乐下载启动会很慢
5. 如果是非正常退出本软件，音乐播放可能无法正常结束
6. 在虚拟环境下，可能没有办法加载静态文件
7. 文件传输时，二维码可能无法正确加载
8. 文件传输时，初次打开网页无法加载，需要刷新一下才可以下载

## 编写时遇到的问题😒

### 出现错误：Download has no attribute“buffer”

前往python解释器目录:`*/python/Lib/site-packages/you-get/common.py`注释掉下面这句话：

```py
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
```

### 出现错误：xxx(class) has no attribute “flush”

解决办法：在xxx里面添加:

```python
def flush(self):
  pass
```

### tkinter部分组件出现类似于"!toplevel!text"之类的错误

Stack Overflow上没有找到对应的解答。但是目前我是使用try except直接忽略这个错误。虽然这很不负责任，但是确实没啥好办法了；况且忽略这个错误后并没有发现任何问题。

### self.button.bind(事件，function)中总是报function缺失一个argument

在定义function的时候需要：

```python
def function(self,event):
  xxx
```

虽然用不到，但这个event必须加。

### 标准输出重定向后无法将标准输出重新设置到控制台

```python
# 先备份
self.stdoutback=sys.__stdout__
# 再重定向
sys.__stdout__=self
# 在重新设置
sys.__stdout__=self.stdoutback
```

## 目前存在的一些问题解答✨

以下问题是在进行内测时由内测成员提出来的，内测成员大多没有编程基础，因此本部分问题可能比较~~弱智~~通俗。

### 启动时弹出窗口：ImportError:Cannot import file或类似问题

该问题只会在虚拟化打包时出现。由于该exe会在虚拟内存中运行，会出现静态资源加载出错的问题。重启软件即可。

### 下载视频时出现“Oops,something went wrong"或其他问题

无法下载该网站视频或者该视频需要会员播放。

### 有时候退出软件后音乐仍然在播放？

这是因为软件异常退出导致的。你可以打开任务管理器(Ctrl+Alt+Delete)来关闭进程。

### 为什么不能复制粘贴?

~~或许你可以试试看Windows系统自带的快捷键Ctrl+V~~1.1版本将会设计一个快捷按钮直接读取剪贴板内容。

### 弹出窗口"该版本的.exe 与你运行的 Windows 版本不兼容。请查看计算机的系统信息，然后联系软件发布者"或类似问题

该软件是在64位系统的环境编译的。如果你的系统是32位的，那么这个软件就无法使用了。

如果你的系统是64位的，请尝试~~卸载腾讯电脑管家/360~~在杀毒软件中添加该软件的白名单。**如果杀毒软件报毒也是这么处理的。**

### 为什么我下载以后会显示"用其他应用打开"或者"不支持打开此文件？

~~你特么看看这是什么文件这是exe文件啊~~EXE文件，全名可执行文件，只能在受支持的Windows系统中使用。

### 我能下载VIP视频/大会员番剧/超前点播/付费观看视频/会员专属音乐吗？

由于浏览器cookie的限制，没有登录会员的设备是没法直接获取地址的。但是部分网站可以通过登录有会员的账号来进行爬取：

- 全程**不要使用**无痕浏览/强制刷新/禁用缓存/清除缓存
- 登录**带有会员**的账号，并且勾选“自动登录/记住我”
- 在该会员账号在线的同时复制视频网址到程序里面，部分网站可以下载。

## 快速开始😎

```git
git clone https://github.com/billma007/multifunction.git
cd multifunction
pip install -r requirements.txt
```

在运行main.py之前，请先前往python解释器目录:`*/python/Lib/site-packages/you-get/common.py`里面将下面一句话注释掉：

```py
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
```

否则将sys.stdout重定向至tkinter.Text输入框时会因为sys.stdout.buffer问题报错。

## 使用的开源库🐱‍🐉

本软件的制作离不开众多无私的开源库作者的支持，对这些大佬们的支持表示感谢。

使用了这些开源库(可以在requirements.txt中查看)：

| 使用的开源库 | 版本            | 用处              | 备注                              |
| ------------ | --------------- | ----------------- | --------------------------------- |
| pyttsx3      | **2.71**  | 播放语音(聊天)    |                                   |
| pillow       | latest          | 数据管理          |                                   |
| pyperclip    | latest          | 复制到剪贴板功能  |                                   |
| you-get      | latest          | 下载视频          |                                   |
| requests     | latest          | 爬虫爬取数据/下载 |                                   |
| playsound    | **1.2.2** | 播放背景音乐      | 1.4.0版本改用本地音乐后无版本限制 |
| pyecharts    | latest          | 疫情数据可视化    |                                   |
| openpyxl     | latest          | 疫情数据生成Excel | 为了压缩空间，在1.3.0版本后被舍弃 |
| pandas       | latest          | 疫情数据整理      | 为了压缩空间，在1.3.0版本后被舍弃 |
| tqdm         | latest          | 下载进度条        |                                   |
| pyecharts    | latest          | 生成地图          | 需要在打包的时候添加静态资源      |
| qrcode       | latest          | 生成二维码        |                                   |
| netifaces    | latest          | 获取本地网关和IP  |                                   |
| colorama     | latest          | 多颜色            | 1.1.0后弃用                       |
| pycryptodome | latest          | 加密算法          |                                   |
|              |                 |                   |                                   |

注意：pyttsx3大于2.71版本播放中文会报错，playsound非1.2.2版本无法在用pyinstaller打包以后播放网络音乐。

此外，在开源项目中，还需要以下依赖：

| col1           | 版本   |
| -------------- | ------ |
| pycryptodome   | latest |
| requests       | latest |
| alive-progress | latest |
| prettytable    | latest |
| click          | lates  |
| PyQt5          | latest |

在安装库的时候要注意：

```shell
pip install pyttsx==2.71
pip install playsound==1.2.2
```

## 使用的github开源项目

| 使用的开源项目             | 开源地址                                                                                    | 功能             |
| -------------------------- | ------------------------------------------------------------------------------------------- | ---------------- |
| soimort/you-get            | [https://github.com/soimort/you-get](https://github.com/soimort/you-get)                       | 下载视频         |
| sdushantha/qr-filetransfer | [https://github.com/sdushantha/qr-filetransfer](https://github.com/sdushantha/qr-filetransfer) | 文件传输         |
| menzi11/BullshitGenerator  | [https://github.com/menzi11/BullshitGenerator](https://github.com/menzi11/BullshitGenerator)   | 生成狗屁不通文章 |
| CharlesPikachu/musicdl     | [https://github.com/CharlesPikachu/musicdl](https://github.com/CharlesPikachu/musicdl)         | 下载音乐         |

## 编译成exe😍

音乐下载部分使用了github开源库[https://github.com/CharlesPikachu/musicdl](https://github.com/CharlesPikachu/musicdl "[https://github.com/CharlesPikachu/musicdl](https://github.com/CharlesPikachu/musicdl)"),原仓库使用PyQt5进行编写，而本软件主体采用tkinter编写，因此建议先将musicdlgui部分编译成exe，再在main.py中使用 `os.openfile()`函数调用已经编译完毕的musiclgui.exe

```cmd
pip install pyinstaller
pyinstaller --hidden-import=you_get.cli_wrapper --hidden-import=you_get.processor --hidden-import=you_get.utl --hidden-import=you_get.extractors --add-data=".\datasets;pyecharts\datasets\." --add-data=".\templates;pyecharts\render\templates\." -i ico.ico -w main.py
```

随后，将以下四个静态文件复制到dist/main文件夹：

1. `ico.ico`
2. `multimusic.mp3`
3. `videodownloadimage.jpg`
4. `musicdlgui.exe`

### 详解

由于you-get本身采用sys.argv调用的方法使用，所以部分模块无法正确引用，故使用隐式引入方法将4个仓库打包：

```cmd
--hidden-import=you_get.cli_wrapper --hidden-import=you_get.processor --hidden-import=you_get.utl --hidden-import=you_get.extractors
```

[由于pyinstaller不支持Pyecharts的静态资源引用打包](https://github.com/pyinstaller/pyinstaller/wiki/Supported-Packages),因此需要将 ``*/python38/Lib/Site-packages/pyecharts/datasets``和 ``*/python38/Lib/Site-packages/pyecharts/datasets/templates``的静态资源文件复制到目录下，然后在pyinstaller中主动添加静态文件：

```cmd
--add-data=".\datasets;pyecharts\datasets\." --add-data=".\templates;pyecharts\render\templates\."
```

### 如果你使用虚拟环境

请在构建 `pipenv shell`后前往 `C:\Users\yourusername\.virtualenvs\xxx-Jswk2kso(随机)\Lib\site-packages\you_get\common.py`中注释掉下列语句：

```py
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
```

## 结构架次🎉

本程序分为以下部分，各个部分都已经含有独立的仓库，可点击前往

- 主函数

  - `main.py`---主窗口生成
- 视频播放与转码

  - `video.py` ---下载视频
  - ~~change.py ---视频、图片、音频转码~~
    - 注意：1.2.5版本后不再支持ffmpeg转码
- 天气查询

  - ~~weather.py---主文件~~
  - ~~Ui_weather.py---PyQt5窗口~~
    - 注意：1.2.1版本后改用Tkinter：
  - `weather_tkinter.py`---改用tkinter制作的主页
  - `query.py`---数据处理
- 聊天系统

  - `chatmain.py`
- 翻译系统

  - `translategui.py`
- 生成图标

  - ~~icon.py ---通过base64进行编码自动生成图标~~1.3.0版本后采用静态资源
  - `ico.ico` ---图标{版权所有}
- 疫情查询

  - `covidcheck.py`---查询疫情的主界面
  - `covidgetjson.py`---从网络下载数据并生成json格式数据
  - `covidpyecharts1.py`---生成国内确诊地图
  - `covidpyecharts2.py`---生成国内治愈地图
  - `covidworld.py-`--生成国际确诊、死亡、治愈、新增数据地图
- 下载音乐

  - `musicdlgui.py`---下载音乐
- 狗屁不通文章生成

  - `goupibutong.py`----生成狗屁不通文章
  - `readJSON.py`---储存狗屁不通句子并且转化为json格式
- 文件传输

  - `qrcodemake.py ---文件传输`
- 其他

  - `README.md` ---英文文档
  - `README-Chinese.md` ---中文文档
  - `gnugpl3license.py`生成GNU-GPL3.0的具体内容
  - `small.py` ---最小化的需要函数
  - `requirements.txt` ---依赖库
  - `.gitignore` ---.gitignore
  - `LICENSE` ---GNU通用公共许可3.0（GNU/GPL3.0）

## 更新日志🐱‍🏍

- 2021/7/1 开始设计聊天机器人
  - 2021/7/14 1.0.0版本开始编写
  - 2021/7/17 1.0.0Developer Beta发布 支持基本的智能聊天
  - 2021/7/19 1.0.0Developer Beta2发布 进行少量内部人员测试
  - 2021/7/24 1.0.0正式版发布 修复了闪退等大量bug
  - 2021/7/28 1.1.0版本发布 支持pyttsx3语音播报但没法关掉
  - 2021/7/31 2.0.0发布 开始在原有API基础上进行在[nonebot2](https://github.com/nonebot/nonebot2)框架下的QQ机器人适配
  - 2021/8/19 2.0.0Pro版本在QQ上面适配大获成功，开始进行错误封装与代码完善
  - 2021/8/24 电脑坏了，而且没有提交到GitHub，花了一个月时间构建的代码全部嗝屁，只留下了8行基本代码
  - 2022/3/3 2.0.0Rewrite(2.1.0)腾空出世，将这个8行的陈旧的代码翻出来重构并重新编写，但是已经无法重现当年辉煌
  - 2022/3/4 2.2.0添加目录并给用户更多选项
  - 2022/3/5 2.3.0 添加settings.txt可以让用户自主选择是否开启pyttsx3语音播报
  - 2022/3/6 2.4.0正式版和2.4.2Developer Beta 添加自动检测和生成settings.txt的代码，目录下没有settings.txt不会报错或者闪退了。
  - 2022/3/6 2.4.1-2.4.2添加自动检测和生成settings.txt的代码，目录下没有settings.txt不会报错或者闪退了。
  - 2022/3/7 2.4.3 修复了 `read()`函数在读入时无法识别utf-8字符的问题，将默认的gbk字符表切换成了utf-8字符
  - 2022/3/8 正式并入该项目
- 2022/1/21 开始设计翻译系统
  - 2022/1/21 开始放寒假，学习requests爬虫知识并开始筹划
  - 2022/1/31 农历春节，写完了MS-DOS1.0版本的前身Basic1.0
  - 2022/2/8 农历大年初八，增加了语音输出的功能，但是要上学了，便没有提交代码
  - 2022/2/15 元宵节，突如其来的疫情让我们~~被迫~~上网课，便在空余时间开始开发语音输出功能(当天便写完了Basic1.1)
  - 2022/3/1 顺利完成Basic2.0，增加了语音设置和剪贴板读取功能
  - 2022/3/4 Basic2.2完成 增加色彩功能
  - 2022/3/9 MS-DOS1.0.0版本发布，同时GUI1.0版本开始筹划并初步完成。
  - 2022/3/9 GUI1.0并入该项目
- 2022/2/28 开始设计天气查询系统
  - 2022/3/2 打表完毕(~真他妈累~真开心)
  - 2022/3/3 1.0发布，支持拼音查询天气
  - 2022/3/4 1.1版本，修复了大量bug
  - 2022/3/5 1.2.1-2版本增加了utf-8字符的兼容性，可以不用拼音代替中文字符。同时2.0.0GUI版开始制作
  - 2022/3/6 1.3.0发布，修复了API接口报错的问题
  - 2022/3/7 2.0.0正式版发布，正式使用PyQt5生成**GUI**界面，操作更加便捷
  - 2022/3/82.0.1版本出炉，可以自动生成 `city_code.txt`文件，解决了目录下没有该文件导致报错的问题。
  - 2022/3/10 GUI2.0.1版本并入该项目
- 2022/2/28 开始设计视频下载并开始整合
- 2022/3/12 增加视频转码功能
- 2022/3/16 找了[@RUA](https://2278365235.qzone.qq.com)画了个~~吉祥物~~图标
- 2022/3/17--1.0.0Beta  把主页面做出来了
- 2022/3/18--1.0.1版本  ~~上课摸鱼~~闲来无事做了个音乐播放，音乐是~~阴游~~音游Phigros的谢幕曲。
- 2022/3/19--1.0.2版本 修复了bug
- 2022/3/21--1.1.0版本：
  - 推翻原代码重构，扩充了以下功能：
  - 1. 查天气
  - 2. AI聊天
  - 3. 放音乐
  - 4. 添加了几个按钮
  - 5. 开启多线程
  - 6. 由于PyQt5实在是太太太占空间了，决定取消PyQt5改用Tkinter
- 2022年3月22日--1.2.1版本：
  - 1. 修复了sys.stdout没有重定向至text文本框导致无法显示进度的问题
  - 2. 将stdout改成__stdout__保证软件安全
  - 3. 将sys.stderr也重定向至文本框
  - 4. 使用sys.exit()抛出异常来结束软件，而不是os.exit()
  - 5. 1.2.1div2(分支版本)添加自动更新系统

    - 如果在中国大陆，会自动使用jsdelivr进行加速
- 2022年3月24日--1.2.2版本：
  - 1. 重构代码，开启多线程来防止卡死
  - 2. 修复了转码功能报错的问题
  - 3. 修复了关闭程序后仍在播放音乐的bug
  - 4. 修复了使用某功能后再点击停止音乐出线bug的问题
  - 5. 代码结构改变：支持功能多开
  - 6. 修复了部分按钮不动的bug
  - 7. 由于cdn.jsdelivr.net老是抽风，决定使用fastly加速
- 2022年3月24日--1.2.3版本：
  - 1. 再次修复了playsound函数抽风导致音乐停不下来的问题
  - 2. 谁~~他妈~~知道fastly.jsdelivr.net也抽风,所以我决定双保险，在cdn与fastly之间取最大值来保持更新
  - 3. 优化更新系统，新增cdn线路
  - 4. 修复了部分窗口部分按钮激活无效函数的bug
- 2022年3月24日--1.2.3dev1(分支)版本：
  - 1. 将sys.exit(0)改成了os._exit(0)使所有进程退出
  - 2. 修改了you-get的源码来防止buffer输出缓存问题

    - sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
- 2022年3月25日--1.2.4版本：
  - 1. 更新了更新系统
  - 2. 修复了ffmpeg的相关bug，增加了批量转码功能
  - 3. 优化了聊天系统
- 2022年3月28日--1.2.5版本：
  - 1. 取消了转码功能
  - 2. 增加了新冠疫情查询功能
  - 3. 修复了翻译、聊天、天气查询的bug
- 2022年3月29日--1.2.5div1(分支)版本：
  - 修复了pyecharts无法编译的问题，直接将其静态资源放到目录下一同打包。
- 2022年2月31日--1.3.0版本：
  - 取消了base64生成ico.ico
  - 取消了更新系统
  - 增加全国、全球疫情地图
  - 修复了天气无法启动的问题
- 2022年4月8日--1.4.0版本：
  - 增加了狗屁不通文章生成
  - 增加了音乐下载功能
  - 优化了UI界面
  - 优化了精简版
  - 优化了最小化托盘
  - 增加了按钮
- 2022年4月9日--1.4.0Release版本：
  - 优化了一些功能
  - 修复了视频无法下载的问题
  - 优化了更新系统
  - 优化了启动速度

## 关于作者😁

江苏省苏州市的一个普通高中牲，一个因为~~玩电脑被学校处分~~在省赛就被刷下来的信息学奥林匹克竞赛选手，热爱编程，但不喜欢前端。

欢迎通过以下联系方式与我探讨信息竞赛、博客搭建、学术讨论以及扯皮：

- QQ:36937975
- Twitter:@billma6688
- Facebook/Instagram:billma007
- CodeForces/USACO/AtCoder:billma007(~~别看我很拉的~~不常用)
- Email:maboning237103015@163.com

## 推广：我的博客🤞

[欢迎光临！](https://billma.top)

## 许可证

[GNU通用公共许可3.0（GNU/GPL3.0)](LICENSE)

**注意**：本软件整体使用GNU通用公共许可3.0，但是本软件的各个部分使用不同的软件许可证，详情请前往各个仓库。

```abc
X:400
T:Drum Kit
%%map drummap D    print=D heads=x_head   % pedal hi-hat
%%map drummap E    print=E                % bass drum 1
%%map drummap F    print=F                % acoustic bass drum
%%map drummap G    print=G                % low floor tom-tom
%%map drummap A    print=A                % high floor tom-tom
%%map drummap B    print=B                % low tom-tom
%%map drummap ^B   print=B heads=triangle % tambourine
%%map drummap c    print=c                % acoustic snare
%%map drummap _c   print=c                % electric snare
%%map drummap ^c   print=c heads=triangle % low wood block
%%map drummap =c   print=c                % side stick
%%map drummap d    print=d                % low-mid tom tom
%%map drummap ^d   print=d heads=triangle % high wood block
%%map drummap e    print=e                % high-mid tom tom
%%map drummap ^e   print=e heads=triangle % cowbell
%%map drummap f    print=f                % high tom tom
%%map drummap ^f   print=f heads=x_head   % ride cymbal 1
%%map drummap g    print=g heads=x_head   % closed hi-hat
%%map drummap ^g   print=g heads=diamond  % open hi-hat
%%map drummap a    print=a heads=x_head   % crash cymbal 1
%%map drummap ^a   print=a heads=triangle % open triangle
%%MIDI drummap D   44 % pedal hi-hat
%%MIDI drummap E   36 % bass drum 1
%%MIDI drummap F   35 % acoustic bass drum
%%MIDI drummap G   41 % low floor tom-tom
%%MIDI drummap A   43 % high floor tom-tom
%%MIDI drummap B   45 % low tom-tom
%%MIDI drummap ^B  54 % tambourine
%%MIDI drummap c   38 % acoustic snare
%%MIDI drummap _c  40 % electric snare
%%MIDI drummap ^c  77 % low wood block
%%MIDI drummap =c  37 % side stick
%%MIDI drummap d   47 % low-mid tom tom
%%MIDI drummap ^d  76 % high wood block
%%MIDI drummap e   48 % high-mid tom tom
%%MIDI drummap ^e  56 % cowbell
%%MIDI drummap f   50 % high tom tom
%%MIDI drummap ^f  51 % ride cymbal 1
%%MIDI drummap g   42 % closed hi-hat
%%MIDI drummap ^g  46 % open hi-hat
%%MIDI drummap a   49 % crash cymbal 1
%%MIDI drummap ^a  81 % open triangle
%%score (1 2)
Q:1/4=120
M:4/4
L:1/4
K:C perc
V:1
z4| g/^f/g/^f/ g/^f/g/^f/| c/^f/g/^f/ A/^f/g/^f/| c/^f/g/^f/ A/^f/g/^f/|
c/c/g/^f/ A/A/g/^f/| c/^f/c/^f/ A/^f/A/^f/|(3B/B/B/ (3f/f/f/ (3e/e/e/ (3d/d/d/ | a4|
V:2
E D E/E/ D|E D E/E/ D|E D E/E/ D|E D E/E/ D|
E D E/E/ D|E D E/E/ D|E D E/E/ D|E D E/E/ D|

```

## 附录

### 支持查询疫情的省份

目前仅支持省份查询。输入省份即可查询该省份所有地级市的疫情情况。

支持查询31个省、市、自治区和新疆生产建设兵团、港澳台的疫情。

香港澳门和台湾的疫情查询暂不支持下沉至地级市/区。

### 支持音乐下载的网站

| 网站名称 | 支持音频 | 支持VIP/绿钻/黑胶？ |
| -------- | -------- | ------------------- |
| QQmusic  | ✓       | ✓                  |
| 网易     | ✓       | ✓                  |
| 酷我     | ✓       | ✓                  |
| 酷狗     | ✓       | ✓                  |
| 千千音乐 | ✓       | ✓                  |

### 支持视频图像下载的网站

同you-get。对于无反爬机制的网站，本软件可以下载任意视频；对于有反扒机制但在下列列出的网站，同样支持。对于有反扒机制但没列出的网站，暂不支持。会员/登陆限制网站需要提供已经开通会员账号的cookie。

|             网站名称             | 网址                                                                                                   | 视频支持 | 图像支持 | 音频支持 |
| :-------------------------------: | :----------------------------------------------------------------------------------------------------- | :------: | :------: | :------: |
|         **YouTube**         | [https://www.youtube.com/](https://www.youtube.com/)                                                      |    ✓    |          |          |
|         **Twitter**         | [https://twitter.com/](https://twitter.com/)                                                              |    ✓    |    ✓    |          |
|                VK                | [http://vk.com/](http://vk.com/)                                                                          |    ✓    |    ✓    |          |
|               Vine               | [https://vine.co/](https://vine.co/)                                                                      |    ✓    |          |          |
|               Vimeo               | [https://vimeo.com/](https://vimeo.com/)                                                                  |    ✓    |          |          |
|               Veoh               | [http://www.veoh.com/](http://www.veoh.com/)                                                              |    ✓    |          |          |
|         **Tumblr**         | [https://www.tumblr.com/](https://www.tumblr.com/)                                                        |    ✓    |    ✓    |    ✓    |
|                TED                | [http://www.ted.com/](http://www.ted.com/)                                                                |    ✓    |          |          |
|            SoundCloud            | [https://soundcloud.com/](https://soundcloud.com/)                                                        |          |          |    ✓    |
|             SHOWROOM             | [https://www.showroom-live.com/](https://www.showroom-live.com/)                                          |    ✓    |          |          |
|             Pinterest             | [https://www.pinterest.com/](https://www.pinterest.com/)                                                  |          |    ✓    |          |
|               MTV81               | [http://www.mtv81.com/](http://www.mtv81.com/)                                                            |    ✓    |          |          |
|             Mixcloud             | [https://www.mixcloud.com/](https://www.mixcloud.com/)                                                    |          |          |    ✓    |
|             Metacafe             | [http://www.metacafe.com/](http://www.metacafe.com/)                                                      |    ✓    |          |          |
|              Magisto              | [http://www.magisto.com/](http://www.magisto.com/)                                                        |    ✓    |          |          |
|           Khan Academy           | [https://www.khanacademy.org/](https://www.khanacademy.org/)                                              |    ✓    |          |          |
|         Internet Archive         | [https://archive.org/](https://archive.org/)                                                              |    ✓    |          |          |
|        **Instagram**        | [https://instagram.com/](https://instagram.com/)                                                          |    ✓    |    ✓    |          |
|               InfoQ               | [http://www.infoq.com/presentations/](http://www.infoq.com/presentations/)                                |    ✓    |          |          |
|               Imgur               | [http://imgur.com/](http://imgur.com/)                                                                    |          |    ✓    |          |
|        Heavy Music Archive        | [http://www.heavy-music.ru/](http://www.heavy-music.ru/)                                                  |          |          |    ✓    |
|             Freesound             | [http://www.freesound.org/](http://www.freesound.org/)                                                    |          |          |    ✓    |
|              Flickr              | [https://www.flickr.com/](https://www.flickr.com/)                                                        |    ✓    |    ✓    |          |
|             FC2 Video             | [http://video.fc2.com/](http://video.fc2.com/)                                                            |    ✓    |          |          |
|             Facebook             | [https://www.facebook.com/](https://www.facebook.com/)                                                    |    ✓    |          |          |
|               eHow               | [http://www.ehow.com/](http://www.ehow.com/)                                                              |    ✓    |          |          |
|            Dailymotion            | [http://www.dailymotion.com/](http://www.dailymotion.com/)                                                |    ✓    |          |          |
|               Coub               | [http://coub.com/](http://coub.com/)                                                                      |    ✓    |          |          |
|                CBS                | [http://www.cbs.com/](http://www.cbs.com/)                                                                |    ✓    |          |          |
|             Bandcamp             | [http://bandcamp.com/](http://bandcamp.com/)                                                              |          |          |    ✓    |
|             AliveThai             | [http://alive.in.th/](http://alive.in.th/)                                                                |    ✓    |          |          |
|            interest.me            | [http://ch.interest.me/tvn](http://ch.interest.me/tvn)                                                    |    ✓    |          |          |
|     **755ナナゴーゴー**     | [http://7gogo.jp/](http://7gogo.jp/)                                                                      |    ✓    |    ✓    |          |
|  **niconicoニコニコ動画**  | [http://www.nicovideo.jp/](http://www.nicovideo.jp/)                                                      |    ✓    |          |          |
| **163/网易视频/网易云音乐** | [http://v.163.com/](http://v.163.com/) or [http://music.163.com/](http://music.163.com/)                     |    ✓    |          |    ✓    |
|               56网               | [http://www.56.com/](http://www.56.com/)                                                                  |    ✓    |          |          |
|          **AcFun**          | [http://www.acfun.cn/](http://www.acfun.cn/)                                                              |    ✓    |          |          |
|     **Baidu/百度贴吧**     | [http://tieba.baidu.com/](http://tieba.baidu.com/)                                                        |    ✓    |    ✓    |          |
|             爆米花网             | [http://www.baomihua.com/](http://www.baomihua.com/)                                                      |    ✓    |          |          |
|    **bilibili/哔哩哔哩**    | [http://www.bilibili.com/](http://www.bilibili.com/)                                                      |    ✓    |    ✓    |    ✓    |
|               豆瓣               | [http://www.douban.com/](http://www.douban.com/)                                                          |    ✓    |          |    ✓    |
|               斗鱼               | [http://www.douyutv.com/](http://www.douyutv.com/)                                                        |    ✓    |          |          |
|             凤凰视频             | [http://v.ifeng.com/](http://v.ifeng.com/)                                                                |    ✓    |          |          |
|              风行网              | [http://www.fun.tv/](http://www.fun.tv/)                                                                  |    ✓    |          |          |
|           iQIYI/爱奇艺           | [http://www.iqiyi.com/](http://www.iqiyi.com/)                                                            |    ✓    |          |          |
|              激动网              | [http://www.joy.cn/](http://www.joy.cn/)                                                                  |    ✓    |          |          |
|               酷6网               | [http://www.ku6.com/](http://www.ku6.com/)                                                                |    ✓    |          |          |
|             酷狗音乐             | [http://www.kugou.com/](http://www.kugou.com/)                                                            |          |          |    ✓    |
|             酷我音乐             | [http://www.kuwo.cn/](http://www.kuwo.cn/)                                                                |          |          |    ✓    |
|              乐视网              | [http://www.le.com/](http://www.le.com/)                                                                  |    ✓    |          |          |
|              荔枝FM              | [http://www.lizhi.fm/](http://www.lizhi.fm/)                                                              |          |          |    ✓    |
|             懒人听书             | [http://www.lrts.me/](http://www.lrts.me/)                                                                |          |          |    ✓    |
|               秒拍               | [http://www.miaopai.com/](http://www.miaopai.com/)                                                        |    ✓    |          |          |
|           MioMio弹幕网           | [http://www.miomio.tv/](http://www.miomio.tv/)                                                            |    ✓    |          |          |
|          MissEvan/猫耳FM          | [http://www.missevan.com/](http://www.missevan.com/)                                                      |          |          |    ✓    |
|              痞客邦              | [https://www.pixnet.net/](https://www.pixnet.net/)                                                        |    ✓    |          |          |
|             PPTV聚力             | [http://www.pptv.com/](http://www.pptv.com/)                                                              |    ✓    |          |          |
|              齐鲁网              | [http://v.iqilu.com/](http://v.iqilu.com/)                                                                |    ✓    |          |          |
|            QQ/腾讯视频            | [http://v.qq.com/](http://v.qq.com/)                                                                      |    ✓    |          |          |
|             企鹅直播             | [http://live.qq.com/](http://live.qq.com/)                                                                |    ✓    |          |          |
|    Sina/新浪视频/微博秒拍视频    | [http://video.sina.com.cn/](http://video.sina.com.cn/) or [http://video.weibo.com/](http://video.weibo.com/) |    ✓    |          |          |
|           Sohu/搜狐视频           | [http://tv.sohu.com/](http://tv.sohu.com/)                                                                |    ✓    |          |          |
|       **Tudou/土豆**       | [http://www.tudou.com/](http://www.tudou.com/)                                                            |    ✓    |          |          |
|             阳光卫视             | [http://www.isuntv.com/](http://www.isuntv.com/)                                                          |    ✓    |          |          |
|       **Youku/优酷**       | [http://www.youku.com/](http://www.youku.com/)                                                            |    ✓    |          |          |
|              战旗TV              | [http://www.zhanqi.tv/lives](http://www.zhanqi.tv/lives)                                                  |    ✓    |          |          |
|              央视网              | [http://www.cntv.cn/](http://www.cntv.cn/)                                                                |    ✓    |          |          |
|           Naver/네이버           | [http://tvcast.naver.com/](http://tvcast.naver.com/)                                                      |    ✓    |          |          |
|              芒果TV              | [http://www.mgtv.com/](http://www.mgtv.com/)                                                              |    ✓    |          |          |
|              火猫TV              | [http://www.huomao.com/](http://www.huomao.com/)                                                          |    ✓    |          |          |
|            阳光宽频网            | [http://www.365yg.com/](http://www.365yg.com/)                                                            |    ✓    |          |          |
|             西瓜视频             | [https://www.ixigua.com/](https://www.ixigua.com/)                                                        |    ✓    |          |          |
|              新片场              | [https://www.xinpianchang.com/](https://www.xinpianchang.com/)                                            |    ✓    |          |          |
|               快手               | [https://www.kuaishou.com/](https://www.kuaishou.com/)                                                    |    ✓    |    ✓    |          |
|               抖音               | [https://www.douyin.com/](https://www.douyin.com/)                                                        |    ✓    |          |          |
|              TikTok              | [https://www.tiktok.com/](https://www.tiktok.com/)                                                        |    ✓    |          |          |
|           中国体育(TV)           | [http://v.zhibo.tv/](http://v.zhibo.tv/)  or  [http://video.zhibo.tv/](http://video.zhibo.tv/)               |    ✓    |          |          |
|               知乎               | [https://www.zhihu.com/](https://www.zhihu.com/)                                                          |    ✓    |          |          |

### 支持查询天气的城市

共支持333个城市和2981个县/区。

注意，查询的时候不要加市、区等字样（特区，新区除外）

例如:`苏州`，`上海`，`姑苏`，`海淀`，`黄埔`，`香港`等

部分新区或者自治州例外，如 `浦东新区`，`伊犁自治州`

暂不支持：苏州工业园区

| 序号 | 城市                   | 所属省份         |
| ---- | ---------------------- | ---------------- |
| 1    | 阿坝藏族羌族自治州     | 四川省           |
| 2    | 阿克苏地区             | 新疆维吾尔自治区 |
| 3    | 阿拉善盟               | 内蒙古自治区     |
| 4    | 阿勒泰地区             | 新疆维吾尔自治区 |
| 5    | 阿里地区               | 西藏自治区       |
| 6    | 安康市                 | 陕西省           |
| 7    | 安庆市                 | 安徽省           |
| 8    | 安顺市                 | 贵州省           |
| 9    | 安阳市                 | 河南省           |
| 10   | 鞍山市                 | 辽宁省           |
| 11   | 巴彦淖尔市             | 内蒙古自治区     |
| 12   | 巴音郭楞蒙古自治州     | 新疆维吾尔自治区 |
| 13   | 巴中市                 | 四川省           |
| 14   | 白城市                 | 吉林省           |
| 15   | 白山市                 | 吉林省           |
| 16   | 白银市                 | 甘肃省           |
| 17   | 百色市                 | 广西壮族自治区   |
| 18   | 蚌埠市                 | 安徽省           |
| 19   | 包头市                 | 内蒙古自治区     |
| 20   | 宝鸡市                 | 陕西省           |
| 21   | 保定市                 | 河北省           |
| 22   | 保山市                 | 云南省           |
| 23   | 北海市                 | 广西壮族自治区   |
| 24   | 本溪市                 | 辽宁省           |
| 25   | 毕节地区               | 贵州省           |
| 26   | 滨州市                 | 山东省           |
| 27   | 博尔塔拉蒙古自治州     | 新疆维吾尔自治区 |
| 28   | 沧州市                 | 河北省           |
| 29   | 昌都地区               | 西藏自治区       |
| 30   | 昌吉回族自治州         | 新疆维吾尔自治区 |
| 31   | 长春市                 | 吉林省           |
| 32   | 长沙市                 | 湖南省           |
| 33   | 长治市                 | 山西省           |
| 34   | 常德市                 | 湖南省           |
| 35   | 常州市                 | 江苏省           |
| 36   | 巢湖市                 | 安徽省           |
| 37   | 朝阳市                 | 辽宁省           |
| 38   | 潮州市                 | 广东省           |
| 39   | 郴州市                 | 湖南省           |
| 40   | 成都市                 | 四川省           |
| 41   | 承德市                 | 河北省           |
| 42   | 池州市                 | 安徽省           |
| 43   | 赤峰市                 | 内蒙古自治区     |
| 44   | 崇左市                 | 广西壮族自治区   |
| 45   | 滁州市                 | 安徽省           |
| 46   | 楚雄彝族自治州         | 云南省           |
| 47   | 达州市                 | 四川省           |
| 48   | 大理白族自治州         | 云南省           |
| 49   | 大连市                 | 辽宁省           |
| 50   | 大庆市                 | 黑龙江省         |
| 51   | 大同市                 | 山西省           |
| 52   | 大兴安岭地区           | 黑龙江省         |
| 53   | 丹东市                 | 辽宁省           |
| 54   | 德宏傣族景颇族自治州   | 云南省           |
| 55   | 德阳市                 | 四川省           |
| 56   | 德州市                 | 山东省           |
| 57   | 迪庆藏族自治州         | 云南省           |
| 58   | 定西市                 | 甘肃省           |
| 59   | 东莞市                 | 广东省           |
| 60   | 东营市                 | 山东省           |
| 61   | 鄂尔多斯市             | 内蒙古自治区     |
| 62   | 鄂州市                 | 湖北省           |
| 63   | 恩施土家族苗族自治州   | 湖北省           |
| 64   | 防城港市               | 广西壮族自治区   |
| 65   | 佛山市                 | 广东省           |
| 66   | 福州市                 | 福建省           |
| 67   | 抚顺市                 | 辽宁省           |
| 68   | 抚州市                 | 江西省           |
| 69   | 阜新市                 | 辽宁省           |
| 70   | 阜阳市                 | 安徽省           |
| 71   | 甘南州                 | 甘肃省           |
| 72   | 甘孜藏族自治州         | 四川省           |
| 73   | 赣州市                 | 江西省           |
| 74   | 固原市                 | 宁夏回族自治区   |
| 75   | 广安市                 | 四川省           |
| 76   | 广元市                 | 四川省           |
| 77   | 广州市                 | 广东省           |
| 78   | 贵港市                 | 广西壮族自治区   |
| 79   | 贵阳市                 | 贵州省           |
| 80   | 桂林市                 | 广西壮族自治区   |
| 81   | 果洛藏族自治州         | 青海省           |
| 82   | 哈尔滨市               | 黑龙江省         |
| 83   | 哈密地区               | 新疆维吾尔自治区 |
| 84   | 海北藏族自治州         | 青海省           |
| 85   | 海东地区               | 青海省           |
| 86   | 海口市                 | 海南省           |
| 87   | 海南藏族自治州         | 青海省           |
| 88   | 海西蒙古族藏族自治州   | 青海省           |
| 89   | 邯郸市                 | 河北省           |
| 90   | 汉中市                 | 陕西省           |
| 91   | 杭州市                 | 浙江省           |
| 92   | 毫州市                 | 安徽省           |
| 93   | 合肥市                 | 安徽省           |
| 94   | 和田地区               | 新疆维吾尔自治区 |
| 95   | 河池市                 | 广西壮族自治区   |
| 96   | 河源市                 | 广东省           |
| 97   | 菏泽市                 | 山东省           |
| 98   | 贺州市                 | 广西壮族自治区   |
| 99   | 鹤壁市                 | 河南省           |
| 100  | 鹤岗市                 | 黑龙江省         |
| 101  | 黑河市                 | 黑龙江省         |
| 102  | 衡水市                 | 河北省           |
| 103  | 衡阳市                 | 湖南省           |
| 104  | 红河哈尼族彝族自治州   | 云南省           |
| 105  | 呼和浩特市             | 内蒙古自治区     |
| 106  | 呼伦贝尔市             | 内蒙古自治区     |
| 107  | 湖州市                 | 浙江省           |
| 108  | 葫芦岛市               | 辽宁省           |
| 109  | 怀化市                 | 湖南省           |
| 110  | 淮安市                 | 江苏省           |
| 111  | 淮北市                 | 安徽省           |
| 112  | 淮南市                 | 安徽省           |
| 113  | 黄冈市                 | 湖北省           |
| 114  | 黄南藏族自治州         | 青海省           |
| 115  | 黄山市                 | 安徽省           |
| 116  | 黄石市                 | 湖北省           |
| 117  | 惠州市                 | 广东省           |
| 118  | 鸡西市                 | 黑龙江省         |
| 119  | 吉安市                 | 江西省           |
| 120  | 吉林市                 | 吉林省           |
| 121  | 济南市                 | 山东省           |
| 122  | 济宁市                 | 山东省           |
| 123  | 佳木斯市               | 黑龙江省         |
| 124  | 嘉兴市                 | 浙江省           |
| 125  | 嘉峪关市               | 甘肃省           |
| 126  | 江门市                 | 广东省           |
| 127  | 焦作市                 | 河南省           |
| 128  | 揭阳市                 | 广东省           |
| 129  | 金昌市                 | 甘肃省           |
| 130  | 金华市                 | 浙江省           |
| 131  | 锦州市                 | 辽宁省           |
| 132  | 晋城市                 | 山西省           |
| 133  | 晋中市                 | 山西省           |
| 134  | 荆门市                 | 湖北省           |
| 135  | 荆州市                 | 湖北省           |
| 136  | 景德镇市               | 江西省           |
| 137  | 九江市                 | 江西省           |
| 138  | 酒泉市                 | 甘肃省           |
| 139  | 喀什地区               | 新疆维吾尔自治区 |
| 140  | 开封市                 | 河南省           |
| 141  | 克拉玛依市             | 新疆维吾尔自治区 |
| 142  | 克孜勒苏柯尔克孜自治州 | 新疆维吾尔自治区 |
| 143  | 昆明市                 | 云南省           |
| 144  | 拉萨市                 | 西藏自治区       |
| 145  | 来宾市                 | 广西壮族自治区   |
| 146  | 莱芜市                 | 山东省           |
| 147  | 兰州市                 | 甘肃省           |
| 148  | 廊坊市                 | 河北省           |
| 149  | 乐山市                 | 四川省           |
| 150  | 丽江市                 | 云南省           |
| 151  | 丽水市                 | 浙江省           |
| 152  | 连云港市               | 江苏省           |
| 153  | 凉山彝族自治州         | 四川省           |
| 154  | 辽阳市                 | 辽宁省           |
| 155  | 辽源市                 | 吉林省           |
| 156  | 聊城市                 | 山东省           |
| 157  | 林芝地区               | 西藏自治区       |
| 158  | 临沧市                 | 云南省           |
| 159  | 临汾市                 | 山西省           |
| 160  | 临夏州                 | 甘肃省           |
| 161  | 临沂市                 | 山东省           |
| 162  | 柳州市                 | 广西壮族自治区   |
| 163  | 六安市                 | 安徽省           |
| 164  | 六盘水市               | 贵州省           |
| 165  | 龙岩市                 | 福建省           |
| 166  | 陇南市                 | 甘肃省           |
| 167  | 娄底市                 | 湖南省           |
| 168  | 泸州市                 | 四川省           |
| 169  | 吕梁市                 | 山西省           |
| 170  | 洛阳市                 | 河南省           |
| 171  | 漯河市                 | 河南省           |
| 172  | 马鞍山市               | 安徽省           |
| 173  | 茂名市                 | 广东省           |
| 174  | 眉山市                 | 四川省           |
| 175  | 梅州市                 | 广东省           |
| 176  | 绵阳市                 | 四川省           |
| 177  | 牡丹江市               | 黑龙江省         |
| 178  | 内江市                 | 四川省           |
| 179  | 那曲地区               | 西藏自治区       |
| 180  | 南昌市                 | 江西省           |
| 181  | 南充市                 | 四川省           |
| 182  | 南京市                 | 江苏省           |
| 183  | 南宁市                 | 广西壮族自治区   |
| 184  | 南平市                 | 福建省           |
| 185  | 南通市                 | 江苏省           |
| 186  | 南阳市                 | 河南省           |
| 187  | 宁波市                 | 浙江省           |
| 188  | 宁德市                 | 福建省           |
| 189  | 怒江傈僳族自治州       | 云南省           |
| 190  | 攀枝花市               | 四川省           |
| 191  | 盘锦市                 | 辽宁省           |
| 192  | 平顶山市               | 河南省           |
| 193  | 平凉市                 | 甘肃省           |
| 194  | 萍乡市                 | 江西省           |
| 195  | 莆田市                 | 福建省           |
| 196  | 濮阳市                 | 河南省           |
| 197  | 普洱市                 | 云南省           |
| 198  | 七台河市               | 黑龙江省         |
| 199  | 齐齐哈尔市             | 黑龙江省         |
| 200  | 黔东南苗族侗族自治州   | 贵州省           |
| 201  | 黔南布依族苗族自治州   | 贵州省           |
| 202  | 黔西南布依族苗族自治州 | 贵州省           |
| 203  | 钦州市                 | 广西壮族自治区   |
| 204  | 秦皇岛市               | 河北省           |
| 205  | 青岛市                 | 山东省           |
| 206  | 清远市                 | 广东省           |
| 207  | 庆阳市                 | 甘肃省           |
| 208  | 曲靖市                 | 云南省           |
| 209  | 衢州市                 | 浙江省           |
| 210  | 泉州市                 | 福建省           |
| 211  | 日喀则地区             | 西藏自治区       |
| 212  | 日照市                 | 山东省           |
| 213  | 三门峡市               | 河南省           |
| 214  | 三明市                 | 福建省           |
| 215  | 三亚市                 | 海南省           |
| 216  | 山南地区               | 西藏自治区       |
| 217  | 汕头市                 | 广东省           |
| 218  | 汕尾市                 | 广东省           |
| 219  | 商洛市                 | 陕西省           |
| 220  | 商丘市                 | 河南省           |
| 221  | 上饶市                 | 江西省           |
| 222  | 韶关市                 | 广东省           |
| 223  | 邵阳市                 | 湖南省           |
| 224  | 绍兴市                 | 浙江省           |
| 225  | 深圳市                 | 广东省           |
| 226  | 沈阳市                 | 辽宁省           |
| 227  | 十堰市                 | 湖北省           |
| 228  | 石家庄市               | 河北省           |
| 229  | 石嘴山市               | 宁夏回族自治区   |
| 230  | 双鸭山市               | 黑龙江省         |
| 231  | 朔州市                 | 山西省           |
| 232  | 四平市                 | 吉林省           |
| 233  | 松原市                 | 吉林省           |
| 234  | 苏州市                 | 江苏省           |
| 235  | 宿迁市                 | 江苏省           |
| 236  | 宿州市                 | 安徽省           |
| 237  | 绥化市                 | 黑龙江省         |
| 238  | 随州市                 | 湖北省           |
| 239  | 遂宁市                 | 四川省           |
| 240  | 塔城地区               | 新疆维吾尔自治区 |
| 241  | 台州市                 | 浙江省           |
| 242  | 太原市                 | 山西省           |
| 243  | 泰安市                 | 山东省           |
| 244  | 泰州市                 | 江苏省           |
| 245  | 唐山市                 | 河北省           |
| 246  | 天水市                 | 甘肃省           |
| 247  | 铁岭市                 | 辽宁省           |
| 248  | 通化市                 | 吉林省           |
| 249  | 通辽市                 | 内蒙古自治区     |
| 250  | 铜川市                 | 陕西省           |
| 251  | 铜陵市                 | 安徽省           |
| 252  | 铜仁市                 | 贵州省           |
| 253  | 吐鲁番地区             | 新疆维吾尔自治区 |
| 254  | 威海市                 | 山东省           |
| 255  | 潍坊市                 | 山东省           |
| 256  | 渭南市                 | 陕西省           |
| 257  | 温州市                 | 浙江省           |
| 258  | 文山壮族苗族自治州     | 云南省           |
| 259  | 乌海市                 | 内蒙古自治区     |
| 260  | 乌兰察布市             | 内蒙古自治区     |
| 261  | 乌鲁木齐市             | 新疆维吾尔自治区 |
| 262  | 无锡市                 | 江苏省           |
| 263  | 吴忠市                 | 宁夏回族自治区   |
| 264  | 芜湖市                 | 安徽省           |
| 265  | 梧州市                 | 广西壮族自治区   |
| 266  | 武汉市                 | 湖北省           |
| 267  | 武威市                 | 甘肃省           |
| 268  | 西安市                 | 陕西省           |
| 269  | 西宁市                 | 青海省           |
| 270  | 西双版纳傣族自治州     | 云南省           |
| 271  | 锡林郭勒盟             | 内蒙古自治区     |
| 272  | 厦门市                 | 福建省           |
| 273  | 咸宁市                 | 湖北省           |
| 274  | 咸阳市                 | 陕西省           |
| 275  | 湘潭市                 | 湖南省           |
| 276  | 湘西土家族苗族自治州   | 湖南省           |
| 277  | 襄樊市                 | 湖北省           |
| 278  | 孝感市                 | 湖北省           |
| 279  | 忻州市                 | 山西省           |
| 280  | 新乡市                 | 河南省           |
| 281  | 新余市                 | 江西省           |
| 282  | 信阳市                 | 河南省           |
| 283  | 兴安盟                 | 内蒙古自治区     |
| 284  | 邢台市                 | 河北省           |
| 285  | 徐州市                 | 江苏省           |
| 286  | 许昌市                 | 河南省           |
| 287  | 宣城市                 | 安徽省           |
| 288  | 雅安市                 | 四川省           |
| 289  | 烟台市                 | 山东省           |
| 290  | 延安市                 | 陕西省           |
| 291  | 延边朝鲜族自治州       | 吉林省           |
| 292  | 盐城市                 | 江苏省           |
| 293  | 扬州市                 | 江苏省           |
| 294  | 阳江市                 | 广东省           |
| 295  | 阳泉市                 | 山西省           |
| 296  | 伊春市                 | 黑龙江省         |
| 297  | 伊犁哈萨克自治州       | 新疆维吾尔自治区 |
| 298  | 宜宾市                 | 四川省           |
| 299  | 宜昌市                 | 湖北省           |
| 300  | 宜春市                 | 江西省           |
| 301  | 益阳市                 | 湖南省           |
| 302  | 银川市                 | 宁夏回族自治区   |
| 303  | 鹰潭市                 | 江西省           |
| 304  | 营口市                 | 辽宁省           |
| 305  | 永州市                 | 湖南省           |
| 306  | 榆林市                 | 陕西省           |
| 307  | 玉林市                 | 广西壮族自治区   |
| 308  | 玉树藏族自治州         | 青海省           |
| 309  | 玉溪市                 | 云南省           |
| 310  | 岳阳市                 | 湖南省           |
| 311  | 云浮市                 | 广东省           |
| 312  | 运城市                 | 山西省           |
| 313  | 枣庄市                 | 山东省           |
| 314  | 湛江市                 | 广东省           |
| 315  | 张家界市               | 湖南省           |
| 316  | 张家口市               | 河北省           |
| 317  | 张掖市                 | 甘肃省           |
| 318  | 漳州市                 | 福建省           |
| 319  | 昭通市                 | 云南省           |
| 320  | 肇庆市                 | 广东省           |
| 321  | 镇江市                 | 江苏省           |
| 322  | 郑州市                 | 河南省           |
| 323  | 中山市                 | 广东省           |
| 324  | 中卫市                 | 宁夏回族自治区   |
| 325  | 舟山市                 | 浙江省           |
| 326  | 周口市                 | 河南省           |
| 327  | 株洲市                 | 湖南省           |
| 328  | 珠海市                 | 广东省           |
| 329  | 驻马店市               | 河南省           |
| 330  | 资阳市                 | 四川省           |
| 331  | 淄博市                 | 山东省           |
| 332  | 自贡市                 | 四川省           |
| 333  | 遵义市                 | 贵州省           |
| 334  | 天津市                 |                  |
| 335  | 重庆市                 |                  |
| 336  | 北京市                 |                  |
| 337  | 上海市                 |                  |
