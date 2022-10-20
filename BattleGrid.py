'''
------------xx------------------
-----------xxxx-----------------
----------xxxxxx----------------
---------xxxxxxxx---------------
--------xxxxxxxxxx--------------
-------xxxxxxxxxxxx-------------
------xxxxxxxxxxxxxx------------
-----xxxxxxxxxxxxxxxx-----------
----xxxxxxxxxxxxxxxxxx----------
---xxxxxxxxxxxxxxxxxxxx---------
--xxxxxxxxxxxxxxxxxxxxxx--------
-xxxxxxxxxxxxxxxxxxxxxxxx-------
xxxxxxxxxxxxxxxxxxxxxxxxxx------
xxxxxxxxxxxxxxxxxxxxxxxxxxx-----
xxxxxxxxxxxxxxxxxxxxxxxxxxxx----
-xxxxxxxxxxxxxxxxxxxxxxxxxxxx---
--xxxxxxxxxxxxxxxxxxxxxxxxxxxx--
---xxxxxxxxxxxxxxxxxxxxxxxxxxxx-
----xxxxxxxxxxxxxxxxxxxxxxxxxxxx
-----xxxxxxxxxxxxxxxxxxxxxxxxxxx
------xxxxxxxxxxxxxxxxxxxxxxxxxx
-------xxxxxxxxxxxxxxxxxxxxxxxx-
--------xxxxxxxxxxxxxxxxxxxxxx--
---------xxxxxxxxxxxxxxxxxxxx---
----------xxxxxxxxxxxxxxxxxx----
-----------xxxxxxxxxxxxxxxx-----
------------xxxxxxxxxxxxxx------
-------------xxxxxxxxxxxx-------
--------------xxxxxxxxxx--------
---------------xxxxxxxx---------
----------------xxxxxx----------
-----------------xxxx-----------
------------------xx------------
'''
from enum import Enum
import json

#none = fake cell, block = obstacles/empty, free = can be reached, player = player, mob = mob
class CellState(str, Enum):
    NONE = "NONE",
    BLOCK = "BLOCK",
    FREE = "FREE",
    PLAYER = "PLAYER",
    MOB = "MOB"


class Cell():
    def __init__(self, gridPos):
        self.ScreenPos = [-9999, -9999]
        self.GridPos = gridPos
        self.State = CellState.NONE

class BattleGrid():
    def __init__(self):
        self.Cells = [[Cell([j, i]) for i in range(32)] for j in range(33)]



# -------------------------------------------

def GetTemplateGridMap() -> BattleGrid:
    mapdofus = BattleGrid()
    with open("./json/dofusmap_template.json", "r") as js:
        dicto = json.load(js)
        for i in range(33):
            for j in range(32):
                mapdofus.Cells[i][j].GridPos = dicto['Cells'][i][j]['GridPos']
                mapdofus.Cells[i][j].ScreenPos = dicto['Cells'][i][j]['ScreenPos']
                mapdofus.Cells[i][j].State = CellState(dicto['Cells'][i][j]['State'])
    
    return mapdofus
