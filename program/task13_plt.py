import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
data = pd.read_csv('C:/Users/Administrator/Desktop/项目数据/利润.csv')
value = data['毛利润']
label = data['售货机']
explode = [0.01, 0.01, 0.01, 0.01, 0.01]
plt.title('每台售货机毛利润占总毛利润比例饼图', bbox=dict(facecolor='yellow', edgecolor='red', alpha=0.8), fontsize=9,
              fontweight='bold')
plt.pie(value, labels=label, autopct='%0.1f%%', explode=explode, shadow=False, pctdistance=0.8, startangle=90, labeldistance=1.1, radius=1.2)

plt.savefig('C:/Users/Administrator/Desktop/项目数据/可视化/2017每台售货机毛利润占总毛利润比例饼图.png')




