import random,pyautogui

for x in range(120):
    h = random.randint(0,800)
    w = random.randint(0,1000)
    pyautogui.click(h,w,duration = 0.1)
    pyautogui.hotkey('winleft','m')
    
import time
import rotatescreen

pd = rotatescreen.get_primary_display()
angle_list = [90,180,270,0]

for x in range(5):
    for angle in angle_list:
        pd.rotate_to(angle)
        time.sleep(0.3)