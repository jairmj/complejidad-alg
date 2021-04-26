import graphstuff as gs
import networkx as nx
import matplotlib.pyplot as plt
import math
import heapq as hq

colors = ['#37AB65', '#3DF735', '#AD6D70', '#EC2504', '#8C0B90', '#C0E4FF', '#27B502', '#7C60A8', '#CF95D7', '#145JKH']

G = nx.DiGraph()
G.add_node(0, label = "undies",  color = colors[0])
G.add_node(1, label = "pants",   color = colors[1])
G.add_node(2, label = "belt",    color = colors[2])
G.add_node(3, label = "shirt",   color = colors[3])
G.add_node(4, label = "tie",     color = colors[4])
G.add_node(5, label = "jacket",  color = colors[5])
G.add_node(6, label = "socks",   color = colors[6])
G.add_node(7, label = "shoes",   color = colors[7])
G.add_node(8, label = "watch",   color = colors[8])

G.add_edges_from([(0, 1), (0, 7),
                 (1, 2), (1, 7),
                 (2,5),
                 (3, 2), (3, 4),
                 (4, 5),
                 (6, 7)])

gs.nx2gv(G, nodeinfo = True).render("test.gv", view = True)

def _dfs(G, u, ts):
    if not G.nodes[u]["visited"]:
        G.nodes[u]["visited"] = True
        for v in G.neighbors(u):
            if not G.nodes[v]["visited"]:
                _dfs(G, v, ts)
        ts.insert(0, G.nodes[u]["label"])
def toposort(G):
    for u in G.nodes():
        G.nodes[u]["visited"] = False
    ts = []
    for u in G.nodes():
        _dfs(G, u, ts)
    return ts

print(toposort(G))