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


G = nx.Graph()
G = nx.read_edgelist('0.edges')
Nodes = list(nx.nodes(G))
print(nx.number_of_nodes(G))
print(Nodes)

'''
#计算还有相似度

nbr = list(G.neighbors(Nodes[0]))
print(nbr)
nbr1 = list(G.neighbors(nbr[0]))
print(nbr1)
s = correlation(nbr, nbr1)
print(s)
'''


f = '邻居节点汇总.txt'
fn = open(f, 'w')
for node in Nodes:
    nbr = list(G.neighbors(node))
    #fn.write(str(node) + ' ')
    length = len(nbr)
    for nbr1 in nbr:
        if nbr1 != nbr[length-1]:
            fn.write(str(nbr1) + ' ')
        else:
            fn.write(str(nbr1))
    fn.write('\n')
fn.close()
