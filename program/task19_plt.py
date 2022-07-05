import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['savefig.dpi'] = 200
plt.rcParams['figure.dpi'] = 150
array = ["A", 'B', "C", "D", "E", "all"]
for k in array:
    data = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/画像数据_年_%s.csv' % (k))
    value = data['订单号'][:30]
    label = data['商品'][:30]
    p1 = plt.figure(figsize=(18, 12))
    explode = [x * 0.02 for x in range(len(label))]
    plt.axes(aspect=1)
    plt.pie(value, labels=label, autopct='%0.1f%%', explode=explode, shadow=False, pctdistance=0.8, startangle=0,
            labeldistance=1.1, radius=1.0, textprops={'fontsize': 20})
    plt.title('2017%s售货机饮料类销售占比饼图'%(k), bbox=dict(facecolor='yellow', edgecolor='red', alpha=0.8), fontsize=25,
              fontweight='bold')  # 添加图表标题
    plt.savefig('C:/Users/Administrator/Desktop/项目数据/可视化/画像饼图_年_%s.png'%(k))
