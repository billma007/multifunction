import time
import tkinter as tk
import json
from pyecharts.charts import Map,Page
from pyecharts import options as opts
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def dxy_data_down(article_url="https://ncov.dxy.cn/ncovh5/view/pneumonia"):

    url = urlopen(article_url)
    soup = BeautifulSoup(url, 'html.parser')   # parser解析
    
    return str(soup)
def get_json():

    # 读取本地文件
    f_content = dxy_data_down()    
    # json字符串前后关键词
    json_start = "try { window.getAreaStat = "
    # 字符串包含的括号要进行转义
    json_end = "}catch\(e\){}"
    
    # json字符串正则匹配
    # (.*?)是匹配所有内容
    regular_key = json_start + "(.*?)" + json_end
    # 参数rs.S可以无视换行符，将所有文本视作一个整体进行匹配
    re_content = re.search(regular_key, f_content, re.S)
    # group()用于获取正则匹配后的字符串
    content = re_content.group()
    
    # 去除json字符串的前后关键词
    content = content.replace(json_start, '')
    # 尾巴要去掉转义符号
    json_end = "}catch(e){}"
    content = content.replace(json_end, '')
    

    return content

