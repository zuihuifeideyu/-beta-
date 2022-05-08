import networkx as nx
import matplotlib.pyplot as plt
import random
import operator

G = nx.Graph()
G = nx.read_edgelist('0.edges')
nx.draw(G, with_labels=True, node_color="red")
#plt.savefig("./graph.jpg")
plt.show()

pr = nx.pagerank(G, max_iter=100, alpha=0.01)  # 得到的是字典

print("最大PR值对应的节点：", max(pr.items(), key=operator.itemgetter(1))[0])
print("100个节点的PR值为：", pr)
pr2 = sorted(pr.items(),  key=lambda d: d[1], reverse=1)
print(pr2)


#前十个25,23,119,322,56,312,277,19,239,230，5个
#greedy,
67,271,56,26,322,122,277,25,252,239
