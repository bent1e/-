import pandas as pd
import numpy as np

'''
每台售货机2017年每个月的销售额和订单数量
首先转换成时间序列，然后对'支付时间'进行按月分组
最后按月算出订单数量和销售额及环比增长率并保存到data1_1A_Month_Counts.csv文件中
'''
# A售货机
data1_1A = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1A.csv', dtype={'实际金额': np.float16})
data1_1A['月份（A）'] = pd.to_datetime(data1_1A['支付时间'])
dataIndexA = pd.DatetimeIndex(data1_1A['月份（A）'])
# 按月分组
datagroupA = data1_1A[['支付时间', '实际金额']].groupby(by=dataIndexA.month)
# 计算销售额
salecountsA = datagroupA.agg({'实际金额': np.sum})
# 计算订单数量
salecountsA['每月订单数量'] = datagroupA.size()
salecountsA.columns = ['每月销售额', '每月订单数量']
salecountsA['月份'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
salecountsA['环比增长1'] = salecountsA['每月订单数量'].pct_change()
salecountsA.fillna(0, inplace=True)

# 保存为csv文件
salecountsA.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1A_Month_Counts.csv')

# B售货机
data1_1B = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1B.csv', dtype={'实际金额': np.float16})
data1_1B['月份（B）'] = pd.to_datetime(data1_1B['支付时间'])
dataIndexB = pd.DatetimeIndex(data1_1B['月份（B）'])
# 按月分组
datagroupB = data1_1B[['支付时间', '实际金额']].groupby(by=dataIndexB.month)
# 计算销售额
salecountsB = datagroupB.agg({'实际金额': np.sum})
# 计算订单数量
salecountsB['订单数量'] = datagroupB.size()
salecountsB.columns = ['每月销售额', '每月订单数量']
salecountsB['月份'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
salecountsB['环比增长1'] = salecountsB['每月订单数量'].pct_change()
salecountsB.fillna(0, inplace=True)

# 保存为csv文件
salecountsB.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1B_Month_Counts.csv')

# C售货机
data1_1C = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1C.csv', dtype={'实际金额': np.float16})
data1_1C['月份（C）'] = pd.to_datetime(data1_1C['支付时间'])
dataIndexC = pd.DatetimeIndex(data1_1C['月份（C）'])
# 按月分组
datagroupC = data1_1C[['支付时间', '实际金额']].groupby(by=dataIndexC.month)
# 计算销售额
salecountsC = datagroupC.agg({'实际金额': np.sum})
# 计算订单数量
salecountsC['订单数量'] = datagroupC.size()
salecountsC.columns = ['每月销售额', '每月订单数量']
salecountsC['月份'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
salecountsC['环比增长1'] = salecountsC['每月订单数量'].pct_change()
salecountsC.fillna(0, inplace=True)
# 保存为csv文件
salecountsC.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1C_Month_Counts.csv')

# D售货机
data1_1D = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1D.csv', dtype={'实际金额': np.float16})
data1_1D['月份（D）'] = pd.to_datetime(data1_1D['支付时间'])
dataIndexD = pd.DatetimeIndex(data1_1D['月份（D）'])
# 按月分组
datagroupD = data1_1D[['支付时间', '实际金额']].groupby(by=dataIndexD.month)
# 计算销售额
salecountsD = datagroupD.agg({'实际金额': np.sum})
# 计算订单数量
salecountsD['订单数量'] = datagroupD.size()
salecountsD.columns = ['每月销售额', '每月订单数量']
salecountsD['月份'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
salecountsD['环比增长1'] = salecountsD['每月订单数量'].pct_change()
salecountsD.fillna(0, inplace=True)
# 保存为csv文件
salecountsD.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1D_Month_Counts.csv')

# E售货机
data1_1E = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1E.csv', dtype={'实际金额': np.float16})
data1_1E['月份（E）'] = pd.to_datetime(data1_1E['支付时间'])
dataIndexE = pd.DatetimeIndex(data1_1E['月份（E）'])
# 按月分组
datagroupE = data1_1E[['支付时间', '实际金额']].groupby(by=dataIndexE.month)
# 计算销售额
salecountsE = datagroupE.agg({'实际金额': np.sum})
# 计算订单数量
salecountsE['订单数量'] = datagroupE.size()
salecountsE.columns = ['每月销售额', '每月订单数量']
salecountsE['月份'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
salecountsE['环比增长1'] = salecountsE['每月订单数量'].pct_change()
salecountsE.fillna(0, inplace=True)
# 保存为csv文件
salecountsE.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1E_Month_Counts.csv')

# 所有售货机
data1_1 = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/update_data.csv', dtype={'实际金额': np.float16})
data1_1['月份（所有售货机）'] = pd.to_datetime(data1_1['支付时间'])
dataIndex = pd.DatetimeIndex(data1_1['月份（所有售货机）'])
datagroup = data1_1[['支付时间', '实际金额', '订单号']].groupby(by=dataIndex.month)
# 计算月销售额以及每月每单平均交易额

def Average(a):
    s = len(a)/30
    return s

salecounts = datagroup.agg({'实际金额': [np.sum, np.mean], '订单号': Average})
salecounts['订单数量'] = datagroup.size()
salecounts.columns = ['每月销售额', '每月每单平均销售额', '每月日均订单量', '每月订单数量']
salecounts['月份'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
salecounts['环比增长1'] = salecounts['每月订单数量'].pct_change()
salecounts.fillna(0, inplace=True)
salecounts.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1all_Month_counts.csv')
