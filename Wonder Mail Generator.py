import time
import numpy as np
import pyautogui
def move(difference,movementKeys,selectKey):
    up = movementKeys[0]
    down = movementKeys[2]
    left = movementKeys[1]
    right = movementKeys[3]
    select = selectKey
    differenceX = difference[0]
    differenceY = difference[1]
  
    if differenceX < 0:
        for i in range(np.abs(differenceX)):
            pyautogui.keyDown(right)
            pyautogui.keyUp(right)
    else:
        for i in range(np.abs(differenceX)):
            pyautogui.keyDown(left)
            pyautogui.keyUp(left)
    if differenceY < 0:
        for i in range(np.abs(differenceY)):
            pyautogui.keyDown(down)
            pyautogui.keyUp(down)
    else:
        for i in range(np.abs(differenceY)):
            pyautogui.keyDown(up)
            pyautogui.keyUp(up)
    pyautogui.keyDown(selectKey)
    pyautogui.keyUp(selectKey)
    return 0

def autoTyper(string,movementKeys=('w','a','x','d'),selectKey = 'j'):
    keyboard = np.array([['A','B','C','D','E','F','G','H','I','J','K','L','M'],
                     ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
                     ['ee','1','2','3','4','5','6','7','8','9','0','colon','.'],
                     ['+','-','comma','fullstop','!','?','le','re','ls','rs','%','#','space']
                    ])
    startingPoint = 'N'
    startingIndex = np.where(keyboard == startingPoint)
    iterator = string + '~'
    time.sleep(2)
    for i in iterator:
        if i == '~':
            pyautogui.keyDown(selectKey)
            pyautogui.keyUp(selectKey)
            break
        nextPoint = i 
        nextIndex = np.where(keyboard == nextPoint)
        move([startingIndex[1][0] - nextIndex[1][0],
              startingIndex[0][0] - nextIndex[0][0]],movementKeys,selectKey)
        startingPoint = i
        startingIndex = np.where(keyboard == startingPoint)
    return 0
        
def main():
    string = input("Please input the Wonder Mail: ")
    print("Starting in 2 seconds.")
    time.sleep(1)
    print("Starting in 1 second.")
    time.sleep(1)
    print("Starting Now")
    autoTyper(string,movementKeys=('w','a','x','d'),selectKey = 'j')
    print("Finished")
    input("Press Enter to escape")
    return 0 

if __name__ == '__main__':
    main()