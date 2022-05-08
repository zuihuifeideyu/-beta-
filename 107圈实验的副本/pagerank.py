import networkx as nx
import matplotlib.pyplot as plt
import random
import operator

G = nx.Graph()
G = nx.read_edgelist('107.edges')
#nx.draw(G, with_labels=True, node_color="red")
#plt.savefig("./graph.jpg")
#plt.show()

pr = nx.pagerank(G, max_iter=100, alpha=0.01)  # 得到的是字典

print("最大PR值对应的节点：", max(pr.items(), key=operator.itemgetter(1))[0])
#print("100个节点的PR值为：", pr)
pr2 = sorted(pr.items(),  key=lambda d: d[1], reverse=1)
print(pr2)


#前十个483,917,1536,1783,1730,1591,1505,1888,1472,1909  2个
#greedy,
1888,1663,1800,1352,1199,1589,1431,1730,1833,1584