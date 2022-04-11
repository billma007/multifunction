import json
from covidgetjson import get_json
def get_provinces(json_content=get_json()):

    # 将字符串转化为字典
    json_data = json.loads(json_content)
    
    data = []
    
    # 省份数据展示
    for i in json_data:
        # 省份名称处理，和地图对应
        province_name = i["provinceName"]
        if(len(province_name)>1):
            if(province_name[-1] == "省"):
                province_name = province_name[:-1]
            if(province_name[-1] == "市"):
                province_name = province_name[:-1]
        if(len(province_name)>3):
            if(province_name[-3:] == "自治区"):
                province_name = province_name[:-3]
        if(len(province_name)>3):
            if(province_name[-3:] == "维吾尔"):
                province_name = province_name[:-3]
        if(len(province_name)>2):
            if(province_name[-2:] == "壮族"):
                province_name = province_name[:-2]
            if(province_name[-2:] == "回族"):
                province_name = province_name[:-2]
        
        data.append((province_name, i["currentConfirmedCount"]))
         
        
    return data

from pyecharts import options as opts
from pyecharts.charts import Map

pieces = [
    {'min': 10000, 'color': '#540d0d'},
    {'max': 9999, 'min': 1000, 'color': '#9c1414'},
    {'max': 999, 'min': 500, 'color': '#d92727'},
    {'max': 499, 'min': 100, 'color': '#ed3232'},
    {'max': 99, 'min': 10, 'color': '#f27777'},
    {'max': 9, 'min': 1, 'color': '#f7adad'},
    {'max': 0, 'color': '#f7e4e4'},
]

def create_china_map():
    return (
        Map()
        .add(
            series_name="现存确诊", 
            data_pair=get_provinces(), 
            maptype="china", 
            # 是否默认选中，默认为True
            is_selected=True,
            # 是否启用鼠标滚轮缩放和拖动平移，默认为True
            is_roam=True,
            # 是否显示图形标记，默认为True
            is_map_symbol_show=False
        )
        # 系列配置项
        # 关闭标签名称显示
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        # 全局配置项
        .set_global_opts(
            # 设置标题
            title_opts=opts.TitleOpts(title="马哥多功能工具：中国现存确诊地图"),
            # 设置视觉配置项分段显示
            visualmap_opts=opts.VisualMapOpts(
                pieces=pieces,
                is_piecewise=True,
                is_show=True
            )
        )
        # 生成本地html文件
    )
    pass