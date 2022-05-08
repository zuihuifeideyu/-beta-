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


max_iter_num = 10  # 模拟的次数

tr = np.loadtxt('节点信任值计算.txt', delimiter=' ')
ls_tr = tr.tolist()



'''
Cen_nodes = nx.degree_centrality(G)
#print(Cen_nodes)
DC_nodes = sorted(Cen_nodes.items(), key = lambda kv:(kv[1]),reverse=1)
print(DC_nodes)
#前五个2839,3363,2754,3101,3291,3082,2742,3397,3426,3320  8个



Bet_nodes = nx.betweenness_centrality(G)
BC_nodes = sorted(Bet_nodes.items(), key = lambda kv:(kv[1]),reverse=1)
print(BC_nodes)
#前五个2754,2863,2946,3117,3105,2738,3168,3263,3274,2729  1个
'''
#2839,3363,3101,2754,2944,2966,2742,3320,3397,3291

ls1 = [2839,3363,3101,2754,2944]
ls2 = [2839,3363,2754,3101,3291]
ls3 = [2754,2863,2946,3117,3105]
ls4 = [2863,3077,171,2951,3256]
ls5 = [2863,3274,3117,2946,3302]

list1 = [str(i) for i in ls1]
list2 = [str(i) for i in ls2]
list3 = [str(i) for i in ls3]
list4 = [str(i) for i in ls4]
list5 = [str(i) for i in ls5]





#SI实验
alpha = 0.32  # 传染概率
beta = 0.65  # 治愈概率


# TS实验

for node in G:
    G.add_node(node, state=0)  # 用state标识状态 state=0 易感 ，state=1 感染 ， state=2 治愈

for node in list1:
    G.nodes[node]['state'] = 1

all_infect_nodes1 = []  # 所有被感染的节点放在这里
for node in list1:
    all_infect_nodes1.append(node)

all_remove_nodes1 = []  # 所有被治愈的节点放在这里

infect1 = []  # 随着迭代次数的增加的感染总人数
recover1 = []  # 随着迭代次数的增加的治愈总人数

for i in range(max_iter_num):
    new_infect1 = list()  # 新被感染的
    new_remove1 = list()  # 新被治愈的
    # t1 = '%s time' % i + ' %s nodes' % len(all_infect_nodes)
    # print('当前感染节点数：', t1) # 当前有多少个节点被感染
    # t2 = '%s time' % i + ' %s nodes' % len(all_remove_nodes)
    # print('治愈节点数：', t2)
    infect1.append(len(all_infect_nodes1))
    recover1.append(len(all_remove_nodes1))

    # 感染的机会不止一次
    # 治愈后不会被感染
    for v in all_infect_nodes1:

        for j in range(len(ls_tr)):
            if int(v) == ls_tr[j][0]:
                t = float(ls_tr[j][1])

        for nbr in G.neighbors(v):  # v的邻居

            if G.nodes[nbr]['state'] == 0:  # 如果这个邻居节点没被感染且没有被治愈

                if alpha < t:
                    G.nodes[nbr]['state'] = 1
                    new_infect1.append(nbr)

    for i in new_remove1:
        if i in new_infect1:
            new_infect1.remove(i)
        if i in all_infect_nodes1:
            all_infect_nodes1.remove(i)

    all_infect_nodes1.extend(new_infect1)  # 将新感染的添加到
    all_remove_nodes1.extend(new_remove1)
    all_infect_nodes1 = list(set(all_infect_nodes1))  # 去重
    all_remove_nodes1 = list(set(all_remove_nodes1))

# 度中心性实验
for edge in G.edges:
    G.add_edge(edge[0], edge[1], weight=random.uniform(0, 1))  # 可不可以作为权值 病毒的感染能力
for node in G:
    G.add_node(node, state=0)  # 用state标识状态 state=0 易感 ，state=1 感染 ， state=2 治愈

for node in list2:
    G.nodes[node]['state'] = 1

all_infect_nodes2 = []  # 所有被感染的节点放在这里
for node in list2:
    all_infect_nodes2.append(node)

all_remove_nodes2 = []  # 所有被治愈的节点放在这里

infect2 = []  # 随着迭代次数的增加的感染总人数
recover2 = []  # 随着迭代次数的增加的治愈总人数

for i in range(max_iter_num):
    new_infect2 = list()  # 新被感染的
    new_remove2 = list()  # 新被治愈的
    # t1 = '%s time' % i + ' %s nodes' % len(all_infect_nodes)
    # print('当前感染节点数：', t1) # 当前有多少个节点被感染
    # t2 = '%s time' % i + ' %s nodes' % len(all_remove_nodes)
    # print('治愈节点数：', t2)
    infect2.append(len(all_infect_nodes2))
    recover2.append(len(all_remove_nodes2))

    # 感染的机会不止一次
    # 治愈后不会被感染
    for v in all_infect_nodes2:
        for j in range(len(ls_tr)):
            if int(v) == ls_tr[j][0]:
                t = float(ls_tr[j][1])

        for nbr in G.neighbors(v):  # v的邻居

            if G.nodes[nbr]['state'] == 0:  # 如果这个邻居节点没被感染且没有被治愈

                if alpha < t:
                    G.nodes[nbr]['state'] = 1
                    new_infect2.append(nbr)

    for i in new_remove2:
        if i in new_infect2:
            new_infect2.remove(i)
        if i in all_infect_nodes2:
            all_infect_nodes2.remove(i)

    all_infect_nodes2.extend(new_infect2)  # 将新感染的添加到
    all_remove_nodes2.extend(new_remove2)
    all_infect_nodes2 = list(set(all_infect_nodes2))  # 去重
    all_remove_nodes2 = list(set(all_remove_nodes2))

# 介数中心性实验
for edge in G.edges:
    G.add_edge(edge[0], edge[1], weight=random.uniform(0, 1))  # 可不可以作为权值 病毒的感染能力
for node in G:
    G.add_node(node, state=0)  # 用state标识状态 state=0 易感 ，state=1 感染 ， state=2 治愈

for node in list3:
    G.nodes[node]['state'] = 1

all_infect_nodes3 = []  # 所有被感染的节点放在这里
for node in list3:
    all_infect_nodes3.append(node)

all_remove_nodes3 = []  # 所有被治愈的节点放在这里

infect3 = []  # 随着迭代次数的增加的感染总人数
recover3 = []  # 随着迭代次数的增加的治愈总人数

for i in range(max_iter_num):
    new_infect3 = list()  # 新被感染的
    new_remove3 = list()  # 新被治愈的
    # t1 = '%s time' % i + ' %s nodes' % len(all_infect_nodes)
    # print('当前感染节点数：', t1) # 当前有多少个节点被感染
    # t2 = '%s time' % i + ' %s nodes' % len(all_remove_nodes)
    # print('治愈节点数：', t2)
    infect3.append(len(all_infect_nodes3))
    recover3.append(len(all_remove_nodes3))

    # 感染的机会不止一次
    # 治愈后不会被感染
    for v in all_infect_nodes3:
        for j in range(len(ls_tr)):
            if int(v) == ls_tr[j][0]:
                t = float(ls_tr[j][1])

        for nbr in G.neighbors(v):  # v的邻居

            if G.nodes[nbr]['state'] == 0:  # 如果这个邻居节点没被感染且没有被治愈

                if alpha < t:
                    G.nodes[nbr]['state'] = 1
                    new_infect3.append(nbr)

    for i in new_remove3:
        if i in new_infect3:
            new_infect3.remove(i)
        if i in all_infect_nodes3:
            all_infect_nodes3.remove(i)

    all_infect_nodes3.extend(new_infect3)  # 将新感染的添加到
    all_remove_nodes3.extend(new_remove3)
    all_infect_nodes3 = list(set(all_infect_nodes3))  # 去重
    all_remove_nodes3 = list(set(all_remove_nodes3))

# pagerank实验
for edge in G.edges:
    G.add_edge(edge[0], edge[1], weight=random.uniform(0, 1))  # 可不可以作为权值 病毒的感染能力
for node in G:
    G.add_node(node, state=0)  # 用state标识状态 state=0 易感 ，state=1 感染 ， state=2 治愈

for node in list4:
    G.nodes[node]['state'] = 1

all_infect_nodes4 = []  # 所有被感染的节点放在这里
for node in list4:
    all_infect_nodes4.append(node)

all_remove_nodes4 = []  # 所有被治愈的节点放在这里

infect4 = []  # 随着迭代次数的增加的感染总人数
recover4 = []  # 随着迭代次数的增加的治愈总人数

for i in range(max_iter_num):
    new_infect4 = list()  # 新被感染的
    new_remove4 = list()  # 新被治愈的
    # t1 = '%s time' % i + ' %s nodes' % len(all_infect_nodes)
    # print('当前感染节点数：', t1) # 当前有多少个节点被感染
    # t2 = '%s time' % i + ' %s nodes' % len(all_remove_nodes)
    # print('治愈节点数：', t2)
    infect4.append(len(all_infect_nodes4))
    recover4.append(len(all_remove_nodes4))

    # 感染的机会不止一次
    # 治愈后不会被感染
    for v in all_infect_nodes4:
        for j in range(len(ls_tr)):
            if int(v) == ls_tr[j][0]:
                t = float(ls_tr[j][1])

        for nbr in G.neighbors(v):  # v的邻居

            if G.nodes[nbr]['state'] == 0:  # 如果这个邻居节点没被感染且没有被治愈

                if alpha < t:
                    G.nodes[nbr]['state'] = 1
                    new_infect4.append(nbr)

    for i in new_remove4:
        if i in new_infect4:
            new_infect4.remove(i)
        if i in all_infect_nodes4:
            all_infect_nodes4.remove(i)

    all_infect_nodes4.extend(new_infect4)  # 将新感染的添加到
    all_remove_nodes4.extend(new_remove4)
    all_infect_nodes4 = list(set(all_infect_nodes4))  # 去重
    all_remove_nodes4 = list(set(all_remove_nodes4))

# 紧密度中心性实验
for edge in G.edges:
    G.add_edge(edge[0], edge[1], weight=random.uniform(0, 1))  # 可不可以作为权值 病毒的感染能力
for node in G:
    G.add_node(node, state=0)  # 用state标识状态 state=0 易感 ，state=1 感染 ， state=2 治愈

for node in list5:
    G.nodes[node]['state'] = 1

all_infect_nodes5 = []  # 所有被感染的节点放在这里
for node in list5:
    all_infect_nodes5.append(node)

all_remove_nodes5 = []  # 所有被治愈的节点放在这里

infect5 = []  # 随着迭代次数的增加的感染总人数
recover5 = []  # 随着迭代次数的增加的治愈总人数

for i in range(max_iter_num):
    new_infect5 = list()  # 新被感染的
    new_remove5 = list()  # 新被治愈的
    # t1 = '%s time' % i + ' %s nodes' % len(all_infect_nodes)
    # print('当前感染节点数：', t1) # 当前有多少个节点被感染
    # t2 = '%s time' % i + ' %s nodes' % len(all_remove_nodes)
    # print('治愈节点数：', t2)
    infect5.append(len(all_infect_nodes5))
    recover5.append(len(all_remove_nodes5))

    # 感染的机会不止一次
    # 治愈后不会被感染
    for v in all_infect_nodes5:
        for j in range(len(ls_tr)):
            if int(v) == ls_tr[j][0]:
                t = float(ls_tr[j][1])

        for nbr in G.neighbors(v):  # v的邻居

            if G.nodes[nbr]['state'] == 0:  # 如果这个邻居节点没被感染且没有被治愈

                if alpha < t:
                    G.nodes[nbr]['state'] = 1
                    new_infect5.append(nbr)

    for i in new_remove5:
        if i in new_infect5:
            new_infect5.remove(i)
        if i in all_infect_nodes5:
            all_infect_nodes5.remove(i)

    all_infect_nodes5.extend(new_infect5)  # 将新感染的添加到
    all_remove_nodes5.extend(new_remove5)
    all_infect_nodes5 = list(set(all_infect_nodes5))  # 去重
    all_remove_nodes5 = list(set(all_remove_nodes5))

# matplotlib中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # aaaaa.py 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）


def draw_picture(nums, max_iter_num, infect1, recover1, infect2, recover2, infect3, recover3, infect4, recover4,
                 infect5, recover5):
    x = range(max_iter_num)
    susceptible = []
    #    for i in range(max_iter_num):
    #        susceptible.append(nums - infect1[i] - recover1[i])

    plt.figure(figsize=(5, 4), dpi=150)  # 图片大小，清晰度

    plt.plot(x, infect2, color='k', lw=0.5, marker='.', linestyle='--', label='DC')
    plt.plot(x, infect3, color='k', lw=0.5, marker='^', linestyle='-.', label='BC')
    plt.plot(x, infect4, color='k', lw=0.5, marker='x', linestyle='-.', label='PR')
    plt.plot(x, infect5, color='k', lw=0.5, marker='*', linestyle='-.', label='CC')
    plt.plot(x, infect1, color='k', label='GTM', lw=0.5, marker='D', linestyle='-')
    #    plt.title('infections')
    # plt.plot(x, recover, color='b', label='治愈数')  # 可以修改颜色、线条风格、图例
    # plt.plot(x, susceptible, color='g', label='易感数')

    plt.legend(loc='lower right')  # 显示图例

    plt.xticks(range(0, max_iter_num, 2))  # 修改x的刻度
    plt.yticks(range(0, nums, 100))  # 修改y的刻度

    # 添加网格显示
    plt.grid(True, linestyle='', alpha=0.5)

    # 添加x，y轴描述信息及标题
    plt.ylabel('Infected nodes')
    plt.xlabel('Timestamps')

    #    # plt.title('对比')
    plt.savefig("./1684对比graph.jpg")
    plt.show()



draw_picture(nums, max_iter_num, infect1, recover1, infect2, recover2, infect3, recover3, infect4, recover4, infect5,
             recover5)

