import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import scipy
import random
from scipy.stats import pearsonr

#全局信任节点
f = '修正后节点信任值.txt'
fn = open(f, 'w')

#初始平均信任度计算
tr = np.loadtxt('节点信任值计算.txt', delimiter=' ')
tr1 = np.delete(tr, [0] , axis = 1)
tr_node_name = np.loadtxt('节点信任值计算.txt' , usecols=(0,) , dtype=str)
#print(tr1)
#print(tr_node_name)
sum = 0.0
for i in tr1:
    sum = sum + float(i)
p_sum = sum/len(tr1)
print(p_sum)

'''
ls_name = ['4038', '4014', '4032', '4027', '4019', '4026', '4023', '4003', '4018', '3997', '4031', '4021', '3998', '4013', '4004', '4030', '3988', '3982', '4002', '4037', '4020', '3995', '3993', '3986', '4017', '3983', '3994', '3999', '4005', '4009', '3991', '3989', '4011', '3992', '3981', '4000', '3985', '594', '3996', '4029', '4001', '4025', '4016', '4034', '3990', '4036', '4033', '4007', '4028', '4012', '3987', '4006']

with open('邻居节点汇总.txt', 'r') as f:
    my_data = f.readlines() #txt中所有字符串读入data，得到的是一个list
    # 对list中的数据做分隔和类型转换
#    print(my_data)
#    for line in my_data:
#       line_data = line.split()
#       print (line_data)
print(len(my_data))

for i in range(len(ls_name)):
    line_data = my_data[i].split()
    nbr_nodes_number = len(line_data)
    s = float(tr1[i])*nbr_nodes_number/52
    fn.write(ls_name[i]+' '+str(s))
    fn.write('\n')
fn.close()
'''


