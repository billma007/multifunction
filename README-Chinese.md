# multifunction

一个可以中英互译，聊天，查天气，下载视频，转码视频/图片/音频的软件

![ ](https://cdn.jsdelivr.net/gh/billma007/imagesave/mainback.png)

## 如何使用?

```git
git clone https://github.com/billma007/multifunction.git
cd multifunction
pip install -r requirements.txt
python main.py
```

## 如何安装？

```cmd
pip install pyinstaller
pyinstaller main.spec
```

## 结构架次

本程序分为以下部分，期中各个部分都已经含有独立的仓库，可点击前往

- [主函数](https://github.com/billma007/videodownloadergui)
  - [main.py](main.py) ---主窗口生成
  - [main.spec](main.spec) ---pyinstaller文件，详情[点击这里](https://github.com/billma007/videodownloadergui#how-to-compile)
  - [gobackmain.py](gobackmain.py) ---从各个子窗口返回主窗口
- [视频播放与转码](https://github.com/billma007/videodownloadergui)
  - [video.py](video.py) ---下载视频
  - [change.py](change.py) ---视频、图片、音频转码
- [天气查询](https://github.com/billma007/weatherGUI2)
  - [weather.py](weather.py) ---主文件
  - [Ui_weather.py](Ui_weather.py) ---PyQt5窗口
  - [query.py](query.py) ---数据处理
- [聊天系统](https://github.com/billma007/mgchatrobot2)
  - [chatmain.py](chatmain.py)
- [翻译系统](https://github.com/billma007/pythontranslator)
  - [translategui.py](translategui.py)
- 生成图标
  - [icon.py](icon.py) ---通过base64进行编码自动生成图标
  - [ico.ico](ico.ico) ---图标{版权所有}
- 其他
  - [README.md](README.md) ---英文文档
  - [README-Chinese.md](README-Chinese.md) ---中文文档
  - [requirements.txt](requirements.txt) ---依赖库
  - [.gitignore](.gitignore) ---.gitignore
  - [LICENSE](LICENSE) ---GNU通用公共许可3.0（GNU/GPL3.0）

## 更新日志

- 2021/7/1 开始设计聊天机器人
- 2022/1/21 开始设计聊天、翻译系统
- 2022/2/28 开始设计视频下载并开始整合
- 2022/3/12 增加视频转码功能
- 2022/3/16 找了[@RUA](http://2278365235.qzone.qq.com)画了个~~吉祥物~~图标
- 2022/3/17 把主页面做出来了
- 2022/3/18 ~~上课摸鱼~~闲来无事做了个音乐播放，音乐是~~阴游~~音游Phigros的谢幕曲。
- 2022/3/19 修复了bug

## 关于作者

江苏省苏州市的一个普通高中牲，一个因为~~玩电脑被学校处分~~在省赛就被刷下来的信息学奥林匹克竞赛选手，热爱编程，但不喜欢前端。

欢迎通过以下联系方式与我探讨信息竞赛、博客搭建、学术讨论以及扯皮：

- QQ:36937975
- Twitter:@billma6688
- Facebook/Instagram:billma007
- CodeForces/USACO/AtCoder:billma007(~~别看我很拉的~~不常用)
- Email:maboning237103015@163.com

## 推广：我的博客

[欢迎光临！](https://billma.top)

## 许可证

[GNU通用公共许可3.0（GNU/GPL3.0)](LICENSE)

**注意**：本软件整体使用GNU通用公共许可3.0，但是本软件的各个部分使用不同的软件许可证，详情请前往各个仓库。