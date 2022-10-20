import cv2
import keyboard
import numpy as np
from PIL import ImageGrab
import BattleGrid

inBattle = False
'''
La detection de map fonctionne super bien avec ces themes la :
=> https://www.dofus.com/fr/forum/1578-themes-interfaces/2291142-2-50-theme-darkopacity?sort=rate_D

Certaines cases ne sont parfois pas reconnu, peut etre essayé de trouver un autre themes ?

BATTLE TODO :
- Pathfinding (afin de pouvoir se déplacer)
- fichier qui stock les data du perso qu'on joue (afin d'etre generique)
- LATER: Pouvoir stocker les datas des sort et intégrer un algo de ligne de vue (pas obligé)
- Pouvoir passer son tour + mettre pret 
- La detection de la map doit se faire apres avoir mis pret (ou bien trouver une solution autre)

JOB TODO :
- Pouvoir définir un path sur une grid GUI (représentant la map dofus)
- Pouvoir donc solve ce path
- Pouvoir définir les metier qu'on souhaite utiliser
- La tranche de level autorisé (ressources a collect)
- Pouvoir detecter quasi toutes les ressources et cliquer dessus avec un interval X
- Géré les temps d'attente de maniere random entre X et Y

AUTRE ?

'''
def InBattle():
    global inBattle
    inBattle = True if not inBattle else False

def TestGrid():
    canConstrcut = False
    templateGrid = BattleGrid.GetTemplateGridMap()
    currentGrid = BattleGrid.BattleGrid()
    keyboard.add_hotkey("z", InBattle)

    while(True):
        if not inBattle:
            continue

        screen = np.array(ImageGrab.grab())
        gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

        if not canConstrcut:
            for i in range(33):
                for j in range(32):
                    currentGrid.Cells[i][j].ScreenPos = templateGrid.Cells[i][j].ScreenPos
                    if (templateGrid.Cells[i][j].State == BattleGrid.CellState.NONE):
                        continue

                    x, y = currentGrid.Cells[i][j].ScreenPos

                    if gray[y, x] < 40:
                        continue

                    currentGrid.Cells[i][j].State = BattleGrid.CellState.FREE
        
        for i in range(33):
            for j in range(32):
                if (currentGrid.Cells[i][j].State == BattleGrid.CellState.NONE):
                    continue
                cv2.circle(screen, currentGrid.Cells[i][j].ScreenPos, 6, (255, 255, 0), -1)

        canConstrcut = True
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        cv2.imshow("gray", gray)
        cv2.imshow("screen", screen)

        if (cv2.waitKey(30) == 27):
            break
    cv2.destroyAllWindows()


TestGrid()