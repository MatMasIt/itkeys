import keyboard
import ctypes
import subprocess
import os
import sys
import time


os.chdir(os.path.abspath(os.path.dirname(__file__)))
def sendKey(key):
    args = ["nircmd.exe", "clipboard", "saveclp", "temp.clp"]
    subprocess.call(args)
    args = ["nircmd.exe", "clipboard", "set", key]
    subprocess.call(args)
    keyboard.send("backspace")
    keyboard.send("ctrl+v")
    time.sleep(0.1)
    args = ["nircmd.exe", "clipboard", "loadclp", "temp.clp"]
    subprocess.call(args)
def isCapslockOn():
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL) & 0xffff !=0
mustRun = False
def run():
    global mustRun
    while mustRun:
        key = keyboard.read_key()
        if not isCapslockOn():
            continue
        if key == "à":
            sendKey("À")
        elif key == "è":
            sendKey("È")
        elif key == "é":
            sendKey("É")
        elif key == "ì":
            sendKey("Ì")
        elif key == "ò":
            sendKey("Ò")
        elif key == "ù":
            sendKey("Ù")
