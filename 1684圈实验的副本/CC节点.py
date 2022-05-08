import io
import random
import urllib.request as urllib
import zipfile

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.Graph()
G = nx.read_edgelist('1684.edges')
#网络中无 0 节点
#print(nx.number_of_nodes(G))
nums = G.number_of_nodes()



Clo_nodes = nx.closeness_centrality(G)
#print(Cen_nodes)
CC_nodes = sorted(Clo_nodes.items(), key = lambda kv:(kv[1]),reverse=1)
print(CC_nodes)
#前五个2863,3274,3117,2946,3302,3101,2787,3214,3342,3291  2个
2839,3363,3101,2754,2944,2966,2742,3320,3397,3291