# 实现KNN算法
# 距离样本点最近的k个已知样本中类别最多的那一类将是预测结果
import numpy as np
import matplotlib.pyplot as plt 

def createDataSet():
    #四组二维特征
    group = np.array([[1,101],[5,89],[108,5],[115,8]])
    #四组特征的标签
    labels = ['爱情片','爱情片','动作片','动作片']
    return group, labels

group ,lables=createDataSet()
# for i in range(len(group)):
#     print(group[i])
#     print(lables[i])
# print(group.shape)

k=5    #k值需要是奇数
# print(type(group[1]))
x=np.empty([group.shape[0],group.shape[1]])  #样本点初始化
# 样本点随机赋值s
for i in range(group.shape[0]):
    for k in range(group.shape[1]):
        x[i][k]=np.random.randint(0,200)
plt.xlabel('X')
plt.ylabel('Y')
colors1 = '#00CED1' # 点的颜色
colors2 = '#DC143C'

# 展示点图
plt.scatter(group[:,0],group[:,1], c=colors1,label='test')

plt.plot([0,100],[0,100],linewidth = '0.5',color='#000000')   #划线
plt.legend()
plt.show()
print(group)