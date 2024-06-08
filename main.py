import os, time, tkinter as tk, threading as th
from tkinter import ttk
from wins import *
import bot
from configparser import ConfigParser

def _start():
    data = ConfigParser()
    data.read("config.ini")

    _debugmode = data['Settings']['debug']
    if _debugmode == "1":bot._main()
    elif _debugmode == "0":bot._main()

def main():
    root = tk.Tk()
    root.resizable(False, False)
    root.geometry("400x130")
    root.title("RuFA SB Monitor")

    btnOpenConfig = ttk.Button(root, text="Open Config", command=WinConfig, width=13).place(x=310,y=10)
    btnOpenSett = ttk.Button(root, text= "Open Settings", command=WinSett, width=13).place(x=310,y=40)
    btnOpenAbout = ttk.Button(root, text= "About RuFA SB", command=WinAbout, width=13).place(x=310,y=100)
    InfoLabel = ttk.Label(text="RuFA Shutdown Bot Monitor").place(x=0,y=100)
    root.mainloop()

if __name__ == "__main__":
    th.Thread(target = update).start()
    main()


