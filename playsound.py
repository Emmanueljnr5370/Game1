import time
import playsound
from gtts import gTTS

import rotatescreen

pd = rotatescreen.get_primary_display()
angle_list = [90,180,270,0]
text = f"Trojan virus activated. your computer system has been infected"
tts = gTTS(text)
tts.save("hi.mp3")
playsound.playsound("hi.mp3")
for x in range(5):
    for angle in angle_list:
        pd.rotate_to(angle)
        time.sleep(0.3)