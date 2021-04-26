import graphstuff as gs
import networkx as nx
import matplotlib.pyplot as plt
import math
import heapq as hq

G = nx.read_adjlist('grafo2.txt')
nx.draw(G, with_labels = True)
plt.show()


def ucs(G, s):
    for u in G.nodes:
        G.nodes[u]['visited'] = False
        G.nodes[u]['path'] = -1
        G.nodes[u]['cost'] = math.inf

    G.node[s]['cost'] = 0
    queue = []
    hq.heappush(queue, (0, s)) # Cola pero ordenada :O

    while queue: #Mientras haya algo en la cola
        g, u = hp.heappop(queue)
        if G.nodes[u]['visited']: continue
        G.nodes[u]['visited'] = True
        for v in G.neighbors(str(u)):
            if not G.nodes[v]['visited']:
                w = G.edge[(u, v)]['weight']
                f = g + w
                if f < G.nodes[v]['cost']:
                    G.nodes[v]['cost'] = f
                    G.nodes[v]['path'] = u
                    hq.heappush(queue, (f, v))
    wPath = [(0, 0)]*G.number_of_nodes()
    for v, info in G.nodes.data():
        wPath[v] = (info['path'], info['cost'])
    return wPath