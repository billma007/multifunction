# multifunction

A python program which can chat with you,search for weather,download videos,change flv into mp4 and translate Chinese/English into English/Chinese.

![ ](https://cdn.jsdelivr.net/gh/billma007/imagesave/mainback.png)

## language

English/[简体中文](README-Chinese.md)

## How to use?

```git
git clone https://github.com/billma007/multifunction.git
cd multifunction
pip install -r requirements.txt
python main.py
```

## How to compile?

```cmd
pip install pyinstaller
pyinstaller main.spec
```

## Structure

This program is divided into the following parts, each of which already contains an independent warehouse, you can click to go to

- [MAIN](https://github.com/billma007/videodownloadergui)
  - [main.py](main.py) ---make main window
  - [main.spec](main.spec) ---pyinstaller,you can [click to learn more](https://github.com/billma007/videodownloadergui#how-to-compile)
  - [gobackmain.py](gobackmain.py) ---go back to main window
- [Video download](https://github.com/billma007/videodownloadergui)
  - [video.py](video.py) ---download videos
  - [change.py](change.py) ---use ffmpeg
- [weacher](https://github.com/billma007/weatherGUI2)
  - [weather.py](weather.py) ---main
  - [Ui_weather.py](Ui_weather.py) ---PyQt5
  - [query.py](query.py) ---query
- [chat robot](https://github.com/billma007/mgchatrobot2)
  - [chatmain.py](chatmain.py)
- [translator](https://github.com/billma007/pythontranslator)
  - [translategui.py](translategui.py)
- make icon
  - [icon.py](icon.py) ---make icon automatically
  - [ico.ico](ico.ico) ---icon(**COPYRIGHT**)
- other
  - [README.md](README.md) ---English doc
  - [README-Chinese.md](README-Chinese.md) ---Chinese Doc
  - [requirements.txt](requirements.txt) ---Requirements
  - [.gitignore](.gitignore) ---.gitignore
  - [LICENSE](LICENSE) ---GNU GPL3.0

## Update log

- 2021/7/1 Start to design chatbot
- 2022/1/21 Start designing chat and translation system
- 2022/2/28 Start design video download and start integration
- 2022/3/12 Add video transcoding function
- 2022/3/16 I found [@RUA](http://2278365235.qzone.qq.com) and drew a~~mascot~~ icon
- 2022/3/17 Made the main page
- 2022/3/18 I have nothing to do and I made a music play. The music is Phigros' curtain call.
- 2022/3/19 Bug fixed

## About

A student in Suzhou,People's Republic of China.An OIer.LIKE C++,C and Python.

- QQ:36937975
- Twitter:@billma007cool
- Facebook/Instagram:billma007
- CodeForces/USACO/AtCoder:billma007(useless)
- Email:maboning237103015@163.com

## My blog

[Welcome!](https://billma.top)

## LICENSE

[GNU GPL3.0](LICENSE)

**Note**: This software uses the GNU General Public License 3.0 as a whole, but different software licenses are used for each part of this software, please go to each repository for details.
