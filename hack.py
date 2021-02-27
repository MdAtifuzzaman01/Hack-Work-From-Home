import pyautogui
import  time
pyautogui.FAILSAFE = False
while True:
    time.sleep(300)
    for x in range(0 , 100):
        pyautogui.moveTo(0, x * 5)

    for y in range(0,3):
        pyautogui.press('Shift')
