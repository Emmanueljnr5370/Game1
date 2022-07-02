import random,pyautogui

while True:
    h = random.randint(0,800)
    w = random.randint(0,1000)
    pyautogui.click(h,w,duration = 0.1)
    pyautogui.hotkey('winleft','m')

