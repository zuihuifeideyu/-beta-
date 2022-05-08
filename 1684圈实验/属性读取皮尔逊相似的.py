import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import scipy
import random
from scipy.stats import pearsonr


#读取属性值
attrbutes = np.loadtxt('0.feat',delimiter=' ')
print(attrbutes[0])
dataset = np.loadtxt('0.feat',delimiter=' ')
print(dataset)
dataset1 = np.delete(dataset, [0] , axis = 1)

s = pearsonr(dataset1[0],dataset1[2])[0]

print(s)


#读取第一列：节点名称
node_name = np.loadtxt('0.feat' , usecols=(0,) , dtype=str)
print(node_name)

#也可以考虑用汉明距离