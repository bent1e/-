import pandas as pd
import numpy as np

# 计算四季每台售货机销量前五的商品并保存为data2_1_%_Season_top5.csv

# A
data2_1A = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1A.csv', dtype={'实际金额': np.float16})
data2_1A['季节（A）'] = pd.to_datetime(data2_1A['支付时间'])
dataIndexA = pd.DatetimeIndex(data2_1A['季节（A）'])
datagroupA = pd.pivot_table(data2_1A, index=[dataIndexA.quarter, '商品', '大类', '二级类'], columns=None, values=['订单号', '实际金额'], aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroupA.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroupA.columns = ['销售额', '订单量']
datagroupA.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_1_A_Season_top5.csv')


# B
data2_1B = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1B.csv', dtype={'实际金额': np.float16})
data2_1B['季节（B）'] = pd.to_datetime(data2_1B['支付时间'])
dataIndexB = pd.DatetimeIndex(data2_1B['季节（B）'])
datagroupB = pd.pivot_table(data2_1B, index=[dataIndexB.quarter, '商品', '大类', '二级类'], columns=None, values=['订单号', '实际金额'], aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroupB.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroupB.columns = ['销售额', '订单量']
datagroupB.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_1_B_Season_top5.csv')


# C
data2_1C = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1C.csv', dtype={'实际金额': np.float16})
data2_1C['季节（C）'] = pd.to_datetime(data2_1C['支付时间'])
dataIndexC = pd.DatetimeIndex(data2_1C['季节（C）'])
datagroupC = pd.pivot_table(data2_1C, index=[dataIndexC.quarter, '商品', '大类', '二级类'], columns=None, values=['订单号', '实际金额'], aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroupC.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroupC.columns = ['销售额', '订单量']
datagroupC.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_1_C_Season_top5.csv')


# D
data2_1D = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1D.csv', dtype={'实际金额': np.float16})
data2_1D['季节（D）'] = pd.to_datetime(data2_1D['支付时间'])
dataIndexD = pd.DatetimeIndex(data2_1D['季节（D）'])
datagroupD = pd.pivot_table(data2_1D, index=[dataIndexD.quarter, '商品', '大类', '二级类'], columns=None, values=['订单号', '实际金额'], aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroupD.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroupD.columns = ['销售额', '订单量']
datagroupD.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_1_D_Season_top5.csv')


# E
data2_1E = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1E.csv', dtype={'实际金额': np.float16})
data2_1E['季节（E）'] = pd.to_datetime(data2_1E['支付时间'])
dataIndexE = pd.DatetimeIndex(data2_1E['季节（E）'])
datagroupE = pd.pivot_table(data2_1E, index=[dataIndexE.quarter, '商品', '大类', '二级类'], columns=None, values=['订单号', '实际金额'], aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroupE.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroupE.columns = ['销售额', '订单量']
datagroupE.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_1_E_Season_top5.csv')


# All
data2_1 = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/update_data.csv', dtype={'实际金额': np.float16})
data2_1['季节'] = pd.to_datetime(data2_1['支付时间'])
dataIndex = pd.DatetimeIndex(data2_1['季节'])
datagroup = pd.pivot_table(data2_1, index=[dataIndex.quarter, '商品', '大类', '二级类'], columns=None, values=['订单号', '实际金额'], aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroup.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroup.columns = ['销售额', '订单量']
datagroup.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_1_all_Season_top5.csv')

