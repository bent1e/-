# -*- coding: utf-8 -*-
# coding: utf-8
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
array = ["A", 'B', "C", "D", "E", "all"]
p1 = plt.figure(figsize=(18, 12))
for k in array:
    data = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1%s_Month_Counts.csv' %(k), dtype={'环比增长1': np.float16, '环比增长2': np.float16})
    plt.rcParams['savefig.dpi'] = 200
    plt.rcParams['figure.dpi'] = 150
    p1.add_subplot(2, 3, array.index(k)+1)
    values1 = data['环比增长1']
    values2 = data['环比增长2']
    x = np.arange(12)
    plt.bar(x, values1, width=0.4, label="订单量环比增长率", align="center", linewidth=1, color='red')
    plt.bar(x+0.4, values2, width=0.4, label="交易额环比增长率", align="center", linewidth=1, color='blue')
    plt.title('2017年%s售货机总销售额与订单量环比增长率柱状图' % (k), loc='center',
              bbox=dict(facecolor='yellow', edgecolor='red', alpha=0.8), fontsize=10, fontweight='bold')
    plt.xlabel('月份/月')  # 添加横轴标签
    plt.ylabel('增长率/100%')
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.25, hspace=0.3)
    plt.legend(fontsize=7, loc='lower right')

    for j in range(12):
        plt.text(j, values1[j], values1[j], va='bottom', ha='center', color='black', fontsize='small',
                 fontweight='bold', alpha=0.8)
plt.savefig('C:/Users/Administrator/Desktop/项目数据/可视化/2017年售货机每月总销售额与订单量环比增长率柱状图.png')
