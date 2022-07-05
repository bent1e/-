import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['savefig.dpi'] = 200
plt.rcParams['figure.dpi'] = 150
'''
data1 = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/附件2.csv')
data2 = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1A.csv')
data2['月份'] = pd.to_datetime(data2['支付时间'])
dataIndex = pd.DatetimeIndex(data2['月份'])
group = pd.pivot_table(data2, index=[dataIndex.month, '二级类'], columns=None, values=['实际金额','大类','商品'], aggfunc={'实际金额': np.sum}, fill_value = 0)
data22 = group
data22.to_csv('C:/Users/Administrator/Desktop/项目数据/气泡图数据A.csv')

'''
array = ["A", 'B', "C", "D", "E"]
for k in array:
    data22 = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/气泡图数据%s.csv' %(k))


    x = data22['月份']#X轴数据

    y = data22['二级类']#Y轴数据

    z = data22['实际金额']#用来调整各个点的大小s


    fig, ax = plt.subplots(figsize = (14, 12))
    cm = plt.cm.get_cmap('RdYlBu')
    bubble = ax.scatter(x, y, s=(z - np.min(z) + 0.1) * 2, c=z, cmap = cm, linewidth=0.5, alpha=0.8)
    ax.grid()
    fig.colorbar(bubble)
    plt.yticks(fontsize='large')
    ax.set_xlabel('月份', fontsize = 15)#X轴标签

    ax.set_title('2017年%s售货机每月交易额气泡图'%(k), bbox=dict(facecolor='yellow', edgecolor='red', alpha=0.8), fontsize=20, fontweight='bold')  # 添加图表标题
    plt.savefig('C:/Users/Administrator/Desktop/项目数据/可视化/2017年%s售货机每月交易额气泡图.png' %(k))



