import time
import rotatescreen

pd = rotatescreen.get_primary_display()
angle_list = [90,180,270,0]

for x in range(5):
    for angle in angle_list:
        pd.rotate_to(angle)
        time.sleep(0.3)