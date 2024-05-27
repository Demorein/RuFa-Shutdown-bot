import telebot
from telebot import types
from Core import basefunc, tg_bot
import configparser
import botevents

def botwork(token, userid, debug, ping):
    bot = telebot.TeleBot(token=token)

    @bot.message_handler(commands=["start"])
    def start(messange):
        if tg_bot.idd(messange,userid) == True: botevents._start(bot,messange)

    @bot.message_handler(commands=["func🔙"])
    def func(messange):
        if tg_bot.idd(messange,userid) == True: botevents._func(bot,messange)

    @bot.message_handler(commands=["Shutdown⭕️"])
    def sht(messange):
        if tg_bot.idd(messange,userid) == True: botevents._Actfunc(bot,messange)
    
    @bot.message_handler(commands=["Infoℹ️"])
    def inf(messange):
        if tg_bot.idd(messange,userid) == True: botevents._Actfunc(bot,messange)
    
    @bot.message_handler(commands=["Ping🔔"])
    def inf(messange):
        if tg_bot.idd(messange,userid) == True: botevents._Actfunc(bot,messange,ping)

    @bot.message_handler(commands=["Lock🔐"])
    def inf(messange):
        if tg_bot.idd(messange,userid) == True: botevents._Actfunc(bot,messange)

    @bot.message_handler(commands=["Hibernation💾"])
    def inf(messange):
        if tg_bot.idd(messange,userid) == True: botevents._Actfunc(bot,messange)

    @bot.message_handler(commands=["Reboot🔄"])
    def inf(messange):
        if tg_bot.idd(messange,userid) == True: botevents._Actfunc(bot,messange)

    bot.infinity_polling()

def main():
    data = configparser.ConfigParser()
    data.read("Config.ini")

    global token, userid, debug, ping, markup
    token, userid, ping, debug = data["Config"]["token"], data["Config"]["userid"], data["Settings"]["ping"], data["Settings"]["debug"]
    print(f"Token = {token}\nUserID = {userid}\nActive Ping = {ping}\nDebug Mode = {debug}")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    botwork(token, userid, debug, ping)

main()