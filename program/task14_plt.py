import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['savefig.dpi'] = 200
plt.rcParams['figure.dpi'] = 150
data = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/update_data.csv' )
datagroup = pd.pivot_table(data, index=[data['实际金额']], columns=None, values=['实际金额'], aggfunc={'实际金额': len}, fill_value = 0)
datagroup1 = datagroup
datagroup1['金额'] = datagroup1.index
datagroup1.rename(columns={'实际金额': '数量'}, inplace = True)
datagroup1['金额'] = datagroup1.index
datagroup1.to_csv('C:/Users/Administrator/Desktop/项目数据/price_account.csv')
data1 = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/price_account1.csv' )
label = data1['实际金额']
value = data1['数量']
plt.figure(figsize=(8, 7))  # 设置画布
plt.bar(label, value, label="订单数量", align="center", linewidth=2, color='deepskyblue')

plt.xlabel('价格区间', fontsize='large')  # 添加横轴标签
plt.ylabel('订单数量', fontsize='large')  # 添加纵轴标签
'''
plt.xticks([],[]) 第一个：对应X轴上的刻度，第二个：显示的文字
plt.xticks(range(0, 70, 4), values[range(0, 70, 4), 1], rotation=45)
从0开始每隔4个步长（只取第一季度）为一个刻度。0刻度时，刻度的值为values[0, 1]，第一行第二列的值，以此类推
'''
plt.xticks(range(len(label)), label, fontsize='large')
# 45度的倾斜
plt.yticks(fontsize='large')
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.25, hspace=0.3)
plt.title('2017年销售价格区间与销售量关系的直方图', bbox=dict(facecolor='yellow', edgecolor='red', alpha=0.8), fontsize=15, fontweight='bold')  # 添加图表标题
for j in range(4):
    plt.text(j, value[j], value[j], va='bottom', ha='center', color='black', fontsize='large',
             fontweight='bold', alpha=0.8)
plt.legend(fontsize='large')
plt.savefig('C:/Users/Administrator/Desktop/项目数据/可视化/2017年销售价格区间与销售量关系的直方图.png')

