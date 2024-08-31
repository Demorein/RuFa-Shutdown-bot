from os import path


def _json(file:str):
    from json import load
    with open(file) as f:
        return load(f)
    
    
    
def _datetime() -> str:
        import datetime
        dt = datetime.datetime.now()
        nowtime = dt.time()
        nowdate = dt.date()
        nowday, nowmounth, nowyear, nowhour, nowminute = nowdate.day, nowdate.month, nowdate.year, nowtime.hour, nowtime.minute
        
        mess = ""
        if len(str(nowday)) == 1: mess += f"0{nowday}" 
        elif len(str(nowday)) == 2: mess += str(nowday)
            
        if len(str(nowmounth)) == 1: mess += f"-0{nowmounth}"
        elif len(str(nowmounth)) == 2: mess += f"-{nowmounth}"
            
        if len(str(nowyear)) == 1: mess += f"-0{nowyear}"
        elif len(str(nowday)) == 2: mess += f"-{nowyear}"
            
        if len(str(nowhour)) == 1: mess += f" 0{nowhour}"
        elif len(str(nowday)) == 2: mess += f" {nowhour}"
            
        if len(str(nowminute)) == 1: mess += f":0{nowminute}"
        elif len(str(nowday)) == 2: mess += f":{nowminute}"
        
        return(mess)
        
        
    
def _elogs(log:str, ecode:int, v = "INFO", file = "errlog", pathh = path.basename(__file__)) -> str: 
    logg = f"\n{_datetime()} | {(v).upper()} | {__name__}:<{pathh}>:{ecode} - {log}"
    with open(f"logs/{file}.log", "a") as f:
        f.write(logg)
        return logg
        
        
        
def idd(mess, userid):
        if mess.from_user.id == int(userid):
            _elogs(f"ID {mess.from_user.id} is True" , 200, "debug")
            return(True)
        else:
            _elogs(f"ID {mess.from_user.id} is False" , 200, "debug")
            return(False)
        
def _Actfunc(bot, messange):
    from os import system

    t = messange.text
    if t == "/Shutdown⭕️": system('shutdown.exe -s -t 5')
    if t == "/Lock🔐": system('RunDll32.exe user32.dll,LockWorkStation')
    if t == "/Hibernation💾": system('shutdown.exe /h')
    if t == "/Reboot🔄": system('shutdown.exe -r -t 5')