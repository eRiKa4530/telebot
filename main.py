import telebot
import random
from evn import TOKEN

bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Да')
button2 = telebot.types.KeyboardButton('Нет')
keyboard.add(button1,button2)


@bot.message_handler(commands=['start','hi'])
def start_function(message):
    msg = bot.send_message(message.chat.id, f'Привет{message.chat.first_name},начнем игру?', reply_markup=keyboard)
    bot.register_callback_query_handler(msg,answer_check)
#     bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAJKK2OhPXA8kY_ioC4nN7S04PXczM6AAAIBAAPANk8TGC5zMKs_LVEsBA')
#     bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAJKcWOhPfSu0GncNiSquy1wXzXOJEwIAAIVAAPANk8TzVamO2GeZOcsBA')
#     bot.send_photo(message.chat.id,'https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/giftcard-email-geode-select-2021?wid=600&hei=600&fmt=png-alpha&.v=1653339397392')
# # @bot.message_handler()
# def echo_all(message):
#         bot.send_message(message.chat.id,message.text)

def answer_check(msg):
   if msg.text == 'Да':
    bot.send_message(msg.chat.id, ' у тебя есть три попытки угдать число от 1 до 10')
    random_number = random.randint(1,10)
    p = 3
    start_game(msg,random_number,p)
   else:
    bot.send_message(msg.chat.id,'Ну и ладно пока')

def start_game(msg,random_number, p): 
    msg = bot.send_message(msg.chat.id,'Выберите число от 1 до 10') 
    bot.register_callback_query_handler(msg, check_func,random_number,p-1)

def check_func(msg,random_number,p) :
    if msg.text == str(random_number):
        bot.send_message(msg.chat.id,'Вы победили!')  
    elif  p == 0 :
        bot.send_message(msg.chat.id,'Вы проиграли ! Число было - {random_number}') 
    else:
        bot.edit_chat_invite_link(msg.chat.id,'Попробуй еще раз , у тебя осталось {p} попыток')
        start_game(msg,random_number,p )        


bot.polling()
