import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['savefig.dpi'] = 200
plt.rcParams['figure.dpi'] = 150
'''
对每台售货机按照商品进行分类，计算出订单量，并按月和按年保存为画像数据_月_%s.csv和画像数据_年_%s.csv
'''
array = ["A", 'B', "C", "D", "E", "all"]
for k in array:
    data1 = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/附件2.csv')
    data2 = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1%s.csv'%(k))
    data2 = data2[data2['大类'].isin(['饮料'])]
    data2['月份'] = pd.to_datetime(data2['支付时间'])
    dataIndex = pd.DatetimeIndex(data2['月份'])
    group = pd.pivot_table(data2, index=['商品'], columns=dataIndex.month, aggfunc={'订单号': len}, fill_value = 0)
    group1 = pd.pivot_table(data2, index=['商品'], aggfunc={'订单号': len}, fill_value = 0)
    data21 = group
    data22 = group1
    data22.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
    data21.to_csv('C:/Users/Administrator/Desktop/项目数据/画像数据_月_%s.csv'%(k))
    data22.to_csv('C:/Users/Administrator/Desktop/项目数据/画像数据_年_%s.csv' % (k))