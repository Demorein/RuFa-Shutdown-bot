import os
import configparser

data = configparser.ConfigParser()
data.read("data.ini")

backmode = "true"
token = data["Data"]["token"]
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
        
token = data["Data"]["token"]
if token:
    print("Token = " + str(token))
elif token == "token":
    print("EDIT TOKEN")
if not token:
    print("No token")

username = data["Data"]["username"]
if username:
    print("Username = " + str(username))
if not username:
    print("Error username")

userid = data["Data"]["userid"]
if userid:
    print("Userid = " + str(userid))
if not username:
    print("Error userid")