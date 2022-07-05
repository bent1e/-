import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.stattools import arma_order_select_ic
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
array = ["B"]
for k in array:
    data = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/预测数据%s饮料.csv' %(k))
    values1 = data['实际金额']
    label = data['日期']
    train = values1[:-20]
    test = values1[-20:]
    model = ARMA(train, (2, 2)).fit()
    # print(model.summary2())  # 给出一份模型报告
    print(model.forecast(20))  # 作为期20天的预测，返回预测结果、标准误差、置信区间。
    forcast = pd.DataFrame(model.forecast(20)[0], index=label[-20:], columns=['forcastsales'])  # 作为期20天的预测，返回预测结果、标准误差、置信区间。
    actual = pd.DataFrame(list(values1[-20:]), index=label[-20:], columns=['actualsales'])
    delta = ((forcast.forcastsales - actual.actualsales) / actual.actualsales).mean() * 200
    print('误差为%0.2f%%' % delta)
    p1 = plt.figure(figsize=(10, 10))
    plt.plot(label[-20:], forcast)
    plt.plot(label[-20:], actual, color='red')
    plt.xlabel('日期')  # 添加横轴标签
    plt.xticks(range(len(label[-20:])), label[-20:], rotation=30)
    plt.ylabel('销售额/元')  # 添加y轴名称
    plt.title('2017年%s售货机最后20天饮料销售额预测值对比图对比图' % (k), loc='center',
              bbox=dict(facecolor='yellow', edgecolor='red', alpha=0.8), fontsize='xx-large', fontweight='bold')
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.3, hspace=0.3)
    p1.savefig('C:/Users/Administrator/Desktop/项目数据/可视化/2017年%s售货机最后20天饮料销售额预测值对比图对比图.png' % (k))