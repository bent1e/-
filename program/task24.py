import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.arima_model import ARMA
import numpy as np
from statsmodels.tsa.stattools import arma_order_select_ic
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
array = ["A", "B", "C", "D", "E"]
for k in array:
    data = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/预测数据%s.csv' %(k))
    values1 = data['实际金额']
    label = data['日期']
    model = ARMA(values1, (0, 1)).fit().forecast(30)
    # print(model.summary2())  # 给出一份模型报告
    print("%s的预测值："%(k), model[0].sum())  # 作为期30天的预测，返回预测结果、标准误差、置信区间。
    np.savetxt('C:/Users/Administrator/Desktop/项目数据/预测值%s.csv'%(k), model[0],delimiter=',')