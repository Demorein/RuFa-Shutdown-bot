import tkinter as tk
from tkinter import ttk

def WinConfig():
    subConfig = tk.Toplevel()
    subConfig.geometry("200x150")
    subConfig.title("RuFA SB Config")
    subConfig.resizable(False, False)

    def Apply():
        subConfig.destroy()

    LabelToken = ttk.Label(subConfig, text="Bot Token").place(x=75,y=10)
    EntryToken = ttk.Entry(subConfig, width=25).place(x=25,y=30)

    LabelUserID = ttk.Label(subConfig, text="UserID").place(x=85,y=60)
    EntryUserID = ttk.Entry(subConfig,width=25).place(x=25, y=80)

    btnApply = ttk.Button(subConfig, text="Apply",command=Apply).place(x=65,y=110)

    subConfig.mainloop()

def WinSett():
    subSett = tk.Toplevel()
    subSett.geometry("170x140")
    subSett.title("RuFA SB Settings")
    subSett.resizable(False, False)

    def Apply():
        subSett.destroy()

    checkboxDebugMode = ttk.Checkbutton(subSett,text="Debug Mode\n(For developers)").place(x=20, y= 10)
    checkboxNormalModeAct = ttk.Checkbutton(subSett,text="Active ping?").place(x=20, y= 50)
    ApplyButton = ttk.Button(subSett,text='Apply',command=Apply).place(x=40, y= 90)

    subSett.mainloop()

def WinAbout():
    subAbout = tk.Toplevel()
    subAbout.geometry("200x100")
    subAbout.title("About")
    subAbout.resizable(False, False)

    LabelName = ttk.Label(subAbout,text="RuFA Shutdown Bot").pack()
    LabelVersion = ttk.Label(subAbout,text="v2.0-b").pack()
    LabelCreator = ttk.Label(subAbout,text="Creator Demorien").pack()
    LabelType = ttk.Label(subAbout,text="OPEN SOURCE").pack()

    subAbout.mainloop()
    
    