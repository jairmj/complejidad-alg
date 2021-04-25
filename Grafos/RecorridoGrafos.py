import graphstuff as gs
import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_adjlist('grafo2.txt')
nx.draw(G, with_labels = True)
plt.show()


def bfs(G, s):
    n = G.order()
    visited    = [False]*n
    path       = [None]*n
    queue      = [s]
    visited[s] = True
    while len(queue) > 0:
        u = int(queue[0])
        queue.pop(0)
        for v in G.neighbors(str(u)):
            v = int(v)
            if not visited[v]:
                visited[v] = True
                path[v] = u
                queue.append(v)
    return visited, path


def dfs(G, s, b = True, visited = [], path = []):
    if b:
        n = G.order()
        visited    = [False]*n
        path       = [None]*n
    visited[s] = True
    for v in G.neighbors(str(s)):
        v = int(v)
        if not visited[v]:
            path[v] = s
            path = dfs(G, int(v), False, visited, path)
    return path

path = dfs(G, 3)
print(path)