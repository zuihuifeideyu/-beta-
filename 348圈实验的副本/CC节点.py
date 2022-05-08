import io
import random
import urllib.request as urllib
import zipfile

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.Graph()
G = nx.read_edgelist('348.edges')
#网络中无 0 节点
#print(nx.number_of_nodes(G))
nums = G.number_of_nodes()



Clo_nodes = nx.closeness_centrality(G)
#print(Cen_nodes)
CC_nodes = sorted(Clo_nodes.items(), key = lambda kv:(kv[1]),reverse=1)
print(CC_nodes)
#前五个376,475,412,563,428,373,497,513,561,525,7个
376,475,373,559,517,497,483,412,513,428