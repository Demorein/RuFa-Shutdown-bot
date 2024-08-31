import telebot
from telebot import types
import Core
from os import path

def main(b, userid):
    print(Core._elogs("Initializing Basic Functions" , 102, "debug", pathh = path.basename(__file__)))
    
    @b.message_handler(commands = ["start"])
    def start(messange):
        if Core.idd(messange, userid) == True:
            ShutdownB = types.KeyboardButton("/Shutdown⭕️")
            SpecialB = types.KeyboardButton("/Special🛠")
            HibernateB = types.KeyboardButton("/Hibernation💾")
            InfoB = types.KeyboardButton("/Infoℹ️")
            LockB = types.KeyboardButton("/Lock🔐")
            RebootB = types.KeyboardButton("Reboot🔄")
            markup.add(ShutdownB, InfoB, HibernateB, SpecialB, RebootB, LockB)
            b.send_message(messange.chat.id,
                        text = "Привет👋",
                        reply_markup =markup)
            Core._elogs("Command /start -------- OK", 200, pathh= path.basename(__file__))
        else:
            Core._elogs("Command /start -------- Access denied", 403, "ERROR", pathh= path.basename(__file__))
        
        
    @b.message_handler(commands=["Shutdown⭕️"])
    def sht(messange):
        if Core.idd(messange,userid) == True: 
            Core._elogs("Command /Shutdown -------- OK", 200, pathh= path.basename(__file__))
            Core._Actfunc(b ,messange)
        
        
    @b.message_handler(commands=["Special🛠"])
    def sp(messange):
        if Core.idd(messange,userid) == True:
            Core._elogs("Command /Special -------- OK", 200, pathh= path.basename(__file__))
            b.send_message(messange.chat.id, 
            text= f"Your user id {messange.from_user.id}")
            
    @b.message_handler(commands=["Lock🔐"])
    def lock(messange):
        if Core.idd(messange,userid) == True: 
            Core._elogs("Command /Lock -------- OK", 200, pathh= path.basename(__file__))
            Core._Actfunc(b,messange)
    
    @b.message_handler(commands=["Reboot🔄"])
    def reboot(messange):
        if Core.idd(messange,userid) == True: 
            Core._elogs("Command /Reboot -------- OK", 200, pathh= path.basename(__file__))
            Core._Actfunc(b,messange)
        
    @b.message_handler(commands=["Hibernation💾"])
    def inf(messange):
        if b.idd(messange,userid) == True:
            Core._elogs("Command /Hibernation -------- OK", 200, pathh= path.basename(__file__))
            Core._Actfunc(b,messange)
        
    @b.message_handler(commands=["Infoℹ️"])
    def info(messange):
        b.send_message(messange.chat.id, 
            text="RuFa 1.12-b (OPEN SOURCE)\nCreator Demorien\nTelegramBot")
        Core._elogs("Command /Info -------- OK", 200, pathh= path.basename(__file__))
        
        
        
    print(Core._elogs("Bot started -------- OK", 200, "info",pathh= path.basename(__file__)))
    b.infinity_polling()
        

if __name__ == "__main__":
    config = Core._json("config.json")
    try:
        b = telebot.TeleBot(config["token"])
    except ValueError as v:
        print(Core._elogs(f"{v}", 404, "critical error", pathh= path.basename(__file__)))
        exit(1)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    print(Core._elogs("Bot starting", 200, "debug",pathh= path.basename(__file__)))
    main(b, config["userid"])