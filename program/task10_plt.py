import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
array = ["A", 'B', "C", "D", "E", "all"]
p1 = plt.figure(figsize=(18, 12))
for k in array:
    data = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1%s_Month_Counts.csv' % (k), dtype={'实际金额': np.float16})
    plt.rcParams['savefig.dpi'] = 200
    plt.rcParams['figure.dpi'] = 150
    p1.add_subplot(2, 3, array.index(k)+1)
    values1 = data['每月销售额']
    values2 = data['每月订单数量']
    plt.plot(values1[:], linewidth=3,color='r', marker='o',
        markerfacecolor='blue', markersize=7, label='总销售额')
    plt.plot(values2[:], linewidth=3, color='yellow', marker='o',
             markerfacecolor='blue', markersize=7, label='总订单量')
    plt.legend(fontsize=10)
    plt.xlabel('月份/月')  # 添加横轴标签
    plt.ylabel('销售额/元， 订单量/个')  # 添加y轴名称
    plt.xticks(range(12), data['月份'])
    plt.title('2017年%s售货机总销售额与订单量折线图' % (k), loc='center',
             bbox=dict(facecolor='yellow', edgecolor='red', alpha=0.8), fontsize='large', fontweight='bold')
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.25, hspace=0.3)
    for j in range(12):
        plt.text(j, values1[j], values1[j], va='bottom', ha='center', color='black', fontsize='small',
                 fontweight='bold', alpha=0.8)
        plt.text(j, values2[j], values2[j], va='bottom', ha='center', color='black', fontsize='small',
                 fontweight='bold', alpha=0.7)
plt.savefig('C:/Users/Administrator/Desktop/项目数据/可视化/2017年售货机每月总销售额与订单量折线图.png')
