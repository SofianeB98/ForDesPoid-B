import cv2
import keyboard
import numpy as np
from PIL import ImageGrab
import BattleGrid

inBattle = False

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