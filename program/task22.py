import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import statsmodels.api as sm
from statsmodels.tsa import stattools
from statsmodels.tsa import arima_model
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
array = ["A", "B", "C", "D", "E"]
for k in array:
    data = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/预测数据%s.csv' %(k))
    values = data['实际金额']
    label = data['日期']
    p1 = plt.figure(figsize=(10, 10))
    plt.plot(values, linewidth=1, color='red', marker='o', markerfacecolor='black',
             markersize=3, label='销售额')
    plt.xlabel('日期')  # 添加横轴标签
    plt.xticks(range(1, len(label), 30), label[0::30], rotation=30)
    plt.ylabel('销售额/元')  # 添加y轴名称
    plt.title('2017年%s售货机全年销售额折线图' % (k), loc='center',
              bbox=dict(facecolor='yellow', edgecolor='red', alpha=0.8), fontsize='xx-large', fontweight='bold')
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.3, hspace=0.3)
    # p1.savefig('C:/Users/Administrator/Desktop/项目数据/可视化/2017年%s售货机全年销售额折线图.png' % (k))
    plot_acf(values, title='2017年%s售货机全年销售额自相关图'%(k))
    # plt.savefig('C:/Users/Administrator/Desktop/项目数据/可视化/2017年%s售货机全年销售额自相关图.png' % (k))
    # print("%s售货机原始ADF检验："%(k))
    # print(sm.tsa.stattools.adfuller(values))
    values1 = values.diff()[1:]
    # print("%s售货机一阶差分后："%(k))
    # print(sm.tsa.stattools.adfuller(values1))
    plot_acf(values1, title='2017年%s售货机全年销售额一阶差分后自相关图' % (k))
    # plt.savefig('C:/Users/Administrator/Desktop/项目数据/可视化/2017年%s售货机全年销售额一阶差分后自相关图.png' % (k))
    print('BIC求解的模型阶次为', stattools.arma_order_select_ic(values1,max_ma=3))