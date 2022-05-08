import io
import random
import urllib.request as urllib
import zipfile

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.Graph()
G = nx.read_edgelist('3980.edges')
#网络中无 0 节点
#print(nx.number_of_nodes(G))
nums = G.number_of_nodes()



Clo_nodes = nx.closeness_centrality(G)
#print(Cen_nodes)
CC_nodes = sorted(Clo_nodes.items(), key = lambda kv:(kv[1]),reverse=1)
print(CC_nodes)
#前五个4023,4030,4014,3998,3982,4004,4020,3994,3997,4038