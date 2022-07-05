import pandas as pd
import numpy as np
'''
每台售货机2017年每个季节的销售额和订单数量
首先转换成时间序列，然后对'支付时间'进行按季节分组
最后按月算出订单数量和销售额并保存到data1_1%s_Season_Counts.csv文件中
'''
# A售货机
data1_1A = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1A.csv', dtype={'实际金额': np.float16})
data1_1A['季节'] = pd.to_datetime(data1_1A['支付时间'])
dataIndexA = pd.DatetimeIndex(data1_1A['季节'])
# 按月分组
datagroupA = data1_1A[['支付时间', '实际金额']].groupby(by=dataIndexA.quarter)
# 计算销售额
salecountsA = datagroupA.agg({'实际金额': np.sum})
salecountsA.columns = ['销售额']
# 计算订单数量
salecountsA['订单数量'] = datagroupA.size()
salecountsA.loc['总和'] = salecountsA.apply(lambda x: x.sum())
# 保存为csv文件
salecountsA.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1A_Season_Counts.csv')

# B售货机
data1_1B = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1B.csv', dtype={'实际金额': np.float16})
data1_1B['季节'] = pd.to_datetime(data1_1B['支付时间'])
dataIndexB = pd.DatetimeIndex(data1_1B['季节'])
# 按月分组
datagroupB = data1_1B[['支付时间', '实际金额']].groupby(by=dataIndexB.quarter)
# 计算销售额
salecountsB = datagroupB.agg({'实际金额': np.sum})
salecountsB.columns = ['销售额']
# 计算订单数量
salecountsB['订单数量'] = datagroupB.size()
salecountsB.loc['总和'] = salecountsB.apply(lambda x: x.sum())
# 保存为csv文件
salecountsB.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1B_Season_Counts.csv')

# C售货机
data1_1C = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1C.csv', dtype={'实际金额': np.float16})
data1_1C['季节'] = pd.to_datetime(data1_1C['支付时间'])
dataIndexC = pd.DatetimeIndex(data1_1C['季节'])
# 按月分组
datagroupC = data1_1C[['支付时间', '实际金额']].groupby(by=dataIndexC.quarter)
# 计算销售额
salecountsC = datagroupC.agg({'实际金额': np.sum})
salecountsC.columns = ['销售额']
# 计算订单数量
salecountsC['订单数量'] = datagroupC.size()
salecountsC.loc['总和'] = salecountsC.apply(lambda x: x.sum())
# 保存为csv文件
salecountsC.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1C_Season_Counts.csv')

# D售货机
data1_1D = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1D.csv', dtype={'实际金额': np.float16})
data1_1D['季节'] = pd.to_datetime(data1_1D['支付时间'])
dataIndexD = pd.DatetimeIndex(data1_1D['季节'])
# 按月分组
datagroupD = data1_1D[['支付时间', '实际金额']].groupby(by=dataIndexD.quarter)
# 计算销售额
salecountsD = datagroupD.agg({'实际金额': np.sum})
salecountsD.columns = ['销售额']
# 计算订单数量
salecountsD['订单数量'] = datagroupD.size()
salecountsD.loc['总和'] = salecountsD.apply(lambda x: x.sum())
# 保存为csv文件
salecountsD.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1D_Season_Counts.csv')

# E售货机
data1_1E = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1E.csv', dtype={'实际金额': np.float16})
data1_1E['季节'] = pd.to_datetime(data1_1E['支付时间'])
dataIndexE = pd.DatetimeIndex(data1_1E['季节'])
# 按月分组
datagroupE = data1_1E[['支付时间', '实际金额']].groupby(by=dataIndexE.quarter)
# 计算销售额
salecountsE = datagroupE.agg({'实际金额': np.sum})
salecountsE.columns = ['销售额']
# 计算订单数量
salecountsE['订单数量'] = datagroupE.size()
salecountsE.loc['总和'] = salecountsE.sum()
# 保存为csv文件
salecountsE.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1E_Season_Counts.csv')

# 所有售货机
data1_1 = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/update_data.csv', dtype={'实际金额': np.float16})
data1_1['季节'] = pd.to_datetime(data1_1['支付时间'])
dataIndex = pd.DatetimeIndex(data1_1['季节'])
datagroup = data1_1[['支付时间', '实际金额']].groupby(by=dataIndex.quarter)
salecounts = datagroup.agg({'实际金额': np.sum})
salecounts.columns = ['销售额']
salecounts['订单数量'] = datagroup.size()
salecounts.loc['总和'] = salecounts.apply(lambda x: x.sum())
salecounts.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1_all_Season_Counts.csv')