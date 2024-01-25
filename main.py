import os
import configparser

data = configparser.ConfigParser()
data.read("data.ini")

backmode = data["Settings"]["Debug_mode"]
print(backmode)

if not backmode:
    print("No data")
if backmode:
    if backmode == "false":
        os.system("start pythonw rufa.pyw")
        exit()
    elif backmode == "true":
        os.system("start python rufa.py")
        exit()
    else:
         print("Only bool values!")
        
