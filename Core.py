# Core v1.1
# Creator: Demorien

# Class with base functions
class basefunc():

    # Read json file. Returns a list
    # EXAMPLE: print(_json_read(file)["Variable"])
    def _json_read(file:str) -> str:
        import json
        with open(file, "r") as f:
            return(json.load(f))
        
    # Write Log in file, Returns -> None
    # EXAMPLE: _log("Hello", log)
    def _logs(log:str, file = "log") -> None:
        with open(f"{file}.txt", "a") as f:
            f.write(f"\n{log}")

    # Creating a config object
    # IS REQUIRED TO USE _confwrite
    def _confobj() -> None:
        import configparser
        global config
        config = configparser.ConfigParser()

    # Writing in .ini file, Returns -> None
    # EXAMPLE: _confwrite(file = "test.ini", section = "test", key = testkey, data = "for example")
    def _confwrite(file:str, section:str, key:str, data) -> None:
        config.read(file)
        config.set(section, key, data)
        with open(file, 'w') as configfile:
            config.write(configfile)

    def confread(file:str, section:str, key:str) -> str:
        config.read()
        return(config[section][key])

class debug():
    def mess(mess,code):
        from easygui import msgbox
        msgbox(mess, code)

class tg_bot():
    def idd(messange, userid):
        if messange.from_user.id == int(userid): return(True)
        else: return(False)
        
        

 
