import io
import random
import urllib.request as urllib
import zipfile

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.Graph()
G = nx.read_edgelist('107.edges')
#网络中无 0 节点
#print(nx.number_of_nodes(G))
nums = G.number_of_nodes()



Clo_nodes = nx.closeness_centrality(G)
#print(Cen_nodes)
CC_nodes = sorted(Clo_nodes.items(), key = lambda kv:(kv[1]),reverse=1)
print(CC_nodes)
#前五个1086,1584,1800,1334,483,917,1746,1620,1352,1730  4个
1888,1663,1800,1352,1199,1589,1431,1730,1833,1584