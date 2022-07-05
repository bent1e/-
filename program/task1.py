import pandas as pd
import numpy as np
# 读取数据
data1 = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/附件1.csv', encoding='gbk')
print(data1.shape)
# 删除重复值
data1.drop_duplicates(subset=['订单号', '支付时间', '商品', '地点'], inplace=True)
print(data1.shape)
# 删除缺失值
data1.dropna(inplace=True)
print(data1.shape)
# 删除异常值，发现在2017/2/29有销售情况，属于错误数据
data1 = data1[~data1['支付时间'].isin(['2017/2/29  3:44:00 PM'])]
# 在附件1中，发现价格为0，0.1的商品所占百分比不足0.5%，与其他商品价格相差过大，所以撇除这部分数据
data1 = data1[~data1['实际金额'].isin(['0.0', '0.1'])]
print(data1.shape)
# 对附件1和附件2进行以商品为主键合并
data2 = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/附件2.csv', encoding='gbk', dtype={'实际金额': np.float16})
data3 = pd.merge(data1, data2, on='商品', how='left')
data3.to_csv('C:/Users/Administrator/Desktop/项目数据/update_data.csv')



