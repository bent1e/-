import pandas as pd
import numpy as np

# 四季每台售货机销量前五的
data2_7A = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1A.csv', dtype={'实际金额': np.float16})
data2_7A['月份（A）'] = pd.to_datetime(data2_7A['支付时间'])
dataIndexA = pd.DatetimeIndex(data2_7A['月份（A）'])
datagroupA = pd.pivot_table(data2_7A, index=[dataIndexA.month, '商品', '大类', '二级类'], columns=None, values=['订单号', '实际金额'], aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroupA.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroupA.columns = ['销售额', '订单量']
datagroupA.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_7_A_Month_top5.csv')

data2_7B = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1B.csv', dtype={'实际金额': np.float16})
data2_7B['月份（B）'] = pd.to_datetime(data2_7B['支付时间'])
dataIndexB = pd.DatetimeIndex(data2_7B['月份（B）'])
datagroupB = pd.pivot_table(data2_7B, index=[dataIndexB.month, '商品', '大类', '二级类'], columns=None, values=['订单号', '实际金额'], aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroupB.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroupB.columns = ['销售额', '订单量']
datagroupB.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_7_B_Month_top5.csv')

data2_7C = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1C.csv', dtype={'实际金额': np.float16})
data2_7C['月份（C）'] = pd.to_datetime(data2_7C['支付时间'])
dataIndexC = pd.DatetimeIndex(data2_7C['月份（C）'])
datagroupC = pd.pivot_table(data2_7C, index=[dataIndexC.month, '商品', '大类', '二级类'], columns=None, values=['订单号', '实际金额'], aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroupC.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroupC.columns = ['销售额', '订单量']
datagroupC.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_7_C_Month_top5.csv')

data2_7D = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1D.csv', dtype={'实际金额': np.float16})
data2_7D['月份（D）'] = pd.to_datetime(data2_7D['支付时间'])
dataIndexD = pd.DatetimeIndex(data2_7D['月份（D）'])
datagroupD = pd.pivot_table(data2_7D, index=[dataIndexD.month, '商品', '大类', '二级类'], columns=None, values=['订单号', '实际金额'], aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroupD.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroupD.columns = ['销售额', '订单量']
datagroupD.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_7_D_Month_top5.csv')

data2_7E = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1E.csv', dtype={'实际金额': np.float16})
data2_7E['月份（E）'] = pd.to_datetime(data2_7E['支付时间'])
dataIndexE = pd.DatetimeIndex(data2_7E['月份（E）'])
datagroupE = pd.pivot_table(data2_7E, index=[dataIndexE.month, '商品', '大类', '二级类'], columns=None, values=['订单号', '实际金额'], aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroupE.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroupE.columns = ['销售额', '订单量']
datagroupE.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_7_E_Month_top5.csv')

data2_7 = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/update_data.csv', dtype={'实际金额': np.float16})
data2_7['月份'] = pd.to_datetime(data2_7['支付时间'])
dataIndex = pd.DatetimeIndex(data2_7['月份'])
datagroup = pd.pivot_table(data2_7, index=[dataIndex.month, '商品', '大类', '二级类'], columns=None, values=['订单号', '实际金额'], aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroup.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroup.columns = ['销售额', '订单量']
datagroup.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_7_all_Month_top5.csv')

