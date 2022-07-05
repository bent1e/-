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
    data = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1%s_Season_Counts.csv' %(k))
    plt.rcParams['savefig.dpi'] = 200
    plt.rcParams['figure.dpi'] = 150
    p1.add_subplot(2, 3, array.index(k)+1)
    values1 = data['销售额']
    values2 = data['订单数量']
    plt.plot(values1[0:4], linewidth=3, color='red', marker='o',markerfacecolor='black',
              markersize=6, label='销售额')
    plt.plot(values2[0:4], linewidth=3, color='blue', marker='o', markerfacecolor='black',
              markersize=6, label='订单数量')
    plt.xlabel('季节')  # 添加横轴标签
    plt.ylabel('销售额/元， 订单量/个')  # 添加y轴名称
    plt.xticks(range(4), data['季节'])
    plt.title('2017年%s售货机四季销售额与订单量折线图' % (k), loc='center',
              bbox=dict(facecolor='yellow', edgecolor='red', alpha=0.8), fontsize='large', fontweight='bold')
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.3, hspace=0.3)
    plt.legend(fontsize=10, loc='upper left')

    for j in range(4):
        plt.text(j, values2[j], values2[j], va='bottom', ha='center', color='black', fontsize='small',
                 fontweight='bold', alpha=0.7)
        plt.text(j, values1[j], values1[j], va='bottom', ha='center', color='black', fontsize='small',
                 fontweight='bold', alpha=0.7)

plt.savefig('C:/Users/Administrator/Desktop/项目数据/可视化/2017年售货机四季销售额与订单量折线图.png')
