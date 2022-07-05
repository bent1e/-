import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['savefig.dpi'] = 200
plt.rcParams['figure.dpi'] = 150
array = ["A", 'B', "C", "D", "E"]
for k in array:
    data = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data2_2_%s.csv'%(k) )
    datagroup = pd.pivot_table(data, index=['二级类','大类'], columns=None,
                                values=['销售额'], aggfunc={'销售额': np.sum}, fill_value=0)
    datagroup = datagroup.sort_values(by=['销售额'], ascending=False)
    value = datagroup['销售额']
    label = datagroup.index
    p1 = plt.figure(figsize=(18, 12))
    explode = [x * 0.02 for x in range(len(label))]
    plt.axes(aspect=1)
    plt.pie(value, labels=label, autopct='%0.1f%%', explode=explode, shadow=False, pctdistance=0.8, startangle=0,
            labeldistance=1.1, radius=1.0, textprops={'fontsize': 20})
    plt.title('2017年%s售货机毛利润占总毛利润比例的饼图'%(k), bbox=dict(facecolor='yellow', edgecolor='red', alpha=0.8), fontsize=25,
              fontweight='bold')  # 添加图表标题
    plt.savefig('C:/Users/Administrator/Desktop/项目数据/可视化/2017年%s售货机毛利润占总毛利润比例的饼图.png'%(k))

