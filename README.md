# multifunction

A python program which can chat with you,search for weather,download videos,change flv into mp4 and translate Chinese/English into English/Chinese.

![ ](https://cdn.jsdelivr.net/gh/billma007/imagesave/mainback.png)

Info:this image:**copyright Billma007 2022**

## language

English/[简体中文](README-Chinese.md)

## How to use?

```git
git clone https://github.com/billma007/multifunction.git
cd multifunction
pip install -r requirements.txt
python main.py
```

Before running main.please go to :`*/python/Lib/site-packages/you-get/common.py`and delete:

```py
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
```

## Module

Thank these selfless maker of the modules

|Module|  |用处|
|------------|------|-----------------------|
pyttsx3      |**2.71**  |播放语音(聊天)     |
pillow       |latest    |数据管理           |
pyperclip    |latest    |复制到剪贴板功能   |
you-get      |latest    |下载视频           |
requests     |latest    |爬虫爬取数据/下载  |
playsound    |**1.2.2** |播放背景音乐       |
pyecharts    |latest    |疫情数据可视化     |
openpyxl     |latest    |疫情数据生成Excel  |
pandas       |latest    |疫情数据整理       |
tqdm         |latest    |下载进度条         |

## How to compile?

```cmd
pip install pyinstaller
pyinstaller --hidden-import=you_get.cli_wrapper --hidden-import=you_get.processor --hidden-import=you_get.utl --hidden-import=you_get.extractors --add-data=".\datasets;pyecharts\datasets\." --add-data=".\templates;pyecharts\render\templates\." -i ico.ico -F -w main.py
```

## Structure

This program is divided into the following parts, each of which already contains an independent warehouse, you can click to go to

- [MAIN](https://github.com/billma007/multifunction)
  - [main.py](main.py) ---make main window
- [Video download](https://github.com/billma007/videodownloadergui)
  - [video.py](video.py) ---download videos
  - ~~[change.py](change.py) ---use ffmpeg~~delete after 1.5.1
- [weacher](https://github.com/billma007/weatherGUI2/)
  - ~~[weather.py](https://github.com/billma007/weatherGUI2/weather.py) ---main~~
  - ~~[Ui_weather.py](https://github.com/billma007/weatherGUI2/Ui_weather.py) ---PyQt5~~
    - delete PyQt5 after 1.2.1
  - [weather_tkinter.py](weather_tkinter.py)
  - [query.py](query.py) ---query
- [chat robot](https://github.com/billma007/mgchatrobot2)
  - [chatmain.py](chatmain.py)
- [translator](https://github.com/billma007/pythontranslator)
  - [translategui.py](translategui.py)
- make icon
  - [icon.py](icon.py) ---make icon automatically
  - [ico.ico](ico.ico) ---icon(**COPYRIGHT**)
- search for the information of covid-19(you can only use it in People's Republic of China)
  - [covid.py](covid.py)
- other
  - [README.md](README.md) ---English doc
  - [README-Chinese.md](README-Chinese.md) ---Chinese Doc
  - [requirements.txt](requirements.txt) ---Requirements
  - [.gitignore](.gitignore) ---.gitignore
  - [LICENSE](LICENSE) ---GNU GPL3.0

## Update log

- 7/1/2021 Start to design chatbot
- 1/21/2022 Start designing chat and translation system
- 2/28/2022 Start design video download and start integration
- 3/12/2022 Add video transcoding function
- 3/16/2022 I found [@RUA](http://2278365235.qzone.qq.com) and drew a~~mascot~~ icon
- 3/17/2022 Made the main page
- 3/18/2022 I have nothing to do and I made a music play. The music is Phigros' curtain call.
- 3/19/2022 Bug fixed
- 3/21/2022 -- 1.1.0:
  - Overturn the original code reconstruction and expand the following functions:
    - 1. Check the weather
    - 2. AI chat
    - 3. Play music
    - 4. Added several buttons
    - 5. Turn on Multithreading
    - 6. Because pyqt5 takes up too much space, I decided to cancel pyqt5 and use Tkinter instead
- 2022/3/22 --  1.2.1:
  - 1. Fixed sys Stdout is not redirected to the text box, resulting in the problem that the progress cannot be displayed
  - 2. Change stdout to `__stdout__` Ensure software security
  - 3. Set `sys.__stderr__` is also redirected to the text box
  - 4. Use `os._exit()` throws an exception to end the software
  - 5. 1.2.1 add automatic update system to div2 (branch version)
    - if you are in Chinese mainland, you will use jsdelivr to accelerate automatically.
- 3/23/2022 --  1.2.2:
  - 1. Refactor the code and start multithreading to prevent jamming
  - 2. Fixed the error reporting of transcoding function
  - 3. Fixed a bug that still plays music after closing the program
  - 4. Fixed the bug of clicking stop music after using a function
  - 5. Code structure change: support multiple functions
  - 6. Fixed the bug that some buttons don't move
  - 7. Due to CDN jsdelivr. He was always drawing air and decided to use fast acceleration. Www. 18fu
- 3/24/2022 --  1.2.3:
  - 1. Fixed the problem that the music couldn't stop due to the suction of playsound function again
  - 2. Who the fuck knows fast jsdelivr. Net is also windy, so I decided to double insurance and take the  maximum value between CDN and fast to keep it updated
  - 3. Optimize and update the system and add CDN lines
  - 4. Fixed the bug that some windows and some buttons activate invalid functions
- 3/24/2022 -- 1.2.3dev1 (Branch) version:
  - 1. Set sys Exit (0) changed to OS_ Exit (0) causes all processes to exit
  - 2. Modify the source code of you get to prevent buffer output cache problems
    - `sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')`
- 3/25/2022 -- 1.2.4:
  - 1. Updated system
  - 2. The MPEG related transcoding function is added
  - 3. Optimized chat system
- March 28, 2022 -- 1.2.5:
  - 1. The transcoding function is cancelled
  - 2. COVID-19 query function has been added.
  - 3. Fixed the bugs of translation, chat and weather query
- March 29, 2022 -- 1.2.5div1 (Branch) :
  - Fixed the problem that pyecarts could not be compiled, and directly put its static resources into the directory and package them together.

## About

A student in Suzhou,People's Republic of China.An OIer.LIKE C++,C and Python.

- QQ:36937975
- Twitter:@billma6688
- Facebook/Instagram:billma007
- CodeForces/USACO/AtCoder:billma007(useless)
- Email:maboning237103015@163.com

## My blog

[Welcome!](https://billma.top)

## LICENSE

[GNU GPL3.0](LICENSE)

**Note**: This software uses the GNU General Public License 3.0 as a whole, but different software licenses are used for each part of this software, please go to each repository for details.
