from structs import *
from ai import *

def trouverPlusProche(position, map, type):

    x = position.X
    y = position.Y

    n = 1
    while n < 10:
        for i in range(-n, n + 1):
            for j in range(-n, n + 1):
                if map[i+10][j+10].Content == type:
                    positionPlusProche = Point(x+i, j+y)
                    return (positionPlusProche)
        n += 1

    return None
