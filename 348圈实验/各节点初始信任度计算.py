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

attrbutes = np.loadtxt('348.feat', delimiter=' ')
attrbutes1 = np.delete(attrbutes, [0] , axis = 1)
at_node_name = np.loadtxt('348.feat' , usecols=(0,) , dtype=str)


ls_name = ['436', '428', '450', '531', '538', '404', '565', '412', '471', '461', '544', '414', '465', '546', '547', '475', '446', '536', '398', '367', '452', '560', '493', '361', '359', '402', '520', '567', '542', '510', '521', '559', '557', '376', '555', '500', '469', '516', '378', '482', '418', '506', '514', '545', '525', '484', '492', '479', '373', '483', '173', '549', '460', '517', '395', '370', '396', '416', '368', '503', '423', '457', '477', '524', '364', '441', '400', '548', '515', '434', '496', '382', '474', '451', '409', '526', '363', '371', '420', '432', '448', '563', '508', '440', '444', '523', '561', '365', '507', '397', '439', '497', '513', '387', '408', '512', '394', '419', '527', '443', '453', '403', '504', '422', '413', '495', '553', '458', '426', '540', '470', '519', '511', '556', '558', '372', '392', '445', '417', '566', '353', '490', '464', '552', '488', '374', '476', '533', '355', '463', '388', '438', '442', '375', '491', '354', '543', '456', '455', '366', '467', '572', '539', '424', '537', '391', '425', '360', '421', '430', '427', '407', '357', '568', '405', '473', '431', '350', '369', '466', '429', '551', '381', '410', '486', '459', '487', '569', '494', '481', '502', '570', '362', '198', '399', '352', '489', '389', '501', '564', '454', '351', '435', '437', '528', '518', '380', '390', '462', '532', '498', '509', '554', '449', '541', '415', '571', '480', '468', '406', '505', '433', '478', '349', '535', '385', '534', '562', '529', '522', '485', '34', '356', '411', '384', '393', '530', '472', '386', '499', '379', '401', '377', '383']

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
