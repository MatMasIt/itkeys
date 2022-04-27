from pystray import MenuItem as item
import pystray
from PIL import Image
import webbrowser
import daemon
import tkinter
import sys
import threading
import os

print(os.path.dirname(__file__))

def repow():
    webbrowser.open("https://github.com/MatMasIt/itkeys")

def licewo():
    webbrowser.open("https://github.com/MatMasIt/itkeys/blob/main/LICENSE")

state = True
def about():
    gui = tkinter.Tk()
    gui.title('Riguardo a ItKeys')
    gui.geometry("500x200")
    gui.iconbitmap('logo.ico')
    # create button
    label = tkinter.Label(gui, text='ItKeys 1.0\n2022, Mattia Mascarello\n Rilasciato sotto Licenza Apache 2.0')
    repo = tkinter.Button(gui, text='Repository', width=40, height=3, command = repow)
    lic = tkinter.Button(gui, text='Licenza', width=40, height=3, command = licewo)
    label.pack()
    repo.pack()
    lic.pack()
    gui.resizable(False,False)
    gui.focus_set()
    gui.mainloop() 

def start():
    if not daemon.mustRun:
        daemon.mustRun = True
        threading.Thread(target=daemon.run).start()
def stop():
    daemon.mustRun = False

def toggle(icon, item):
    global state
    state = not item.checked
    if state:
        start()
    else:
        stop()
start()

def die():
    icon.stop()
    stop()
    sys.exit()

image = Image.open("logo.jpg")
menu = (item('Sostituzione maiuscole accentate', toggle, lambda item: state), item('Riguardo a...', about), item("Chiudi",die))
icon = pystray.Icon("name", image, "ITkeys", menu)
icon.run()
