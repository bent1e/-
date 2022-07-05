import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
array = ["A", 'B', "C", "D", "E"]
for k in array:
        data = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/可视化/%s销量TOP5.csv' % (k), encoding='gbk', dtype={'实际金额': np.float16})
        plt.rcParams['savefig.dpi'] = 200
        plt.rcParams['figure.dpi'] = 150
        p1 = plt.figure(figsize=(16, 12), edgecolor='red', frameon=True, facecolor='green')  # 创建一个空白画布，可以指定大小，像素
        for i in range(0, 16, 5):
                p1_1 = p1.add_subplot(2, 2, (i / 5) + 1)
                values1 = data['订单量'][i:i+5]  # 提取其中的values数组，数据的存在位置
                values2 = data['销售额'][i:i+5]
                label = data['商品'][i:i+5]   # 刻度标签
                my_height1 = values1
                my_height2 = values2
                x = np.arange(5)
                plt.bar(x, my_height1, width=0.4, edgecolor='black', label="订单量", align="center", linewidth=2, color='red')   
                plt.bar(x+0.4, my_height2, width=0.4, edgecolor='black', label="销售额", align="center", linewidth=2, color='deepskyblue')
                plt.legend(fontsize='x-large')
                plt.ylabel('订单量/销售额', fontsize='xx-large')   # 添加y轴名称
                plt.xticks(x+0.4/2, label, rotation=25, fontsize='x-large')
                plt.yticks(fontsize='xx-large')
                plt.title('2017年%s售货机第%d季度销量TOP5柱状图' % (k, (i/5)+1), loc='center', bbox=dict(facecolor='yellow', edgecolor='red', alpha=0.65 ), fontsize='xx-large', fontweight='bold')   # 添加图表标题
                plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                                    wspace=None, hspace=0.5)
                for j in range(0, 5):
                        plt.text(j, my_height1[j+i], my_height1[j+i], va='bottom', ha='center', color='black', fontsize='large', fontweight='bold')
                        plt.text(j+0.4, my_height2[j + i], my_height2[j + i], va='bottom', ha='center', color='black',
                                 fontsize='large')
        plt.savefig('C:/Users/Administrator/Desktop/项目数据/可视化/2017年%s售货机销量TOP5柱状图.png' % (k))

