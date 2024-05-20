# BotCore v1.1
# Creator: Demorien

class basefunc():

    #Read json file. Returns a list
    #EXAMPLE: print(_json_read(file)["Variable"])
    def _json_read(file:str) -> str:
        import json
        with open(file, "r") as f:
            return(json.load(f))
        
    #Write Log in file, Returns None
    #EXAMPLE: _log("Hello", log)
    def _logs(log:str, file = "log") -> None:
        with open(f"{file}.txt", "a") as f:
            f.write(f"\n{log}")

 
