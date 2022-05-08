import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import scipy
import random
from scipy.stats import pearsonr

tr = np.loadtxt('修正后节点信任值.txt', delimiter=' ')
ls_tr = tr.tolist()
#print(ls_tr)
tr1 = sorted(ls_tr, key = (lambda x: float(x[1])), reverse = 1)
print(tr1)


tr2 = np.delete(tr, [0] , axis = 1)
sum = 0
for i in range(len(tr2)):
    sum = sum + float(tr2[i])
p_sum = sum/len(tr2)
print(p_sum)

#p_sum = 0.01535816335483148

#2839,3363,3101,2944,2754,2966,3026,2669,2877,2755