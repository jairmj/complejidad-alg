import graphstuff as gs
import networkx as nx
import matplotlib.pyplot as plt
import math
import heapq as hq

G = nx.read_adjlist('grafo3.txt', create_using = nx.DiGraph, nodetype = int)
v = gs.nx2gv(G)
#v.render('test.gv', view = True)


def _dls(G, u, limit):
    if limit > 0:
        if not G.nodes[u]['visited']:
            print("Nodo visitado: {}".format(u))
            G.nodes[u]['visited'] = True
            for v in G.neighbors(u):
                if not G.nodes[v]['visited']:
                    G.nodes[v]['reached'] = True
                    G.nodes[v]['path'] = u
                    _dls(G, v, limit - 1)

def dls(G, s, limit):
    for u in G.nodes:
        G.nodes[u]['visited'] = False
        G.nodes[u]['path'] = -1

    _dls(G, s, limit)

    path = [0]*G.number_of_nodes()
    for v, info in G.nodes.data():
        path[v] = info['path']
    return path

def ids(G, s, t):
    for u in G.nodes:
        G.nodes[u]['visited'] = False
        G.nodes[u]['reached'] = False
        G.nodes[u]['path'] = -1

    limit = 0
    while not G.nodes[t]['reached']:
        _dls(G, s, limit)
        limit += 1
        if not G.nodes[t]['reached']: #Si no lo encuentra reseteo para volver a hacer la llamada con otro límite
            for u in G.nodes:
                G.nodes[u]['visited'] = False
                G.nodes[u]['reached'] = False
                G.nodes[u]['path'] = -1


    path = [0]*G.number_of_nodes()
    for v, info in G.nodes.data():
        path[v] = info['path']
    return path


# path = dls(G, 3, 400)
# print(path)
# gs.path2gv(path).render('test.gv', view = True)

path = ids(G, 3, 12)
print(path)
gs.path2gv(path, params = {'rankdir' : 'LR', 'size' : '5'}).render('test.gv', view = True)


