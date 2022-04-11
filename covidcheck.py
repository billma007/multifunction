import time
import tkinter as tk
import json
from tkinter import messagebox
import covidpyecharts1,covidpyecharts2 
from covidgetjson import get_json
from pyecharts.charts import Page
import requests
def createcovidtoplevel():
    covid=tk.Toplevel()
    covid.iconbitmap('ico.ico')
    kkk=tk.StringVar()
    covid.geometry('500x310')
    covid.title="疫情查询和下载"
    tk.Label(covid,text="请输入你要查询的省份(要加“省市自治区”字样)").pack()
    a=tk.Entry(covid,textvariable=kkk)
    a.pack()
    tk.Button(covid,text="查询",command=lambda:Parse_data2(kkk.get())).pack()
    tk.Button(covid,text="全国疫情形势(数据+地图)",command=lambda:display_provinces()).pack()
    tk.Label(covid,text="众志成城，共克时艰！",font=("等线",11),fg="red").pack()
    tk.Label(covid,text="数据来源：国内数据来自中华人民共和国国家卫生与健康委员会\n由于卫健委api格式在不停变化，该功能可能会失效\n绘制出的可视化地图非官方制图，请勿用于商业用途\n软件及绘制出的图像由BillMa007版权所有").pack()
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
        data1 = Down_data()
        list1 = ['截至时间：'+str(data1['lastUpdateTime'])+'\n'
              '全国确诊人数：'+str(data1['chinaTotal']['confirm'])+'\n'
              '今日新增确诊：'+str(data1['chinaAdd']['confirm'])+'\n'
              '全国疑似：'+str(data1['chinaTotal']['suspect'])+'\n'
              '今日新增疑似：'+str(data1['chinaAdd']['suspect'])+'\n'
]
        result = ''.join(list1)
        data = Down_data()['areaTree'][0]['children']
        with open(str(time.strftime("%Y年%m月%d日  %H时%M分%S秒", time.localtime()))+'疫情查询数据.txt', 'a+',  encoding="utf-8") as f:
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

def display_provinces(json_content=get_json()):
    # 将字符串转化为字典
    json_data = json.loads(json_content)
    with open(time.strftime('%Y年%m月%d日 %I时%M分%S秒疫情查询数据.txt' , time.localtime()),'w',encoding='utf-8') as f:
    # 省份数据展示
        f.write("截至您的计算机本地时间"+time.strftime('%Y年%m月%d日%I时%M分%S秒,' , time.localtime())+"全国各省份疫情数据如下：+'\n'")
        for i in json_data:
            f.write("【省份名】：" + i["provinceName"]+'\n')
            f.write("现存确诊：" + str(i["currentConfirmedCount"])+'\n')
            f.write("累计确诊：" + str(i["confirmedCount"])+'\n')
            f.write("死亡：" + str(i["deadCount"])+'\n')
            f.write("治愈：" + str(i["curedCount"])+'\n')
        f.close()
    aaa=covidpyecharts1.create_china_map()
    bbb=covidpyecharts2.create_china_map()
    page = Page(layout=Page.DraggablePageLayout,page_title="马哥多功能工具：全国疫情形势图")
    page.add(
        aaa,bbb
    )
    # 先生成render.html文件
    messagebox.showinfo("查询成功！","全国数据已经保存至Excel表格，可视化地图已经保存至render.html，请及时查看！\n请注意，数据并非实时更新，而是各地卫健委实时上报的数据")
    page.render('全国疫情形势图.html')
import json

def display_citys( province_name,json_content=get_json()):
    with open(time.strftime('%Y年%m月%d日 %I时%M分%S秒疫情查询数据.txt' , time.localtime()),'w',encoding='utf-8') as f:
    # 将字符串转化为字典
        json_data = json.loads(json_content)

        # 省份数据展示
        f.write(time.strftime('截至您的计算机本地时间%Y年%m月%d日 %I时%M分%S秒，' , time.localtime())+province_name + "疫情数据如下：\n")
        for i in json_data:
            # print(i)
            if(i["provinceName"] == province_name):
                # 读取里面的城市信息
                try:
                    citys = i["cities"]
                    for ii in citys:
                        f.write("【城市名】：" + ii["cityName"]+'\n')
                        f.write("现存确诊：" + str(ii ["currentConfirmedCount"])+'\n')
                        f.write("累计确诊：" + str(ii["confirmedCount"])+'\n')
                        f.write("死亡：" + str(ii["deadCount"])+'\n')
                        f.write("治愈：" + str(ii["curedCount"])+'\n')
                except Exception as e:
                    f.write(e)
                    f.write("没有相应的城市信息!")
        f.close()



if __name__=="__main__":
    createcovidtoplevel()