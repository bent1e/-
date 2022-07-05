import pandas as pd
# 将每台售货机对应的销售数据提取出来
data = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/update_data.csv')
data1_1C = data.loc[data['地点']=='C', ['订单号', '实际金额', '商品', '支付时间', '地点', '大类', '二级类']]
data1_1C.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1C.csv')
data1_1B = data.loc[data['地点']=='B', ['订单号', '实际金额', '商品', '支付时间', '地点', '大类', '二级类']]
data1_1B.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1B.csv')
data1_1A = data.loc[data['地点']=='A', ['订单号', '实际金额', '商品', '支付时间', '地点', '大类', '二级类']]
data1_1A.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1A.csv')
data1_1D = data.loc[data['地点']=='D', ['订单号', '实际金额', '商品', '支付时间', '地点', '大类', '二级类']]
data1_1D.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1D.csv')
data1_1E = data.loc[data['地点']=='E', ['订单号', '实际金额', '商品', '支付时间', '地点', '大类', '二级类']]
data1_1E.to_csv('C:/Users/Administrator/Desktop/项目数据/data1_1E.csv')
