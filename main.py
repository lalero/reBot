import telebot
from telebot import types
import yaml

bot = telebot.TeleBot('5844849473:AAEDoV95mmhGduMgtahGepwS7biz5a2BHF0')

file = open('data.txt', encoding='utf-8')
for row in file:
    hello = row
    #print()

with open("dataYaml.yaml", "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)

#print(data)

@bot.message_handler(commands=['start'])
def start(message):
    #markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    text = pageSwitch("startpage")

    #Получение данных из button[i] caption
    buttons = []
    for page in data['Pages']:
       if page['page'] == 'startpage':
          for key, value in page.items():
             if key.startswith('button'):
                buttons.append(value['caption'])
    #print(buttons)

    button1 = types.KeyboardButton(buttons[0])
    button2 = types.KeyboardButton(buttons[1])
    button3 = types.KeyboardButton(buttons[2])
    button4 = types.KeyboardButton(buttons[3])

    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)

    bot.send_message(message.chat.id, text=text.format(message.from_user), reply_markup=markup)
    infoUser(message.from_user.id, message.from_user.username, message.from_user.first_name,
             message.from_user.last_name, message.text)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Установка ОС"):
        photo_path = 'OS.jpg'
        photo = open(photo_path, 'rb')
        bot.send_photo(message.chat.id, photo)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="*Инструкция*", reply_markup=markup)

    elif (message.text == "Монтирование флешки"):

        photo_path = 'mountFlash.jpg'
        photo = open(photo_path, 'rb')
        bot.send_photo(message.chat.id, photo)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #btn1 = types.KeyboardButton("Наш")
        #btn2 = types.KeyboardButton("Не наш")
        back = types.KeyboardButton("Вернуться в главное меню")
        #markup.add(btn1, btn2, back)
        markup.add(back)
        bot.send_message(message.chat.id, text="*Инструкция*", reply_markup=markup)

    elif (message.text == "Установка дистрибутива изделия"):

        photo_path = 'distrib.png'
        photo = open(photo_path, 'rb')
        bot.send_photo(message.chat.id, photo)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton("Наш")
        # btn2 = types.KeyboardButton("Не наш")
        back = types.KeyboardButton("Вернуться в главное меню")
        # markup.add(btn1, btn2, back)
        markup.add(back)
        bot.send_message(message.chat.id, text="*Инструкция*", reply_markup=markup)

    elif (message.text == "Задать вопрос в чате"):
        photo_path = 'questionsChat.jpg'
        photo = open(photo_path, 'rb')
        bot.send_photo(message.chat.id, photo)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton("Наш")
        # btn2 = types.KeyboardButton("Не наш")
        back = types.KeyboardButton("Вернуться в главное меню")
        # markup.add(btn1, btn2, back)
        markup.add(back)
        bot.send_message(message.chat.id, text="В разработке...", reply_markup=markup)

    #elif (message.text == "Наш"):
    #    bot.send_message(message.chat.id, "Правильный ответ, Вы прошли проверку")

    #elif message.text == "Не наш":
    #    bot.send_message(message.chat.id, text="Попался! Шпион!")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        #Повтор функции, потом сделать её отдельно
        buttons = []
        for page in data['Pages']:
            if page['page'] == 'startpage':
                for key, value in page.items():
                    if key.startswith('button'):
                        buttons.append(value['caption'])

        button1 = types.KeyboardButton(buttons[0])
        button2 = types.KeyboardButton(buttons[1])
        button3 = types.KeyboardButton(buttons[2])
        button4 = types.KeyboardButton(buttons[3])

        markup.add(button1)
        markup.add(button2)
        markup.add(button3)
        markup.add(button4)

        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован...")

    infoUser(message.from_user.id, message.from_user.username, message.from_user.first_name,
             message.from_user.last_name, message.text)


def infoUser(idUser, nicknameUser, firstnameUser, lastnameUser, messageUser):
    #print(idUser)
    #print(nicknameUser)
    #print(firstnameUser)
    #print(lastnameUser)
    #print(messageUser)

    file = open("usersLog.txt", "a")
    file.write(str(idUser)+" "+nicknameUser+" "+firstnameUser+" "+lastnameUser+" "+messageUser+'\n')
    file.close()


def pageSwitch(pageName):
    for pageData in data['Pages']:
        if pageData['page'] == pageName:
            text = pageData['text']
            break

    #print(text)
    return text

bot.polling(none_stop=True)