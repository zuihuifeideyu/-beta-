import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import scipy
import random
from scipy.stats import pearsonr


#jaccard相似系数:交集/并集
def correlation(a,b):
    unions = len(set(a).union(set(b)))
    intersections = len(set(a).intersection(set(b)))
    return 1. * intersections / unions

f = '节点信任值计算.txt'
fn = open(f, 'w')

attrbutes = np.loadtxt('3980.feat', delimiter=' ')
attrbutes1 = np.delete(attrbutes, [0] , axis = 1)
at_node_name = np.loadtxt('3980.feat' , usecols=(0,) , dtype=str)


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
    i_node_name = int(ls_name[i])
    sum = 0
    line_data1 = my_data[i].split()
    for n in range(len(at_node_name)):
        if at_node_name[n] == ls_name[i]:
            at1 = attrbutes1[n]


    for nbr in line_data1:
        nbr_node_name = int(nbr)
        for m in range(len(at_node_name)):
            if at_node_name[m] == nbr:
                at2 = attrbutes1[m]
        s1 = pearsonr(at1, at2)[0]
        for j in range(len(ls_name)):
            if nbr == ls_name[j]:
                line_data2 = my_data[j].split()
                s2 = correlation(line_data1, line_data2)
        sum = sum + s1/2 + s2/2
    p_sum = sum/len(line_data1)
    fn.write(str(i_node_name) + ' ' + str(p_sum))
    fn.write('\n')
fn.close()




'''
i = 0
for node_name in ngr_node_name:
    i_node_name = int(node_name)
    sum = 0
    for nbr in ngr1[i]:
        nbr_node_name = int(nbr)
        s1 = pearsonr(attrbutes1[i_node_name - 1],attrbutes1[nbr_node_name - 1])[0]
        for j in len(ngr_node_name):
            if ngr_node_name[j] == nbr:
                s2 = correlation(ngr1[i], ngr1[j])
        sum = sum + s1 + s2
    sum = sum/len(ngr1[i])
    fn.write(node_name + ' ' + str(sum))
    fn.write('\n')
    i = i + 1
fn.close()
'''
