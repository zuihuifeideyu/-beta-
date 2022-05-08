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

attrbutes = np.loadtxt('0.feat', delimiter=' ')
attrbutes1 = np.delete(attrbutes, [0] , axis = 1)
at_node_name = np.loadtxt('0.feat' , usecols=(0,) , dtype=str)


ls_name = ['236', '186', '122', '285', '24', '346', '271', '304', '176', '9', '130', '329', '204', '213', '252', '332', '82', '65', '276', '26', '280', '272', '211', '199', '84', '133', '62', '239', '172', '322', '53', '3', '170', '175', '46', '56', '254', '194', '231', '117', '127', '135', '103', '188', '23', '116', '73', '299', '288', '315', '119', '323', '48', '57', '200', '98', '313', '63', '344', '67', '118', '325', '277', '134', '270', '76', '36', '223', '274', '88', '21', '339', '108', '197', '169', '275', '273', '83', '28', '312', '242', '214', '20', '307', '71', '333', '207', '168', '308', '341', '128', '334', '238', '265', '141', '78', '345', '317', '158', '38', '302', '27', '54', '139', '109', '291', '142', '203', '105', '232', '64', '217', '248', '126', '224', '261', '283', '144', '226', '290', '25', '342', '146', '300', '94', '1', '184', '159', '149', '13', '59', '17', '326', '80', '187', '161', '66', '31', '136', '7', '255', '49', '320', '85', '246', '123', '284', '140', '137', '343', '115', '297', '185', '104', '324', '171', '111', '14', '310', '32', '30', '222', '92', '72', '40', '125', '266', '212', '278', '340', '237', '311', '309', '330', '230', '70', '16', '249', '39', '251', '10', '55', '228', '69', '113', '258', '257', '196', '156', '303', '286', '81', '174', '293', '33', '42', '347', '2', '281', '263', '279', '51', '338', '162', '19', '75', '218', '268', '314', '5', '178', '192', '243', '195', '181', '8', '245', '129', '328', '331', '150', '101', '99', '296', '102', '318', '163', '173', '165', '121', '306', '177', '180', '87', '189', '60', '259', '45', '58', '269', '167', '227', '96', '91', '143', '61', '93', '41', '235', '6', '89', '107', '79', '208', '132', '221', '301', '250', '106', '29', '337', '100', '110', '264', '225', '86', '152', '148', '295', '201', '289', '260', '160', '321', '68', '131', '22', '298', '262', '220', '234', '44', '50', '193', '97', '124', '112', '90', '179', '216', '151', '145', '157', '4', '327', '95', '120', '247', '190', '282', '244', '319', '233', '256', '166', '202', '155', '191', '147', '206', '229', '138', '164', '240', '77', '219', '305', '153', '154', '198', '182', '336', '241', '294', '253', '267', '316', '205', '47', '183', '52', '34', '35']

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
    for nbr in line_data1:
        nbr_node_name = int(nbr)
        s1 = pearsonr(attrbutes1[i_node_name - 1], attrbutes1[nbr_node_name - 1])[0]
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
