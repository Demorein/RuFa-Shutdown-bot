import tkinter as tk
from tkinter import ttk
from Core import basefunc, debug
from main import _start
import threading

def WinConfig():
    subConfig = tk.Toplevel()
    subConfig.geometry("200x150")
    subConfig.title("RuFA SB Config")
    subConfig.resizable(False, False)

    def Apply():
        import error_codes
        basefunc._confobj()
        if EntryToken.get() and EntryUserID.get():
            basefunc._confwrite(file = "config.ini", section = 'Config', key = "token", data = EntryToken.get())
            basefunc._confwrite(file = "config.ini", section = 'Config', key = "userid", data = EntryUserID.get())
            update()

        else:
            basefunc._confwrite(file = "config.ini", section = 'Config', key = "token", data = "0")
            basefunc._confwrite(file = "config.ini", section = 'Config', key = "userid", data = "0")
            debug.mess(error_codes.e41.split("$")[0],error_codes.e41.split("$")[1])
            update()
        subConfig.destroy()

    LabelToken = ttk.Label(subConfig, text="Bot Token").place(x=75,y=10)
    EntryToken = ttk.Entry(subConfig, width=25)
    EntryToken.place(x=25,y=30)

    LabelUserID = ttk.Label(subConfig, text="UserID").place(x=85,y=60)
    EntryUserID = ttk.Entry(subConfig,width=25)
    EntryUserID.place(x=25, y=80)

    btnApply = ttk.Button(subConfig, text="Apply",command=Apply).place(x=65,y=110)

    subConfig.mainloop()

def WinSett():
    subSett = tk.Toplevel()
    subSett.geometry("170x140")
    subSett.title("RuFA SB Settings")
    subSett.resizable(False, False)

    basefunc._confobj()
    
    def Apply():
        basefunc._confwrite(file = "config.ini", section = 'Settings', key = "debug", data = str(Debugm.get()))
        basefunc._confwrite(file = "config.ini", section = 'Settings', key = "ping", data = str(Pingm.get()))
        
        #DELETE
        #basefunc._confwrite(file = "config.ini", section = 'Settings', key = 'autostart', data = str(AutoStart.get()))
        
        update()
        subSett.destroy()

    Debugm = tk.IntVar()
    Pingm = tk.IntVar()
    AutoStart = tk.IntVar()

    #DETELE
    #checkboxAutoStart = ttk.Checkbutton(subSett, text="Auto Start",variable=AutoStart).place(x=20, y=80)
    
    checkboxDebugMode = ttk.Checkbutton(subSett,text="Debug Mode\n(For developers)",variable=Debugm).place(x=20, y= 10)
    checkboxPing = ttk.Checkbutton(subSett,text="Active ping?",variable=Pingm).place(x=20, y= 50)
    ApplyButton = ttk.Button(subSett,text='Apply',command=Apply).place(x=40, y= 110)

    subSett.mainloop()

def WinAbout():
    subAbout = tk.Toplevel()
    subAbout.geometry("200x100")
    subAbout.title("About")
    subAbout.resizable(False, False)

    def Ok():
        subAbout.destroy()

    LabelName = ttk.Label(subAbout,text="RuFA Shutdown Bot").pack()
    LabelVersion = ttk.Label(subAbout,text="v2.0-b").pack()
    LabelCreator = ttk.Label(subAbout,text="Creator Demorien").pack()
    LabelType = ttk.Label(subAbout,text="OPEN SOURCE").pack()
    btnOk = ttk.Button(subAbout, text="Ок",command=Ok).pack()

    subAbout.mainloop()

def update():
    from configparser import ConfigParser
    cfg = ConfigParser()
    cfg.read("config.ini")

    if cfg["Config"]["token"] == "0":
        labeltoken = ttk.Label(text=cfg["Config"]["token"],width=50,background="red").place(x=0, y=0)
    else:
        labeltoken = ttk.Label(text=cfg["Config"]["token"],width=50).place(x=0, y=0)


    if cfg["Config"]["userid"] == "0":
        labeluserid = ttk.Label(text=cfg["Config"]["userid"],width=50, background="red").place(x=0, y=20)
    else:
        labeluserid = ttk.Label(text=cfg["Config"]["userid"],width=50).place(x=0, y=20)


    if cfg["Settings"]["debug"] == "1":
        labeldebug = ttk.Label(text="Debug mode = True  ").place(x=0, y=40)
    else:
        labeldebug = ttk.Label(text="Debug mode = False").place(x=0, y=40)


    if cfg["Settings"]["ping"] == "1":
        labelping = ttk.Label(text="Active Ping = True",width=50).place(x=0, y=60)
    else:
        labelping = ttk.Label(text="Active Ping = False",width=50).place(x=0, y=60)



    #START BUTTON
    def __start():
        threading.Thread(target=_start).start()
        
    if cfg["Config"]["token"] == "0" or cfg["Config"]["userid"] == "0":
        btnStart = ttk.Button(text="Start RuFA", width=13, state="disabled").place(x=310,y=70)
    else:
        btnStart = ttk.Button(text="Start RuFA", width=13, command=__start).place(x=310,y=70)