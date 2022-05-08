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

#p_sum = 0.053269844223856125

#1888,1663,1833,1589,1199,1800,1352,1613,1612,1707