
from structs import *


def strat(player):
    print("--- Strat ---")

    if player.level < 3:

        if distanceEnnemieToHouse():
            moveTo(Player.HouseLocation)

        elif player.CarriedRessources >= player.CarryingCapacity:
            moveTo(player.HouseLocation)

        elif distanceEntre(player.Position, trouverPlusProche(minerais)) == 1:
            miner()
        else
            moveTo(trouverPlusProche(minerais))

    else




def distanceEntre(point1, point2):
    deltaX = abs(point1.x - point2.x)
    deltaY = abs(point1.y - point2.y)
    total = deltaX+deltaY
    return total


