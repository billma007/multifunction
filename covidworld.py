# 导入库
import tkinter.messagebox
import requests
import json
import pyecharts
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ChartType, _CurrentConfig
from pyecharts.charts import Map, Page
from pyecharts import options as opts


# 自定义header
header = {
    'Host': 'news.qq.com/zt2020/page/feiyan.htm#/global',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400',
}


# 获取json数据
def get_data(url):
    get_data = requests.get(url, header)
    json_data = json.dumps(get_data.json()['data'])
    json_data = json.loads(json_data)
    return json_data
pieces = [
    {'min': 2*(10**7), 'color': '#540d0d'},
    {'max': 2*(10**7)-1,'min': 6*(10**6),'color': '#9c1414'},
    {'max': 6*(10**6)-1, 'min': 1.5*(10**6), 'color': '#d92727'},
    {'max':  1.5*(10**6)-1, 'min':  7*(10**5), 'color': '#ed3232'},
    {'max': 7*(10**5)-1, 'min': 1*(10**5), 'color': '#f27777'},
    {'max': 1*(10**5)-1, 'min': 4*(10**4), 'color': '#f7adad'},
    {'max': 4*(10**4)-1, 'min': 1*(10**4), 'color': '#f7adad'},
    {'max': 1*(10**4)-1, 'color': '#f7e4e4'},
]

# 世界疫情地图
def world_map(data):

    # 国家名
    National_data = []
    # 确诊数据
    num_data = []
    # 治愈数据
    num_data_zy = []
    # 较上日
    day_data = []
    for i in range((len(data))):
        National_data.append(data[i]['name'])
        num_data.append(data[i]['confirm'])
        num_data_zy.append(data[i]['heal'])
        day_data.append(data[i]['confirmAdd'])

    nameMap = {
        'Singapore Rep.': '新加坡',
        'Dominican Rep.': '多米尼加',
        'Palestine': '巴勒斯坦',
        'Bahamas': '巴哈马',
        'Timor-Leste': '东帝汶',
        'Afghanistan': '阿富汗',
        'Guinea-Bissau': '几内亚比绍',
        "Côte d'Ivoire": '科特迪瓦',
        'Siachen Glacier': '锡亚琴冰川',
        "Br. Indian Ocean Ter.": '英属印度洋领土',
        'Angola': '安哥拉',
        'Albania': '阿尔巴尼亚',
        'United Arab Emirates': '阿联酋',
        'Argentina': '阿根廷',
        'Armenia': '亚美尼亚',
        'French Southern and Antarctic Lands': '法属南半球和南极领地',
        'Australia': '澳大利亚',
        'Austria': '奥地利',
        'Azerbaijan': '阿塞拜疆',
        'Burundi': '布隆迪',
        'Belgium': '比利时',
        'Benin': '贝宁',
        'Burkina Faso': '布基纳法索',
        'Bangladesh': '孟加拉国',
        'Bulgaria': '保加利亚',
        'The Bahamas': '巴哈马',
        'Bosnia and Herz.': '波斯尼亚和黑塞哥维那',
        'Belarus': '白俄罗斯',
        'Belize': '伯利兹',
        'Bermuda': '百慕大',
        'Bolivia': '玻利维亚',
        'Brazil': '巴西',
        'Brunei': '文莱',
        'Bhutan': '不丹',
        'Botswana': '博茨瓦纳',
        'Central African Rep.': '中非',
        'Canada': '加拿大',
        'Switzerland': '瑞士',
        'Chile': '智利',
        'China': '中国',
        'Ivory Coast': '象牙海岸',
        'Cameroon': '喀麦隆',
        'Dem. Rep. Congo': '刚果民主共和国',
        'Congo': '刚果',
        'Colombia': '哥伦比亚',
        'Costa Rica': '哥斯达黎加',
        'Cuba': '古巴',
        'N. Cyprus': '北塞浦路斯',
        'Cyprus': '塞浦路斯',
        'Czech Rep.': '捷克',
        'Germany': '德国',
        'Djibouti': '吉布提',
        'Denmark': '丹麦',
        'Algeria': '阿尔及利亚',
        'Ecuador': '厄瓜多尔',
        'Egypt': '埃及',
        'Eritrea': '厄立特里亚',
        'Spain': '西班牙',
        'Estonia': '爱沙尼亚',
        'Ethiopia': '埃塞俄比亚',
        'Finland': '芬兰',
        'Fiji': '斐',
        'Falkland Islands': '福克兰群岛',
        'France': '法国',
        'Gabon': '加蓬',
        'United Kingdom': '英国',
        'Georgia': '格鲁吉亚',
        'Ghana': '加纳',
        'Guinea': '几内亚',
        'Gambia': '冈比亚',
        'Guinea Bissau': '几内亚比绍',
        'Eq. Guinea': '赤道几内亚',
        'Greece': '希腊',
        'Greenland': '格陵兰',
        'Guatemala': '危地马拉',
        'French Guiana': '法属圭亚那',
        'Guyana': '圭亚那',
        'Honduras': '洪都拉斯',
        'Croatia': '克罗地亚',
        'Haiti': '海地',
        'Hungary': '匈牙利',
        'Indonesia': '印度尼西亚',
        'India': '印度',
        'Ireland': '爱尔兰',
        'Iran': '伊朗',
        'Iraq': '伊拉克',
        'Iceland': '冰岛',
        'Israel': '以色列',
        'Italy': '意大利',
        'Jamaica': '牙买加',
        'Jordan': '约旦',
        'Japan': '日本本土',
        'Kazakhstan': '哈萨克斯坦',
        'Kenya': '肯尼亚',
        'Kyrgyzstan': '吉尔吉斯斯坦',
        'Cambodia': '柬埔寨',
        'Korea': '韩国',
        'Kosovo': '科索沃',
        'Kuwait': '科威特',
        'Lao PDR': '老挝',
        'Lebanon': '黎巴嫩',
        'Liberia': '利比里亚',
        'Libya': '利比亚',
        'Sri Lanka': '斯里兰卡',
        'Lesotho': '莱索托',
        'Lithuania': '立陶宛',
        'Luxembourg': '卢森堡',
        'Latvia': '拉脱维亚',
        'Morocco': '摩洛哥',
        'Moldova': '摩尔多瓦',
        'Madagascar': '马达加斯加',
        'Mexico': '墨西哥',
        'Macedonia': '马其顿',
        'Mali': '马里',
        'Myanmar': '缅甸',
        'Montenegro': '黑山',
        'Mongolia': '蒙古',
        'Mozambique': '莫桑比克',
        'Mauritania': '毛里塔尼亚',
        'Malawi': '马拉维',
        'Malaysia': '马来西亚',
        'Namibia': '纳米比亚',
        'New Caledonia': '新喀里多尼亚',
        'Niger': '尼日尔',
        'Nigeria': '尼日利亚',
        'Nicaragua': '尼加拉瓜',
        'Netherlands': '荷兰',
        'Norway': '挪威',
        'Nepal': '尼泊尔',
        'New Zealand': '新西兰',
        'Oman': '阿曼',
        'Pakistan': '巴基斯坦',
        'Panama': '巴拿马',
        'Peru': '秘鲁',
        'Philippines': '菲律宾',
        'Papua New Guinea': '巴布亚新几内亚',
        'Poland': '波兰',
        'Puerto Rico': '波多黎各',
        'Dem. Rep. Korea': '朝鲜',
        'Portugal': '葡萄牙',
        'Paraguay': '巴拉圭',
        'Qatar': '卡塔尔',
        'Romania': '罗马尼亚',
        'Russia': '俄罗斯',
        'Rwanda': '卢旺达',
        'W. Sahara': '西撒哈拉',
        'Saudi Arabia': '沙特阿拉伯',
        'Sudan': '苏丹',
        'S. Sudan': '南苏丹',
        'Senegal': '塞内加尔',
        'Solomon Is.': '所罗门群岛',
        'Sierra Leone': '塞拉利昂',
        'El Salvador': '萨尔瓦多',
        'Somaliland': '索马里兰',
        'Somalia': '索马里',
        'Serbia': '塞尔维亚',
        'Suriname': '苏里南',
        'Slovakia': '斯洛伐克',
        'Slovenia': '斯洛文尼亚',
        'Sweden': '瑞典',
        'Swaziland': '斯威士兰',
        'Syria': '叙利亚',
        'Chad': '乍得',
        'Togo': '多哥',
        'Thailand': '泰国',
        'Tajikistan': '塔吉克斯坦',
        'Turkmenistan': '土库曼斯坦',
        'East Timor': '东帝汶',
        'Trinidad and Tobago': '特里尼达和多巴哥',
        'Tunisia': '突尼斯',
        'Turkey': '土耳其',
        'Tanzania': '坦桑尼亚',
        'Uganda': '乌干达',
        'Ukraine': '乌克兰',
        'Uruguay': '乌拉圭',
        'United States': '美国',
        'Uzbekistan': '乌兹别克斯坦',
        'Venezuela': '委内瑞拉',
        'Vietnam': '越南',
        'Vanuatu': '瓦努阿图',
        'West Bank': '西岸',
        'Yemen': '也门',
        'South Africa': '南非',
        'Zambia': '赞比亚',
        'Zimbabwe': '津巴布韦',
        'Dem.Rep.Congo': '刚果（金）',
        'Congo': '刚果（布）',
        'Central African Rep.': '中非共和国',
        'Sudan': '苏丹',
        'Greenland': '格陵兰岛',
        'Bangladesh': '孟加拉'
    }
    # 国家中文名转为英文
    for a in range(len(National_data)):
        for b in nameMap.keys():
            if National_data[a] == nameMap[b]:
                National_data[a] = b
            else:
                continue
    # 使用zip压缩为元组形式
    qz_data = [tuple(z) for z in zip(National_data, num_data)]
    zy_data = [tuple(z) for z in zip(National_data, num_data_zy)]
    sr_data = [tuple(z) for z in zip(National_data, day_data)]

    data_sum = 0
    data_zy = 0
    for i in range(len(num_data)):
        data_sum += num_data[i]
        data_zy += num_data_zy[i]
    # 副标题
    subtitle = "确诊数量：" + str(data_sum) + "例\n\n治愈数量："+str(data_zy)+"例"
    world_map_data = (
        Map()
        .add(
            "确诊数量",
            qz_data,
            maptype="world",
            is_selected=True,
            is_map_symbol_show=False
        )
        .add(
            "治愈数量",
            zy_data,
            maptype="world",
            is_selected=False,
            is_map_symbol_show=False
        )
        .add(
            "较上日数量",
            sr_data,
            maptype="world",
            is_selected=False,
            is_map_symbol_show=False
        )
        # 系列配置
        .set_series_opts(
            # 不显示经纬度，设置颜色，字体大小
            label_opts={'is_show': 'True',
                        'color': '#fff', 'font_size': '18', 'position': 'left'},
        )
        # 全局配置
        .set_global_opts(
            # 视觉映射配置项
            visualmap_opts=opts.VisualMapOpts(          
                pieces=pieces,
                is_piecewise=True,
                is_show=True),
            # 设置左上角标题和副标题
            title_opts=opts.TitleOpts(
                title="世界疫情地图", subtitle=subtitle, pos_left="50", pos_top="2%", 

                title_textstyle_opts=opts.TextStyleOpts(font_size=30), subtitle_textstyle_opts=opts.TextStyleOpts(font_size=18, color='#222')
            ),
            # 图例设置
            legend_opts=opts.LegendOpts(
                selected_mode='single', pos_top="50", pos_bottom="2%", textstyle_opts=opts.TextStyleOpts(font_size=18)),
        )
        .render("世界疫情地图.html")
    )



def covidworld_main():
    # 世界疫情地图
    QQ_data_url2 = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
    json_data2 = get_data(QQ_data_url2)
    world_map(json_data2)
    tkinter.messagebox.showinfo("成功！","文件已经生成在‘世界疫情地图.html’，请及时查看！")
if __name__=="__name__":
    covidworld_main()