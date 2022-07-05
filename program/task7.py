import pandas as pd
import numpy as np

# 对每台售货机所售商品的价格区间计算出所处价格区间的订单量，并保存为data2_3%.csv

# A
data2_3A = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1A.csv', dtype={'实际金额': np.float16})
datagroupA = pd.pivot_table(data2_3A, index=['实际金额'], columns=None, aggfunc={'订单号': len})
datagroupA.columns = ['销售量']
datagroupA.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_3A.csv')
# B
data2_3B = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1B.csv', dtype={'实际金额': np.float16})
datagroupB = pd.pivot_table(data2_3B, index=['实际金额'], columns=None, aggfunc={'订单号': len})
datagroupB.columns = ['销售量']
datagroupB.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_3B.csv')
# C
data2_3C = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1C.csv', dtype={'实际金额': np.float16})
datagroupC = pd.pivot_table(data2_3C, index=['实际金额'], columns=None, aggfunc={'订单号': len})
datagroupC.columns = ['销售量']
datagroupC.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_3C.csv')
# D
data2_3D = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1D.csv', dtype={'实际金额': np.float16})
datagroupD = pd.pivot_table(data2_3D, index=['实际金额'], columns=None, aggfunc={'订单号': len})
datagroupD.columns = ['销售量']
datagroupD.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_3D.csv')
# E
data2_3E = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/data1_1E.csv', dtype={'实际金额': np.float16})
datagroupE = pd.pivot_table(data2_3E, index=['实际金额'], columns=None, aggfunc={'订单号': len})
datagroupE.columns = ['销售量']
datagroupE.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_3E.csv')
# All
data2_3 = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/update_data.csv', dtype={'实际金额': np.float16})
datagroup = pd.pivot_table(data2_3, index=['实际金额'], columns=None, aggfunc={'订单号': len})
datagroup.columns = ['销售量']
datagroup.to_csv('C:/Users/Administrator/Desktop/项目数据/data2_3_all.csv')