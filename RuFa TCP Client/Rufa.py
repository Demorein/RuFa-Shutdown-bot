#RuFa 2.0-b Server +
#Библиотеки
from colorama import Fore, Back, Style
import configparser
import telebot
from telebot import types
from win10toast import ToastNotifier
import os
import socket

os.system("cls")

print("Starting...")

n = ToastNotifier() 

data = configparser.ConfigParser()
data.read("data.ini")

#Client object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Переменные из data.ini
token = data["Data"]["token"]
print(Fore.LIGHTCYAN_EX + "Token = " + str(token))

username = data["Data"]["username"]
print("Username = " + str(username))

userid = data["Data"]["userid"]
print("Userid = " + str(userid))

backmode = "true"
print("Debug Mode = " + str(backmode))

ip = data["TCP"]["ip"]
print("\nIP = " + str(ip))

port = data["TCP"]["port"]
print("PORT = " + str(port))


#API Telegram
api_token = token
bot = telebot.TeleBot(api_token)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


##TCP Client trying connect to server ip:port
#FIXME: Replace on socket
def _connect():
    try:
        #FIXME: Solve the problem that ip and port are not imported into the rufa.py file
        client.connect(("LOCALHOST", YOURPORT))
        packet = client.recv(1024).decode("utf-8")
        print(Fore.LIGHTGREEN_EX + "\nGeted packet:" + str(packet))
        print("\nIP/PORT:\n" + str(client.getsockname()))
        return False
    
    except ConnectionRefusedError:
        if backmode == "true":
            print(Fore.LIGHTRED_EX + "\nTCP ERROR: 402\n" + "The server rejected the connection request")
        elif backmode == "false":
            os.system("start .vbs\TCP402")
        return True

    except ValueError:
        if backmode == "true":
            print(Fore.LIGHTRED_EX + "\nTCP ERROR: 404\nEnter values IP and PORT in file data.ini")
        elif backmode == "false":
            os.system("start .vbs\TCP404")
        return True
  
    except ConnectionResetError:
        if backmode == "true":
            print(Fore.LIGHTRED_EX + "\nTCP ERROR: 403\nThe remote host forcibly closed an existing connection")
        elif backmode == "false":
            os.system("start .vbs\TCP403")
        return True

ClientError = _connect()

#Команда /start
@bot.message_handler(commands=['start'])
def start(messange):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("func🔙")
    markup.add(btn1)
    bot.send_message(messange.chat.id, 
        text="Привет👋", 
        reply_markup=markup)


#Команда func (Выводит список возможных функций func)
@bot.message_handler(content_types=['text'])
def func(messange):
    if(messange.text == "func🔙") and messange.from_user.id == int(userid):
        bot.send_message(messange.chat.id, 
            text="func🔙")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        #Кнопки
        btn2 = types.KeyboardButton("🔴Shutdown🔴")
        btn3 = types.KeyboardButton("Infoℹ️")
        btn4 = types.KeyboardButton("Ping🔔")
        btn5 = types.KeyboardButton("Lock🔐")
        btn16 = types.KeyboardButton("Hibernation💾")
        btn17 = types.KeyboardButton("Reboot🔄")
        btn18 = types.KeyboardButton("Special🛠")
        markup.add(btn2, btn3, btn4, btn5, btn16, btn17, btn18)
        bot.send_message(messange.chat.id, 
            text="Привет👋", 
            reply_markup=markup)
        
    #Функция Ping (Отправляет запрос на Windows cистему)
    elif(messange.text == "Ping🔔") and messange.from_user.id == int(userid):
        if ClientError == False:
            try:
                client.send(("Ping".encode("utf-8")))
                bot.send_message(messange.chat.id, 
                    text="Act🔔")
            except ConnectionResetError:
                bot.send_message(messange.chat.id, 
                    text="TCP ERROR🔴")
                print(Fore.LIGHTRED_EX + "TCP ERROR: Ping")
                
        elif ClientError == True:
            bot.send_message(messange.chat.id,
                text="Server disable🔴")
        
        #n.show_toast("Rufa", "You pinged", duration = 10, icon_path ="rufa.ico")
    
    #Функция Lock (Блокирует Windows cистему)
    elif(messange.text == "Lock🔐") and messange.from_user.id == int(userid):
        if ClientError == False:
            try:
                client.send(("Lock".encode("utf-8")))
                bot.send_message(messange.chat.id,
                    text="Locked")
            except ConnectionResetError:
                bot.send_message(messange.chat.id, 
                    text="TCP ERROR🔴")
                print(Fore.LIGHTRED_EX + "TCP ERROR: Lock")
                
        elif ClientError == True:
            bot.send_message(messange.chat.id,
                text="Server disable🔴")

        #os.system('RunDll32.exe user32.dll,LockWorkStation')
        
    #Функция Shutdown (Моментально выключает Windows cистему)
    elif(messange.text == "🔴Shutdown🔴") and messange.from_user.id == int(userid):
        if ClientError == False:
            try:
                client.send(("Shutdown".encode("utf-8")))
                bot.send_message(messange.chat.id, 
                    text="🔴Shutdowning...🔴")
            except ConnectionResetError:
                bot.send_message(messange.chat.id, 
                    text="TCP ERROR🔴")
                print(Fore.LIGHTRED_EX + "TCP ERROR: Shutdown")
                
        elif ClientError == True:
            bot.send_message(messange.chat.id,
                text="Server disable🔴")

        #os.system('shutdown.exe -s -t 5')
    
    #Функция Гибернация (Моментально вводит cистему в режим Гибернации)
    elif(messange.text == "Hibernation💾") and messange.from_user.id == int(userid):
        if ClientError == False:
            try:
                client.send(("Hibernation".encode("utf-8")))
                bot.send_message(messange.chat.id, 
                    text="Hibernate...💾")
            except ConnectionResetError:
                bot.send_message(messange.chat.id, 
                    text="TCP ERROR🔴")
                print(Fore.LIGHTRED_EX + "TCP ERROR: Hibernation")
                
        elif ClientError == True:
            bot.send_message(messange.chat.id,
                text="Server disable🔴")

        #os.system('shutdown.exe /h')

    #Функция Reboot(Моментально перезагружает cистему)
    elif(messange.text == "Reboot🔄") and messange.from_user.id == int(userid):
        if ClientError == False:
            try:
                client.send(("Reboot".encode("utf-8")))
                bot.send_message(messange.chat.id, 
                    text="Rebooting...🔄")
            except ConnectionResetError:
                bot.send_message(messange.chat.id, 
                    text="TCP ERROR🔴")
                print(Fore.LIGHTRED_EX + "TCP ERROR: Reboot")
                
        elif ClientError == True:
            bot.send_message(messange.chat.id,
                text="Server disable🔴") 
            
        #os.system('shutdown.exe -r -t 5')
        
    #info
    elif(messange.text == "Infoℹ️") and messange.from_user.id == int(userid):
        bot.send_message(messange.chat.id, 
            text="RuFa 2.0-b (OPEN SOURCE)\nCreator Demorien\nTelegramBot")
        
    #Функция Special (Выводит userid пользователя)
    elif(messange.text == "Special🛠") and messange.from_user.id == int(userid):
        bot.send_message(messange.chat.id, 
            text="Your user id " + str(messange.from_user.id))

    else:
        bot.send_message(messange.chat.id, 
            text="Такой команды нет")

if ClientError == False:
    print("\nStarted")
elif ClientError == True:
    print(Fore.LIGHTYELLOW_EX + "\nStarted with errors:\nClient error = " + str(ClientError))
print(Fore.LIGHTCYAN_EX + "==================-DEBUG-===================")

bot.infinity_polling()
