import os, time, tkinter as tk, telebot, threading as th
from tkinter import ttk
from Core import basefunc
from wins import *

def main():
    root = tk.Tk()
    root.resizable(False, False)
    root.geometry("400x200")
    root.title("RuFA SB Monitor")

    btnOpenConfig = ttk.Button(root, text="Open Config", command=WinConfig, width=13).place(x=310,y=10)
    btnOpenSett = ttk.Button(root, text= "Open Settings", command=WinSett, width=13).place(x=310,y=40)
    btnOpenAbout = ttk.Button(root, text= "About RuFA SB", command=WinAbout, width=13).place(x=310,y=170)

    root.mainloop()

if __name__ == "__main__":
    main()


