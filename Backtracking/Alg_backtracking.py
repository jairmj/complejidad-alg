import matplotlib.pyplot as plt
import numpy as np

def dibujar(t):
    n = len(t)
    tablero = np.zeros((n, n, 3))
    tablero += 0.8
    tablero[::2, ::2] = 1
    tablero[1::2, 1::2] = 1

    fig, ax = plt.subplots()
    ax.imshow(tablero, interpolation='nearest')

    for y, x in enumerate(t):
        ax.text(x, y, u'\u2655', size=30, ha='center', va='center')

    ax.set(xticks=[], yticks = [])
    ax.axis('image')

    plt.show()
    
dibujar([0, 2, -1, -1])

def isLegal(board, row, column):
    n = len(board)
    for i in range(row):
        if board[i] == column:
            return False
        dif = row - i
        if board[i] + diff == column or board[i] - dif == column:
            return False