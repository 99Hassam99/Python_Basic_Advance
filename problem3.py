"""
import pyttsx3
engine = pyttsx3.init()
engine.say("Hy How are you")
engine.runAndWait()

engine=pyttsx3.init()
engine.say("Can you please tell Eimaan to say i love you to me")
engine.runAndWait()
"""

import pyautogui

pyautogui.moveTo(100, 200,duration=2)  # moves mouse to X of 100, Y of 200.
pyautogui.moveRel(100,200, duration=2)