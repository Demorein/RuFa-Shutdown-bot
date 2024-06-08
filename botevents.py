from telebot import types
import os

def _start(bot, messange):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnfunc = types.KeyboardButton("/func🔙")
    markup.add(btnfunc)

    bot.send_message(chat_id=messange.chat.id, text="Hi",
                     reply_markup=markup)
    
    
def _func(bot, messange):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnsht = types.KeyboardButton("/Shutdown⭕️")
    btninf = types.KeyboardButton("/Infoℹ️")
    btnping = types.KeyboardButton("/Ping🔔")
    btnlock = types.KeyboardButton("/Lock🔐")
    btnhib = types.KeyboardButton("/Hibernation💾")
    btnreb = types.KeyboardButton("/Reboot🔄")
    markup.add(btnsht, btninf, btnping, btnlock, btnhib, btnreb)

    bot.send_message(chat_id=messange.chat.id, text=f"Hello!\n@{messange.from_user.username}",
                     reply_markup=markup)
    
def _Actfunc(bot, messange, ping = None):
    from win10toast import ToastNotifier
    n = ToastNotifier()
    def _sendInfo():
        bot.send_message(messange.chat.id, 
            text="RuFa 2.0-b (OPEN SOURCE)\nCreator Demorien\nTelegramBot")
    #def _sendAct():
        #bot.send_message(messange.chat.id, 
            #text="Ping function is disabled\n\nCheck bot settings")
    def _sendActae():
        bot.send_message(messange.chat.id, 
            text="Act🔔")
        
    t = messange.text
    if t == "/Shutdown⭕️": os.system('shutdown.exe -s -t 5')
    if t == "/Infoℹ️": _sendInfo()
    if t == "/Ping🔔" and ping == "1":
        print("\n")
        _sendActae()
        n.show_toast("Rufa", "You pinged", duration = 10)
    else:
        #_sendAct()
        pass

    if t == "/Lock🔐": os.system('RunDll32.exe user32.dll,LockWorkStation')
    if t == "/Hibernation💾": os.system('shutdown.exe /h')
    if t == "/Reboot🔄": os.system('shutdown.exe -r -t 5')

