#RuFa 1.7-b
#Библиотеки
import telebot
from telebot import types
from win10toast import ToastNotifier
import os

n = ToastNotifier() 

#Файл с api_token
file1 = open("token.txt", "r")
token = file1.readline()

file2 = open("username.txt", "r")
username = file2.readline()
print(token)

api_token = token
bot = telebot.TeleBot(api_token)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
print("Starting...")

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
    if(messange.text == "func🔙") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="func🔙")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #Кнопки
        btn2 = types.KeyboardButton("Shutdown list📑")
        btn3 = types.KeyboardButton("Infoℹ️")
        btn4 = types.KeyboardButton("Ping🔔")
        btn5 = types.KeyboardButton("Lock🔐")
        btn16 = types.KeyboardButton("Hibernation💾")
        btn17 = types.KeyboardButton("Reboot🔄")
        markup.add(btn2, btn3, btn4, btn5, btn16, btn17)
        bot.send_message(messange.chat.id, 
            text="Привет👋", 
            reply_markup=markup)

#Команда Shutdown list (Выводит список возможных функций shutdown)
    elif(messange.text == "Shutdown list📑") and messange.from_user.first_name == username:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #Кнопки
        btn6 = types.KeyboardButton("🔴SD 5m⏳")
        btn7 = types.KeyboardButton("🔴SD 20m⏳")
        btn8 = types.KeyboardButton("🔴SD 1h⏳")
        btn9 = types.KeyboardButton("🔴SD 2h⏳")
        btn10 = types.KeyboardButton("🔴SD 3h⏳")
        btn11 = types.KeyboardButton("🔴SD 4h⏳")
        btn12 = types.KeyboardButton("🔴SD 5h⏳")
        btn13 = types.KeyboardButton("🔴Shutdown🔴")
        btn14 = types.KeyboardButton("⛔️Stop it⛔️")
        btn15 = types.KeyboardButton("func🔙")
        markup.add(btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15)
        bot.send_message(messange.chat.id, 
            text="👇Выберите функцию👇", 
            reply_markup=markup)
    
    #Функция Ping (Отправляет запрос на Windows машину)
    elif(messange.text == "Ping🔔") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="Act🔔")
        n.show_toast("Rufa", "You pinged", duration = 10, icon_path ="rufa.ico")
    
    #Функция Lock (Блокирует Windows машину)
    elif(messange.text == "Lock🔐") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="Locked")
        os.system('RunDll32.exe user32.dll,LockWorkStation')
    
    #Функция SD 5m (Выключает Windows машину через 5 минут)
    elif(messange.text == "🔴SD 5m⏳") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="Shutdown after 5 minutes⏳")
        os.system('shutdown.exe -s -t 300')
    
    #Функция SD 20m (Выключает Windows машину через 20 минут)
    elif(messange.text == "🔴SD 20m⏳") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="Shutdown after 20 minutes⏳")
        os.system('shutdown.exe -s -t 1200')
    
    #Функция SD 1h (Выключает Windows машину через 1 час)
    elif(messange.text == "🔴SD 1h⏳") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="Shutdown after 1 hours⏳")
        os.system('shutdown.exe -s -t 3600')  
    
    #Функция SD 2h (Выключает Windows машину через 2 часа)
    elif(messange.text == "🔴SD 2h⏳") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="Shutdown after 2 hours⏳")
        os.system('shutdown.exe -s -t 7200')
    
    #Функция SD 3h (Выключает Windows машину через 3 часа)
    elif(messange.text == "🔴SD 3h⏳") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="Shutdown after 3 hours⏳")
        os.system('shutdown.exe -s -t 10800')
    
    #Функция SD 4h (Выключает Windows машину через 4 часа)
    elif(messange.text == "🔴SD 4h⏳") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="Shutdown after 4 hours⏳")
        os.system('shutdown.exe -s -t 14400')
    
    #Функция SD 5h (Выключает Windows машину через 5 часов)
    elif(messange.text == "🔴SD 5h⏳") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="Shutdown after 5 hours⏳")
        os.system('shutdown.exe -s -t 18000')
    
    #Функция Shutdown (Моментально выключает Windows машину)
    elif(messange.text == "🔴Shutdown🔴") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="🔴Shutdowning...🔴")
        os.system('shutdown.exe -s -t 5')
    
    #Функция Stop it (Останавливает запланированное выключение)
    elif(messange.text == "⛔️Stop it⛔️") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="Shutdown stoped⛔️")
        os.system('shutdown.exe -a')
    elif(messange.text == "Menu") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="Menu")
        func()
    
    #Функция Гибернация (Моментально вводит машину в режим Гибернации)
    elif(messange.text == "Hibernation💾") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="Hibernate...💾")
        os.system('shutdown.exe /h')

    #Функция Reboot(Моментально перезагружает машину)
    elif(messange.text == "Reboot🔄") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="Rebooting...🔄")
        os.system('shutdown.exe -r -t 5')
        
    #info
    elif(messange.text == "Infoℹ️") and messange.from_user.first_name == username:
        bot.send_message(messange.chat.id, 
            text="RuFa 1.7-b (OPEN SOURCE)\nCreator Demorien\nTelegramBot")
    else:
        bot.send_message(messange.chat.id, 
            text="Такой команды нет")

print("Started")

bot.infinity_polling()
