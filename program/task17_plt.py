import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series,DataFrame
import seaborn as sns
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['savefig.dpi'] = 200
plt.rcParams['figure.dpi'] = 150
array = ["A", 'B', "C", "D", "E"]
for k in array:
    '''
    按照月份和天对订单数量进行分类，并保存为data2_8%s.csv
    '''
    data = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1%s.csv'%(k) )
    data['月份'] = pd.to_datetime(data['支付时间'])
    data['天'] = pd.to_datetime(data['支付时间'])
    dataIndex1 = pd.DatetimeIndex(data['月份'])
    dataIndex2 = pd.DatetimeIndex(data['天'])
    data['day'] = data['订单号']
    datagroup = pd.pivot_table(data, index=dataIndex1.month, columns=dataIndex2.day, aggfunc={'day': len}, fill_value=0)
    datagroup.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_8%s.csv'%(k))
    f, ax = plt.subplots(figsize=(9, 6))
    sns.heatmap(datagroup, fmt="d", cmap='YlGnBu', ax=ax, annot=True, linewidths=.5) # annot参数是指显示数据，fmt='d'是指以整数形式显示
    label_y = ax.get_yticklabels()
    plt.setp(label_y, rotation=360, horizontalalignment='right')
    label_x = ax.get_xticklabels()
    plt.setp(label_x, rotation=50, horizontalalignment='right')
    plt.title('2017年%s售货机每天订单量热力图' % (k), bbox=dict(facecolor='yellow', edgecolor='red', alpha=0.7), fontsize=10,
              fontweight='bold')
    plt.savefig('C:/Users/Administrator/Desktop/项目数据/可视化/2017年%s售货机每天订单量热力图.png' % (k))

