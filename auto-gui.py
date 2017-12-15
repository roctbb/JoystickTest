import pyautogui
import time
# gives us time to get situated in the game
time.sleep(5)

print('down')
pyautogui.keyDown('w')
time.sleep(3)
print('up')
pyautogui.keyUp('w')