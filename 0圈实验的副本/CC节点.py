import io
import random
import urllib.request as urllib
import zipfile

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.Graph()
G = nx.read_edgelist('0.edges')
#网络中无 0 节点
#print(nx.number_of_nodes(G))
nums = G.number_of_nodes()



Clo_nodes = nx.closeness_centrality(G)
#print(Cen_nodes)
CC_nodes = sorted(Clo_nodes.items(), key = lambda kv:(kv[1]),reverse=1)
print(CC_nodes)
#前五个277,25,322,67,119,56,271,315,21,26，7个
67,271,56,26,322,122,277,25,252,239