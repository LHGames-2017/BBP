
from structs import *
from look import *
import ai
import path_finder


def strat(player, map):
    print("--- Strat ---")

    posRes = trouverPlusProche(player.HouseLocation, map, 1)

    if player.level < 3:

        if (DistanceEntre(player.HouseLocation, player.Position)+1) > DistanceEntre(trouverPlusProche(player.HouseLocation, map, 2), player.HouseLocation):
            return path_finder.move_to(map, player.Position, player.HouseLocation)

        elif player.CarriedRessources >= player.CarryingCapacity:
            return path_finder.move_to(map, player.Position, player.HouseLocation)

        elif abs(DistanceEntre(player.Position, posRes)) == 1:
            return ai.create_collect_action(posRes)

        else:
            return path_finder.move_to(map, player.Position, posRes)



    return


def DistanceEntre(point1, point2):
    deltaX = abs(point1.x - point2.x)
    deltaY = abs(point1.y - point2.y)
    total = deltaX+deltaY
    return total

