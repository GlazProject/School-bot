from filters import IsPermitUser
from time import time
from aiogram import types
from configurator import config
from dispatcher import dp, db
import localization
from sqlighter import SQLighter
from fuzzywuzzy import fuzz
import datetime
from lessonDB import lessons as les

from contextlib import suppress
from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted,
                                      MessageToDeleteNotFound)


# add information for new user
def update_class(clas, id1):
    hw0 = db.get(clas, 'hw0')
    hw1 = db.get(clas, 'hw1')
    hw2 = db.get(clas, 'hw2')
    hw3 = db.get(clas, 'hw3')
    hw4 = db.get(clas, 'hw4')
    hw5 = db.get(clas, 'hw5')
    noten = db.get(clas, 'noten')
    db.update(id1, 'class',clas)
    db.update(clas, 'hw0',hw0)
    db.update(clas, 'hw1',hw1)
    db.update(clas, 'hw2',hw2)
    db.update(clas, 'hw3',hw3)
    db.update(clas, 'hw4',hw4)
    db.update(clas, 'hw5',hw5)
    db.update(clas, 'noten',noten)


# gues weekday
def day(today):
    return{
        0: "<b>Понедельник</b>",
        1: "<b>Вторник</b>",
        2: "<b>Среда</b>",
        3: "<b>Четверг</b>",
        4: "<b>Пятница</b>",
        5: "<b>Суббота</b>",
        6: "<b>Воскресенье</b>",
    }[today]


#
@dp.callback_query_handler()
async def send_random_value(call: types.CallbackQuery):

    # swlect class
    if call.data == '11':
        markup = types.InlineKeyboardMarkup(row_width=2, row_height = 2)
        item1 = types.InlineKeyboardButton("11 A", callback_data="11а")
        item2 = types.InlineKeyboardButton("11 М", callback_data="11м")
        item3 = types.InlineKeyboardButton("11 ФМ", callback_data="11фм")
        item4 = types.InlineKeyboardButton("11 И", callback_data="11и")
        markup.add(item1, item2, item3, item4)
        await call.call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Теперь нужно выбрать букву класса ниже.",reply_markup = markup)
    elif call.data == '10':
        markup = types.InlineKeyboardMarkup(row_width=3, row_height = 2)
        item1 = types.InlineKeyboardButton("10 A", callback_data="10а")
        item2 = types.InlineKeyboardButton("10 Б", callback_data="10б")
        item3 = types.InlineKeyboardButton("10 В", callback_data="10в")
        item4 = types.InlineKeyboardButton("10 М", callback_data="10м")
        item5 = types.InlineKeyboardButton("10 ФМ", callback_data="10фм")
        item6 = types.InlineKeyboardButton("10 И", callback_data="10и")
        markup.add(item1, item2, item3, item4, item5, item6)
        await call.call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Теперь нужно выбрать букву класса ниже.",reply_markup = markup)
    elif call.data == '9':
        markup = types.InlineKeyboardMarkup(row_width=2, row_height = 2)
        item1 = types.InlineKeyboardButton("9 A", callback_data="9а")
        item2 = types.InlineKeyboardButton("9 Б", callback_data="9б")
        item3 = types.InlineKeyboardButton("9 В", callback_data="9в")
        item4 = types.InlineKeyboardButton("9 М", callback_data="9м")
        item5 = types.InlineKeyboardButton("9 ФМ", callback_data="9фм")
        item6 = types.InlineKeyboardButton("9 И", callback_data="9и")
        markup.add(item1, item2, item3, item4, item5, item6)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Теперь нужно выбрать букву класса ниже.",reply_markup = markup)
# 11 classes	
    elif call.data == '11а':
        update_class('11A', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>11 А</b> класса.", parse_mode = "HTML",reply_markup = None)
    elif call.data == '11м':
        update_class('11M', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>11 М</b> класса.", parse_mode = "HTML",reply_markup = None)
    elif call.data == '11фм':
        update_class('11FM', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>11 ФМ</b> класса.", parse_mode = "HTML",reply_markup = None)
    elif call.data == '11и':
        update_class('11I', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>11 И</b> класса.", parse_mode = "HTML",reply_markup = None)

# 10 классы
    elif call.data == '10а':
        update_class('10A', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>10 А</b> класса.", parse_mode = "HTML",reply_markup = None)
    elif call.data == '10б':
        update_class('10B', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>10 Б</b> класса.", parse_mode = "HTML",reply_markup = None)
    elif call.data == '10в':
        update_class('10V', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>10 В</b> класса.", parse_mode = "HTML",reply_markup = None)
    elif call.data == '10м':
        update_class('10M', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>10 М</b> класса.", parse_mode = "HTML",reply_markup = None)
    elif call.data == '10фм':
        update_class('10FM', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>10 ФМ</b> класса.", parse_mode = "HTML",reply_markup = None)
    elif call.data == '10и':
        update_class('10I', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>10 И</b> класса.", parse_mode = "HTML",reply_markup = None)

# 9 классы
    elif call.data == '9а':
        update_class('9A', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>9 А</b> класса.", parse_mode = "HTML",reply_markup = None)
    elif call.data == '9б':
        update_class('9B', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>9 Б</b> класса.", parse_mode = "HTML",reply_markup = None)
    elif call.data == '9в':
        update_class('9V', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>9 В</b> класса.", parse_mode = "HTML",reply_markup = None)
    elif call.data == '9м':
        update_class('9M', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>9 М</b> класса.", parse_mode = "HTML",reply_markup = None)
    elif call.data == '9фм':
        update_class('9FM', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>9 ФМ</b> класса.", parse_mode = "HTML",reply_markup = None)
    elif call.data == '9и':
        update_class('9I', call.from_user.id)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id = call.message.message_id, text = "Добро пожаловать!\nТеперь я знаю, что ты из <b>9 И</b> класса.", parse_mode = "HTML",reply_markup = None)



#	------------------------------ОТМЕНА ОТПРАВКИ УВЕДОМЛЕНИЯ------------------------------
    elif call.data == 'esc':
        db.update(call.from_user.id, 'add_hw', 0)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text = call.message.text, reply_markup = None)
        await call.bot.send_message(call.from_user.id, "Ты отменил(а) отправку.")
#	------------------------------ОТМЕНА ОТПРАВКИ УВЕДОМЛЕНИЯ------------------------------

#	------------------------------РАСПИСАНИЕ------------------------------
    #	На сегодня
    elif call.data == 'l_today':
        today = datetime.datetime.today().weekday()
        clas = db.get(call.from_user.id, 'class')
        if (str(les.lessons(today, "", 3)) in str(db.get_upd_rasp(clas))):
            msg = db.get_lesson(clas, les.lessons(today, "", 2))
            if "➜" in msg:
                msg = msg.split("➜")
                if len(msg) == 3:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
                else:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
        else:
            msg = db.get_lesson(clas, les.lessons(today, "", 0))
            time_lesson_show = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Показать время", callback_data='show_time')
            time_lesson_show.add(item1)
            if "➜" in msg:
                msg = msg.split("➜")
                if len(msg) == 3:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
                else:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
    
    #	На завтра
    elif call.data == 'l_tomorrow':
        today = datetime.datetime.today().weekday()
        clas = db.get(call.from_user.id, 'class')
        if (str(les.lessons(today, "завтра", 3)) in str(db.get_upd_rasp(clas))):
            msg = db.get_lesson(clas, les.lessons(today, "завтра", 2))
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
        else:
            msg = db.get_lesson(clas, les.lessons(today, "завтра", 0))
            time_lesson_show = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Показать время", callback_data='show_time')
            time_lesson_show.add(item1)
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = time_lesson_show)


    #	На другой день
    elif call.data == 'l_other_day':
        lessons = types.InlineKeyboardMarkup(row_width=2,row_height = 3)
        item1 = types.InlineKeyboardButton("Понедельник", callback_data='l_monday')
        item2 = types.InlineKeyboardButton("Вторник", callback_data='l_tuesday')
        item3 = types.InlineKeyboardButton("Среда", callback_data='l_wednesday')
        item4 = types.InlineKeyboardButton("Четверг", callback_data='l_thursday')
        item5 = types.InlineKeyboardButton("Пятница", callback_data='l_friday')
        item6 = types.InlineKeyboardButton("Суббота", callback_data='l_saturday')
        lessons.add(item1, item4, item2, item5, item3, item6)
        msg = "Выбери день, на котрый ты хочешь узнать расписание."
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = lessons)
    
    #	Показать время
    elif call.data == 'show_time':
        time_lesson_hide = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Скрыть время", callback_data='hide_time')
        time_lesson_hide.add(item1)
        today = datetime.datetime.today().weekday()
        clas = db.get(call.from_user.id, 'class')
        msg = ""
        if "11a" in call.message.text.lower(): clas = '11A'; msg+="<b>Расписание 11a класса</b>\n"
        elif "11m" in call.message.text.lower(): clas = '11M'; msg+="<b>Расписание 11m класса</b>\n"
        elif "11fm" in call.message.text.lower(): clas = '11FM'; msg+="<b>Расписание 11fm класса</b>\n"
        elif "11i" in call.message.text.lower(): clas = '11I'; msg+="<b>Расписание 11i класса</b>\n"
        
        elif "10i" in call.message.text.lower(): clas = '10I'; msg+="<b>Расписание 10i класса</b>\n"
        elif "10a" in call.message.text.lower(): clas = '10A'; msg+="<b>Расписание 10a класса</b>\n"
        elif "10b" in call.message.text.lower(): clas = '10B'; msg+="<b>Расписание 10b класса</b>\n"
        elif "10v" in call.message.text.lower(): clas = '10V'; msg+="<b>Расписание 10v класса</b>\n"
        elif "10fm" in call.message.text.lower(): clas = '10FM'; msg+="<b>Расписание 10fm класса</b>\n"
        elif "10m" in call.message.text.lower(): clas = '10M'; msg+="<b>Расписание 10m класса</b>\n"
        
        elif "9i" in call.message.text.lower(): clas = '9I'; msg+="<b>Расписание 9i класса</b>\n"
        elif "9a" in call.message.text.lower(): clas = '9A'; msg+="<b>Расписание 9a класса</b>\n"
        elif "9b" in call.message.text.lower(): clas = '9B'; msg+="<b>Расписание 9b класса</b>\n"
        elif "9v" in call.message.text.lower(): clas = '9V'; msg+="<b>Расписание 9v класса</b>\n"
        elif "9fm" in call.message.text.lower(): clas = '9FM'; msg+="<b>Расписание 9fm класса</b>\n"
        elif "9m" in call.message.text.lower(): clas = '9M'; msg+="<b>Расписание 9m класса</b>\n"
        
        msg += db.get_lesson(clas, les.lessons(today, call.message.text.lower(), 1))
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = time_lesson_hide)		
    
    #	Скрыть время
    elif call.data == 'hide_time':
        time_lesson_show = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Показать время", callback_data='show_time')
        time_lesson_show.add(item1)
        today = datetime.datetime.today().weekday()
        clas = db.get(call.from_user.id, 'class')
        msg = ""
        if "11a" in call.message.text.lower(): clas = '11A'; msg+="<b>Расписание 11a класса</b>\n"
        elif "11m" in call.message.text.lower(): clas = '11M'; msg+="<b>Расписание 11m класса</b>\n"
        elif "11fm" in call.message.text.lower(): clas = '11FM'; msg+="<b>Расписание 11fm класса</b>\n"
        
        elif "10i" in call.message.text.lower(): clas = '10I'; msg+="<b>Расписание 10i класса</b>\n"
        elif "10a" in call.message.text.lower(): clas = '10A'; msg+="<b>Расписание 10a класса</b>\n"
        elif "10b" in call.message.text.lower(): clas = '10B'; msg+="<b>Расписание 10b класса</b>\n"
        elif "10v" in call.message.text.lower(): clas = '10V'; msg+="<b>Расписание 10v класса</b>\n"
        elif "10fm" in call.message.text.lower(): clas = '10FM'; msg+="<b>Расписание 10fm класса</b>\n"
        elif "10m" in call.message.text.lower(): clas = '10M'; msg+="<b>Расписание 10m класса</b>\n"
        
        elif "9i" in call.message.text.lower(): clas = '9I'; msg+="<b>Расписание 9i класса</b>\n"
        elif "9a" in call.message.text.lower(): clas = '9A'; msg+="<b>Расписание 9a класса</b>\n"
        elif "9b" in call.message.text.lower(): clas = '9B'; msg+="<b>Расписание 9b класса</b>\n"
        elif "9v" in call.message.text.lower(): clas = '9V'; msg+="<b>Расписание 9v класса</b>\n"
        elif "9fm" in call.message.text.lower(): clas = '9FM'; msg+="<b>Расписание 9fm класса</b>\n"
        elif "9m" in call.message.text.lower(): clas = '9M'; msg+="<b>Расписание 9m класса</b>\n"
        
        msg += db.get_lesson(clas, les.lessons(today, call.message.text.lower(), 0))
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = time_lesson_show)				
    
    #	На понедельник
    elif call.data == 'l_monday':
        today = datetime.datetime.today().weekday()
        clas = db.get(call.from_user.id, 'class')
        if (str(les.lessons(today, "понедельник", 3)) in str(db.get_upd_rasp(clas))):
            msg = db.get_lesson(clas, les.lessons(today, "понедельник", 2))
            if "➜" in msg:
                msg = msg.split("➜")
                if len(msg) == 3:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
                else:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
        else:
            msg = db.get_lesson(clas, les.lessons(today, "понедельник", 0))
            time_lesson_show = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Показать время", callback_data='show_time')
            time_lesson_show.add(item1)
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = time_lesson_show)
    
    #	На вторник
    elif call.data == 'l_tuesday':
        today = datetime.datetime.today().weekday()
        clas = db.get(call.from_user.id, 'class')
        if (str(les.lessons(today, "вторник", 3)) in str(db.get_upd_rasp(clas))):
            msg = db.get_lesson(clas, les.lessons(today, "вторник", 2))
            if "➜" in msg:
                msg = msg.split("➜")
                if len(msg) == 3:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
                else:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
        else:
            msg = db.get_lesson(clas, les.lessons(today, "вторник", 0))
            time_lesson_show = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Показать время", callback_data='show_time')
            time_lesson_show.add(item1)
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = time_lesson_show)
    
    #	На среду
    elif call.data == 'l_wednesday':
        today = datetime.datetime.today().weekday()
        clas = db.get(call.from_user.id, 'class')
        if (str(les.lessons(today, "среда", 3)) in str(db.get_upd_rasp(clas))):
            msg = db.get_lesson(clas, les.lessons(today, "среда", 2))
            if "➜" in msg:
                msg = msg.split("➜")
                if len(msg) == 3:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
                else:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
        else:
            msg = db.get_lesson(clas, les.lessons(today, "среда", 0))
            time_lesson_show = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Показать время", callback_data='show_time')
            time_lesson_show.add(item1)
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = time_lesson_show)
    
    #	На четверг
    elif call.data == 'l_thursday':
        today = datetime.datetime.today().weekday()
        clas = db.get(call.from_user.id, 'class')
        if (str(les.lessons(today, "четверг", 3)) in str(db.get_upd_rasp(clas))):
            msg = db.get_lesson(clas, les.lessons(today, "четверг", 2))
            if "➜" in msg:
                msg = msg.split("➜")
                if len(msg) == 3:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
                else:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
        else:
            msg = db.get_lesson(clas, les.lessons(today, "четверг", 0))
            time_lesson_show = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Показать время", callback_data='show_time')
            time_lesson_show.add(item1)
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = time_lesson_show)
    
    #	На пятницу
    elif call.data == 'l_friday':
        today = datetime.datetime.today().weekday()
        clas = db.get(call.from_user.id, 'class')
        if (str(les.lessons(today, "пятница", 3)) in str(db.get_upd_rasp(clas))):
            msg = db.get_lesson(clas, les.lessons(today, "пятница", 2))
            if "➜" in msg:
                msg = msg.split("➜")
                if len(msg) == 3:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
                else:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
        else:
            msg = db.get_lesson(clas, les.lessons(today, "пятница", 0))
            time_lesson_show = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Показать время", callback_data='show_time')
            time_lesson_show.add(item1)
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = time_lesson_show)
    
    #	На субботу
    elif call.data == 'l_saturday':
        today = datetime.datetime.today().weekday()
        clas = db.get(call.from_user.id, 'class')
        if (str(les.lessons(today, "суббота", 3)) in str(db.get_upd_rasp(clas))):
            msg = db.get_lesson(clas, les.lessons(today, "суббота", 2))
            if "➜" in msg:
                msg = msg.split("➜")
                if len(msg) == 3:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
                else:
                    await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                    await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
        else:
            msg = db.get_lesson(clas, les.lessons(today, "суббота", 0))
            time_lesson_show = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Показать время", callback_data='show_time')
            time_lesson_show.add(item1)
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = time_lesson_show)
#	------------------------------РАСПИСАНИЕ------------------------------



    elif call.data == 'know_hw':
        select_day = types.InlineKeyboardMarkup(row_width=2, row_height = 2)
        item1 = types.InlineKeyboardButton("На сегодня", callback_data='k_today')
        item2 = types.InlineKeyboardButton("На завтра", callback_data='k_tomorrow')
        item3 = types.InlineKeyboardButton("На другой день недели", callback_data='k_other_day')
        select_day.add(item1, item2, item3)
        msg ="Выбери, на когда ты хочешь узнать домашнее задание."
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = select_day)
    
    #	На сегодня
    elif call.data == 'k_today':
        today = datetime.datetime.today().weekday()
        if today == 6: today = 0
        msg = day(today) +"\n"+db.get(call.from_user.id, "hw"+str(today))
        if "➜" in msg:
            msg = msg.split("➜")
            if len(msg) == 3:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
        else:
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
    
    #	На завтра
    elif call.data == 'k_tomorrow':
        today = datetime.datetime.today().weekday()
        today+=1
        if today >= 6: today = 0
        msg = day(today) +"\n"+db.get(call.from_user.id, "hw"+str(today))
        if "➜" in msg:
            msg = msg.split("➜")
            if len(msg) == 3:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
        else:
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
    
    #	На другой день
    elif call.data == 'k_other_day':
        select_day = types.InlineKeyboardMarkup(row_width=2,row_height = 3)
        item1 = types.InlineKeyboardButton("Понедельник", callback_data='k_monday')
        item2 = types.InlineKeyboardButton("Вторник", callback_data='k_tuesday')
        item3 = types.InlineKeyboardButton("Среда", callback_data='k_wednesday')
        item4 = types.InlineKeyboardButton("Четверг", callback_data='k_thursday')
        item5 = types.InlineKeyboardButton("Пятница", callback_data='k_friday')
        item6 = types.InlineKeyboardButton("Суббота", callback_data='k_saturday')
        select_day.add(item1, item4, item2, item5, item3, item6)
        msg = "Выбери день, на котрый ты хочешь узнать задание."
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = select_day)
    
    #	На понедельник
    elif call.data == 'k_monday':
        today = 0
        msg = "<b>Понедельник\n</b>" + str(db.get(call.from_user.id, "hw"+str(today)))
        if "➜" in msg:
            msg = msg.split("➜")
            if len(msg) == 3:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
        else:
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
    
    #	На вторник
    elif call.data == 'k_tuesday':
        today = 1
        msg = "<b>Вторник\n</b>" + str(db.get(call.from_user.id, "hw"+str(today)))
        if "➜" in msg:
            msg = msg.split("➜")
            if len(msg) == 3:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
        else:
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
    
    #	На среду
    elif call.data == 'k_wednesday':
        today = 2
        msg ="<b>Среда\n</b>" + str( db.get(call.from_user.id, "hw"+str(today)))
        if "➜" in msg:
            msg = msg.split("➜")
            if len(msg) == 3:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
        else:
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
    
    #	На четверг
    elif call.data == 'k_thursday':
        today = 3
        msg = "<b>Четверг\n</b>" + str(db.get(call.from_user.id, "hw"+str(today)))
        if "➜" in msg:
            msg = msg.split("➜")
            if len(msg) == 3:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
        else:
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
    
    #	На пятницу
    elif call.data == 'k_friday':
        today = 4
        msg ="<b>Пятница\n</b>" + str(db.get(call.from_user.id, "hw"+str(today)))
        if "➜" in msg:
            msg = msg.split("➜")
            if len(msg) == 3:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
        else:
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
    
    #	На субботу
    elif call.data == 'k_saturday':
        today = 5
        msg = "<b>Суббота\n</b>" + str(db.get(call.from_user.id, "hw"+str(today)))
        if "➜" in msg:
            msg = msg.split("➜")
            if len(msg) == 3:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
            else:
                await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text="Смотри фото", reply_markup = None)
                await call.bot.send_photo(call.from_user.id, msg[1], caption = msg[0])
        else:
            await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = None)
#	------------------------------УЗНАТЬ ДОМАШНЕЕ ЗАДАНИЕ------------------------------


#	------------------------------ДОБАВИТЬ ДОМАШНЕЕ ЗАДАНИЕ------------------------------
    elif IsPermitUser(call.from_user.id) and call.data == 'add_hw':
        select_day = types.InlineKeyboardMarkup(row_width=2,row_height = 2)
        item1 = types.InlineKeyboardButton("На завтра", callback_data='a_tomorrow')
        item2 = types.InlineKeyboardButton("На другой день недели", callback_data='a_other_day')
        item3 = types.InlineKeyboardButton("Создать заметку для своего класса", callback_data='a_note')
        select_day.add(item1, item2, item3)
        msg ="Выбери, на когда ты хочешь добавить задание."
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = select_day)
    
    #	На завтра
    elif call.data == 'a_tomorrow':
        msg = "Ты хочешь добавить задание <b>на завтра</b>.\nОтправь мне в сообщении задание  или фото с подписью к нему НО ТОЛЬКО ОДНО. Чтобы твоим одноклассникам было удобнее, соблюдай формат\nНазвание предмета1: задание по нему\nНазвание предмета2: задание по нему\nДля отмены просто отправь мне пробел\nДля очистка отправь \"/cls\""
        today = datetime.datetime.today().weekday()
        today+=1
        if today >= 6: today = 0
        db.update(call.from_user.id, 'add_hw', 100+today)
        esc = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Отмена", callback_data='esc')
        esc.add(item1)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = esc)
    
    #	На другой день
    elif call.data == 'a_other_day':
        select_day = types.InlineKeyboardMarkup(row_width=2,row_height = 3)
        item1 = types.InlineKeyboardButton("Понедельник", callback_data='a_monday')
        item2 = types.InlineKeyboardButton("Вторник", callback_data='a_tuesday')
        item3 = types.InlineKeyboardButton("Среда", callback_data='a_wednesday')
        item4 = types.InlineKeyboardButton("Четверг", callback_data='a_thursday')
        item5 = types.InlineKeyboardButton("Пятница", callback_data='a_friday')
        item6 = types.InlineKeyboardButton("Суббота", callback_data='a_saturday')
        select_day.add(item1, item4, item2, item5, item3, item6)
        msg = "Выбери день, на котрый ты хочешь добавить задание."
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = select_day)
    
    #	Добавить заметку для класса
    elif call.data == 'a_note':
        msg = "Ты хочешь добавить заметку для своего класса.\nОтправь мне в сообщении ее или фото с подписью к нему НО ТОЛЬКО ОДНО.\nДля отмены отправь мне пробел\nДля очистки - \"/cls\"."
        db.update(call.from_user.id, 'add_hw', 300)
        esc = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Отмена", callback_data='esc')
        esc.add(item1)
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = esc)
    
    #	На понедельник
    elif call.data == 'a_monday':
        db.update(call.from_user.id, 'add_hw', 100)
        esc = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Отмена", callback_data='esc')
        esc.add(item1)
        msg = "Ты хочешь добавить задание <b>на понедельник</b>.\nОтправь мне в сообщении задание или фото с подписью к нему НО ТОЛЬКО ОДНО. Чтобы твоим одноклассникам было удобнее, соблюдай формат\nНазвание предмета1: задание по нему\nНазвание предмета2: задание по нему\nДля отмены просто отправь мне пробел\nДля очистки - \"/cls\"."
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = esc)
    
    #	На вторник
    elif call.data == 'a_tuesday':
        db.update(call.from_user.id, 'add_hw', 101)
        esc = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Отмена", callback_data='esc')
        esc.add(item1)
        msg = "Ты хочешь добавить задание <b>на второник</b>.\nОтправь мне в сообщении задание или фото с подписью к нему НО ТОЛЬКО ОДНО. Чтобы твоим одноклассникам было удобнее, соблюдай формат\nНазвание предмета1: задание по нему\nНазвание предмета2: задание по нему\nДля отмены просто отправь мне пробел\nДля очистки - \"/cls\"."
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = esc)
    
    #	На среду
    elif call.data == 'a_wednesday':
        db.update(call.from_user.id, 'add_hw', 102)
        esc = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Отмена", callback_data='esc')
        esc.add(item1)
        msg = "Ты хочешь добавить задание <b>на среду</b>.\nОтправь мне в сообщении задание или фото с подписью к нему НО ТОЛЬКО ОДНО. Чтобы твоим одноклассникам было удобнее, соблюдай формат\nНазвание предмета1: задание по нему\nНазвание предмета2: задание по нему\nДля отмены просто отправь мне пробел\nДля очистки - \"/cls\"."
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = esc)
    
    #	На четверг
    elif call.data == 'a_thursday':
        db.update(call.from_user.id, 'add_hw', 103)
        esc = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Отмена", callback_data='esc')
        esc.add(item1)
        msg = "Ты хочешь добавить задание <b>на четверг</b>.\nОтправь мне в сообщении задание или фото с подписью к нему НО ТОЛЬКО ОДНО. Чтобы твоим одноклассникам было удобнее, соблюдай формат\nНазвание предмета1: задание по нему\nНазвание предмета2: задание по нему\nДля отмены просто отправь мне пробел\nДля очистки - \"/cls\"."
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = esc)
    
    #	На пятницу
    elif call.data == 'a_friday':
        db.update(call.from_user.id, 'add_hw', 104)
        esc = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Отмена", callback_data='esc')
        esc.add(item1)
        msg = "Ты хочешь добавить задание <b>на пятницу</b>.\nОтправь мне в сообщении задание или фото с подписью к нему НО ТОЛЬКО ОДНО. Чтобы твоим одноклассникам было удобнее, соблюдай формат\nНазвание предмета1: задание по нему\nНазвание предмета2: задание по нему\nДля отмены просто отправь мне пробел\nДля очистки - \"/cls\"."
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = esc)
    
    #	На субботу
    elif call.data == 'a_saturday':
        db.update(call.from_user.id, 'add_hw', 105)
        esc = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Отмена", callback_data='esc')
        esc.add(item1)
        msg = "Ты хочешь добавить задание <b>на субботу</b>.\nОтправь мне в сообщении задание или фото с подписью к нему НО ТОЛЬКО ОДНО. Чтобы твоим одноклассникам было удобнее, соблюдай формат\nНазвание предмета1: задание по нему\nНазвание предмета2: задание по нему\nДля отмены просто отправь мне пробел\nДля очистки - \"/cls\"."
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = esc)
#	------------------------------ДОБАВИТЬ ДОМАШНЕЕ ЗАДАНИЕ------------------------------
    
#	------------------------------ДОБАВИТЬ РАСПИСАНИЕ НА ОДИН ДЕНЬ------------------------------
    elif call.data == 'e_monday':
        db.update(call.from_user.id, 'add_hw', 800)
        esc = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Отмена", callback_data='esc')
        esc.add(item1)
        msg = "Ты хочешь изменить расписание <b>на понедельник</b>.\nОтправь мне в сообщении своё расписание или фото с подписью к нему НО ТОЛЬКО ОДНО.\nДля сброса расписания отправь /cls"
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = esc)
    elif call.data == 'e_tuesday':
        db.update(call.from_user.id, 'add_hw', 801)
        esc = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Отмена", callback_data='esc')
        esc.add(item1)
        msg = "Ты хочешь изменить расписание <b>на вторник</b>.\nОтправь мне в сообщении своё расписание или фото с подписью к нему НО ТОЛЬКО ОДНО.\nДля сброса расписания отправь /cls"
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = esc)
    elif call.data == 'e_wednesday':
        db.update(call.from_user.id, 'add_hw', 802)
        esc = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Отмена", callback_data='esc')
        esc.add(item1)
        msg = "Ты хочешь изменить расписание <b>на среду</b>.\nОтправь мне в сообщении своё расписание или фото с подписью к нему НО ТОЛЬКО ОДНО.\nДля сброса расписания отправь /cls"
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = esc)
    elif call.data == 'e_thursday':
        db.update(call.from_user.id, 'add_hw', 803)
        esc = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Отмена", callback_data='esc')
        esc.add(item1)
        msg = "Ты хочешь изменить расписание <b>на четверг</b>.\nОтправь мне в сообщении своё расписание или фото с подписью к нему НО ТОЛЬКО ОДНО.\nДля сброса расписания отправь /cls"
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = esc)
    elif call.data == 'e_friday':
        db.update(call.from_user.id, 'add_hw', 804)
        esc = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Отмена", callback_data='esc')
        esc.add(item1)
        msg = "Ты хочешь изменить расписание <b>на пятницу</b>.\nОтправь мне в сообщении своё расписание или фото с подписью к нему НО ТОЛЬКО ОДНО.\nДля сброса расписания отправь /cls"
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = esc)
    elif call.data == 'e_saturday':
        db.update(call.from_user.id, 'add_hw', 805)
        esc = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Отмена", callback_data='esc')
        esc.add(item1)
        msg = "Ты хочешь изменить расписание <b>на суботу</b>.\nОтправь мне в сообщении своё расписание или фото с подписью к нему НО ТОЛЬКО ОДНО.\nДля сброса расписания отправь /cls"
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=msg, reply_markup = esc)
#	------------------------------ДОБАВИТЬ РАСПИСАНИЕ НА ОДИН ДЕНЬ------------------------------


    else:
        await call.bot.edit_message_text(chat_id=call.from_user.id, message_id= call.message.message_id, text=localization.get_string("access_denied"), reply_markup = None)