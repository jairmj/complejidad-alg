# Generar una matriz aleatoria de adyacencia para G
# Generar una lista aleatoria de adyacencia para G
import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt

#Matriz de adyacencia
def Matriz_adyacencia():
    n = 10
    G = np.random.randint(2, size = (n, n))
    print(G)

    G2 = [[random.randint(0,1) for _ in range(n)] for _ in range (n)]
    print(G2)

    G = nx.from_numpy_matrix(G)
    nx.draw(G, with_labels = True, node_color = "black", font_color = "White")
    plt.show()

#Lista de adyacencia
def ListaAdyacencia():
    n, m = 10, 20

    lst = [[]for _ in range(n)]

    for _ in range(m):
        u = random.randint(0, n-1)
        while True:
            v = random.randint(0, n-1)
            if not v in lst[u] and v != u: 
                break 
        lst[u].append(v)

    f = open("1.txt", "w")

    for u in range(n):
        print(u, *lst[u])
        ap = "{}".format(u)
        for i in lst[u]:
            ap = "{} {}".format(ap, i)
        ap = "{}\n".format(ap)
        f.write(ap)

    f.close()
    
    Gra = nx.read_adjlist("1.txt", create_using = nx.DiGraph)
    nx.draw(Gra, with_labels = True, node_color = "black", font_color = "White")
    plt.show()
ListaAdyacencia()