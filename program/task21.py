import numpy as np
import pandas as pd
'''
对每台售货机按2017年每一天进行分类，计算出每天的销售额，并保存为预测数据%s.csv
'''
array = ["A", 'B', "C", "D", "E"]
for k in array:
    data = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1%s.csv' %(k))
    data['日期'] = pd.to_datetime(data['支付时间'])
    dataIndexA = pd.DatetimeIndex(data['日期'])
    group = pd.pivot_table(data, index=dataIndexA.date, values="实际金额", aggfunc={"实际金额": np.sum}, fill_value=0)
    datagroup = group
    datagroup.to_csv('C:/Users/Administrator/Desktop/项目数据/预测数据%s.csv' %(k))