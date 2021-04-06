from mazeBuilder import makeMaze
import matplotlib.pyplot as plt
import time
def drawMaze(maze):
    fig, ax = plt.subplots(figsize=(18, 18))
    ax.imshow(maze, cmap='viridis') # 
    ax.axis('off')

def mazeSolve(maze, row, col, rowF, colF):
    maze[row][col] = 3              # camino correcto (amarillito)
    time.sleep(0.1)
    drawMaze(maze)
    plt.show()
    if row == rowF and col == colF: #Si es la salida
        return True
 
    for r, c in [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]: #rc se vuelve en la priemra tupla, luego la sig, y así
        if maze[r][c] == 1 and mazeSolve(maze, r, c, rowF, colF):
            return True

    maze[row][col] = 2              # camino sin salida (verde)
    time.sleep(0.1)
    drawMaze(maze)
    plt.show()
    return False

maze = makeMaze(5, 10)
rows, cols = maze.shape # matriz de numpy, sino, sería len(maze), len(maze[0])
mazeSolve(maze, 1, 1, rows - 2, cols -2 )
