from structs import *
from ai import *

def trouverPlusProche(position, map, type):

    x = position.x
    y = position.y

    n = 1
    while n < 10:
        for i in range(x - n, x + n + 1):
            for j in range(y - n, y + n + 1):
                if map[i][j].Content == type:
                    positionPlusProche = Point(x, y)
                    return (positionPlusProche)
        n += 1

    return None
