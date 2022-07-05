import pandas as pd
import numpy as np

# 对每台售货机按照每件商品（大类、二级类）计算出销售额和订单量并保存为data2_2_%.csv

# A
data2_2A = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1A.csv', dtype={'实际金额': np.float16})
datagroupA = pd.pivot_table(data2_2A, index=['商品', '大类', '二级类'], columns=None, aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroupA.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroupA.columns = ['销售额', '订单量']
datagroupA.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_2_A.csv')


# B
data2_2B = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1B.csv', dtype={'实际金额': np.float16})
datagroupB = pd.pivot_table(data2_2B, index=['商品', '大类', '二级类'], columns=None, aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroupB.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroupB.columns = ['销售额', '订单量']
datagroupB.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_2_B.csv')


# C
data2_2C = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1C.csv', dtype={'实际金额': np.float16})
datagroupC = pd.pivot_table(data2_2C, index=['商品', '大类', '二级类'], columns=None, aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroupC.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroupC.columns = ['销售额', '订单量']
datagroupC.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_2_C.csv')


# D
data2_2D = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1D.csv', dtype={'实际金额': np.float16})
datagroupD = pd.pivot_table(data2_2D, index=['商品', '大类', '二级类'], columns=None, aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroupD.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroupD.columns = ['销售额', '订单量']
datagroupD.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_2_D.csv')


# E
data2_2E = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1E.csv', dtype={'实际金额': np.float16})
datagroupE = pd.pivot_table(data2_2E, index=['商品', '大类', '二级类'], columns=None, aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroupE.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroupE.columns = ['销售额', '订单量']
datagroupE.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_2_E.csv')


# All
data2_2 = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/update_data.csv', dtype={'实际金额': np.float16})
datagroup = pd.pivot_table(data2_2, index=['商品', '大类', '二级类'], columns=None, aggfunc={'订单号': len, '实际金额': np.sum}, fill_value = 0)
datagroup.sort_values(by='订单号', axis=0, ascending=False, inplace=True)
datagroup.columns = ['销售额', '订单量']
datagroup.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_2_all.csv')