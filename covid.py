
import tkinter as tk
import requests
from lxml import etree
import json
import openpyxl
import pandas as pd
from pyecharts.charts import Map,Page
from pyecharts import options as opts
import time
from tkinter import messagebox
def createcovidtoplevel():
    covid=tk.Toplevel()
    kkk=tk.StringVar()
    covid.geometry('500x210')
    covid.title="疫情查询和下载"
    tk.Label(covid,text="请输入你要查询的省份(不要加“省市自治区”字样)").pack()
    tk.Entry(covid,textvariable=kkk).pack()
    tk.Button(covid,text="查询",command=lambda:Parse_data2(kkk.get())).pack()
    tk.Button(covid,text="全国疫情形势可视化和数据化",command=covidpyecharts).pack()
    tk.Label(covid,text="众志成城，共克时艰！",font=("等线",11),fg="red").pack()
    tk.Label(covid,text="数据来源：中华人民共和国国家卫生与健康委员会\n由于卫健委api格式在不停变化，该功能可能会失效\n绘制出的可视化地图非官方制图，请勿用于商业用途\n软件及绘制出的图像由BillMa007版权所有").pack()
    covid.mainloop()
def Down_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'
    }
    r = requests.get(url, headers)
    res = json.loads(r.text)
    data_res = json.loads(res['data'])
    return data_res
        
 
def Parse_data2(path):
    try:
        data1 = Down_data()
        list1 = ['截至时间：'+str(data1['lastUpdateTime'])+'\n'
              '全国确诊人数：'+str(data1['chinaTotal']['confirm'])+'\n'
              '今日新增确诊：'+str(data1['chinaAdd']['confirm'])+'\n'
              '全国疑似：'+str(data1['chinaTotal']['suspect'])+'\n'
              '今日新增疑似：'+str(data1['chinaAdd']['suspect'])+'\n'
]
        result = ''.join(list1)
        data = Down_data()['areaTree'][0]['children']
        with open(str(time.strftime("%Y-%m-%d  %H：%M：%S", time.localtime()))+'疫情查询.txt', 'a+',  encoding="utf-8") as f:
            f.write(result + '\n')
            for i in data:
                if path in i['name']:
                    for item in i['children']:
                        list_city = [
                            '地区: '+str(item['name'])+'  ',
                            ' 确诊人数：' + str(item['total']['confirm']) ,
                            ' 新增确诊：' + str(item['today']['confirm'])+"\n"]
                        res_city = ''.join(list_city)
                        f.write(res_city)
            f.close()
        messagebox.showinfo("查询成功！","查询结果已经保存至本软件同一目录下，请及时查看！")
    except Exception as eeeeee:
        messagebox.showerror("发生错误","发生错误：\n"+eeeeee)
def covidpyecharts():
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5     Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/    78.0.3904.108 Mobile Safari/537.36'
        }
        nowtime=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())    )
        #通用爬虫
        url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia'
        data1=Down_data()
        response = requests.get(url=url,headers=headers).text
        #在使用xpath的时候要用树形态
        html = etree.HTML(response)
        #用xpath来获取我们之前找到的页面json数据  并打印看看
        json_text = html.xpath('//script[@type="application/json"]/text ()')
        json_text = json_text[0]
        #用python本地自带的库转换一下json数据
        result = json.loads(json_text)
        print(result)
        #通过打印出转换的对象我们可以看到我们要的数据都要key为component对   应5 的值之下  所以现在我们将值拿出来
        result = result["component"]
        #再次打印看看结果
        result = result[0]['caseList']
        #创建工作簿
        wb = openpyxl.Workbook()

        ws = wb.active

        ws.title = "国内疫情数据表格"

        ws.append(["省份","累计确诊","死亡","治愈"])
        #获取各省份的数据并写入
        for line in result:
            line_name = [line["area"],line["confirmed"],line["died"],   line["crued"]]
            for ele in line_name:
                if ele == '':
                    ele = 0
            ws.append(line_name)
        #保存到excel中
        wb.save(ws.title+'.xlsx')
        randertitle="截至"+nowtime+"国内疫情数据可视化地图"
        # 设置列对齐
        pd.set_option('display.unicode.ambiguous_as_wide', True)
        pd.set_option('display.unicode.east_asian_width', True)
        # 打开文件
        df = pd.read_excel(ws.title+'.xlsx')
        # 对省份进行统计
        data2 = df['省份']
        data2_list = list(data2)
        data3 = df['累计确诊']
        data3_list = list(data3)
        data4 = df['死亡']
        data4_list = list(data4)
        data5 = df ['治愈']
        data5_list = list(data5)

        a = (
            Map()
                .add("累计确诊", [list(z) for z in zip(data2_list,  data3_list)], "china")
                .set_global_opts(
                title_opts=opts.TitleOpts(title="全国各省确诊患者(不含无症状感染者)"),
                visualmap_opts=opts.VisualMapOpts(max_=3000),
            )
        )

        b = (
            Map()
                .add("死亡", [list(z) for z in zip(data2_list,  data4_list)], "china")
                .set_global_opts(
                title_opts=opts.TitleOpts(title="全国各省积累死亡患者"),
                visualmap_opts=opts.VisualMapOpts(max_=10),
            )
        )

        c = (
            Map()
                .add("治愈", [list(z) for z in zip(data2_list,  data5_list)], "china")
                .set_global_opts(
                title_opts=opts.TitleOpts(title="全国各省积累治愈患者"),
                visualmap_opts=opts.VisualMapOpts(max_=2000),
            )
        )

        page = Page(layout=Page.DraggablePageLayout,page_title="马哥多功能工具：全国疫情形势图")
        page.add(
            a,
            b,
            c,
        )
        # 先生成render.html文件
        messagebox.showinfo("查询成功！","全国数据已经保存至Excel表格，可视化地图已经保存至render.html，请及时查看！\n请注意，数据并非实时更新，而是各地卫健委实时上报的数据")
    except Exception as ee:
        messagebox.showerror("发生错误","发生错误：\n"+ee)
    page.render()
def checkmain():
    try:
        Down_data()
        Parse_data2()
    except Exception as eeeee:
       messagebox.showerror("发生错误","发生了错误：\n"+eeeee)
if __name__=="__main__":
    createcovidtoplevel()