from time import time
from aiogram import types
from aiogram.dispatcher.filters import Text
from configurator import config
from dispatcher import dp, db
import localization
import random
from fuzzywuzzy import fuzz
import datetime
from filters import IsPermitUser
from lessonDB import lessons as les


# update last view time
def UPDdLastView(user_id):
    if (str(db.get(user_id, 'last')) != str(datetime.datetime.today().date())):
        db.update_time(user_id, datetime.datetime.today().date())
        clas = db.get(user_id, 'class')
        stat = int(db.get(clas,'statistics'))
        stat += 1
        db.update(clas,'statistics',stat)


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


# goodbye user
@dp.message_handler(commands = ['goodbye'])
async def echo(message: types.Message):
	if (not db.subscriber_exists(message.from_user.id)):
		db.add_subscriber(message.from_user.id, "{0.first_name}".format(message.from_user), message.from_user.username, 3)
		await message.answer(localization.get_string("goodbye_somebody"))
	else:
		db.update_subscription(message.from_user.id, 3)
		await message.answer(localization.get_string("goodbye_user"))


# new user
@dp.message_handler(commands = ['start'])
async def welkome(message: types.Message):
	status = db.get(message.from_user.id, 'status')
	if (not db.subscriber_exists(message.from_user.id)):
		db.add_subscriber(message.from_user.id, "{0.first_name}".format(message.from_user), message.from_user.username, 1)
		# keyboard
		markup = types.InlineKeyboardMarkup(row_width=3)
		item1 = types.InlineKeyboardButton("11", callback_data="11")
		item2 = types.InlineKeyboardButton("10", callback_data="10")
		item3 = types.InlineKeyboardButton("9", callback_data="9")
		markup.add(item1, item2, item3)
		await message.bot.send_sticker(chat_id = message.from_user.id, sticker = "CAACAgIAAxkBAAEJEWpgZ0bGHPRA9txoVm34TkQKVtWsagACBQADwDZPE_lqX5qCa011HgQ")
		await message.answer(localization.get_string("hello_new_user"), reply_markup = markup)
	else:
		if (status == 1 or status == 7 or status == 0 or status == 3):
			await message.bot.send_sticker(chat_id = message.from_user.id, sticker = "CAACAgIAAxkBAAEJEWpgZ0bGHPRA9txoVm34TkQKVtWsagACBQADwDZPE_lqX5qCa011HgQ")
			await message.answer(localization.get_string("hello_old_user"))
		else:
			await message.answer(localization.get_string("acces_denied"))
	await message.answer(localization.get_string("help_command"))


# user change class
@dp.message_handler(commands = ['changeclass'])
async def change(message: types.Message):

	# update last view
	UPDdLastView(message.from_user.id)

	if IsPermitUser(message.from_user.id):
		markup = types.InlineKeyboardMarkup(row_width=3)
		item1 = types.InlineKeyboardButton("11", callback_data="11")
		item2 = types.InlineKeyboardButton("10", callback_data="10")
		item3 = types.InlineKeyboardButton("9", callback_data="9")
		markup.add(item1, item2, item3)
		await message.answer(localization.get_string("select_class"), reply_markup = markup)
	else:
		await message.answer(localization.get_string("access_denied"))


# notice for all classes
@dp.message_handler(commands = ['notice_for_classes'])
async def debug(message: types.Message):

	# update last view
	UPDdLastView(message.from_user.id)

	if IsPermitUser(message.from_user.id):
		esc = types.InlineKeyboardMarkup(row_width=1)
		item1 = types.InlineKeyboardButton("Отмена", callback_data='esc')
		esc.add(item1)
		await message.answer(localization.get_string("notice_for_all_classes"), reply_markup = esc)
		db.update(message.from_user.id, 'add_hw', 900)
	else:
		await message.answer(localization.get_string("access_denied"))


# school contacts
@dp.message_handler(commands = ['contacts'])
async def debug(message: types.Message):
	if IsPermitUser(message.from_user.id):
		await message.answer(localization.get_string("school_contacts"))
	else:
		await message.answer(localization.get_string("access_denied"))


# about teachers
@dp.message_handler(commands = ['teachers'])
async def debug(message: types.Message):
	if IsPermitUser(message.from_user.id):
		await message.answer(localization.get_string("about_teachers"))
	else:
		await message.answer(localization.get_string("access_denied"))


# get help info
@dp.message_handler(commands = ['help'])
async def debug(message: types.Message):
	await message.answer(localization.get_string("help_info"))


# when bot get photo
@dp.message_handler(content_types=['photo'])
async def photo(message: types.Message):

    UPDdLastView(message.from_user.id)

    # photo for all classes
    if db.get(message.from_user.id, 'add_hw') == 900:
        clas = db.get(message.from_user.id, 'class')
        if len(clas) == 3:
            clas = clas[:2]
        elif len(clas) == 2:
            clas = clas[0]
        db.update(message.from_user.id, 'add_hw', 0)
        for send in db.debug():
            if (clas in send[3]) and (send[2]!=6) and (send[2]!=3) and (str(send[1])!=str(message.from_user.id)) and (send[2]!=22):
                if (message.caption):
                    await message.bot.send_photo(send[1], message.photo[0].file_id, caption = "<b><i>Объявление для учеников "+clas+" класса</i></b>\nОт "+ db.get(message.from_user.id, 'name')+ " "+ db.get(message.from_user.id, 'class')+"\n"+message.caption)
                else:
                    await message.bot.send_photo(send[1], message.photo[0].file_id, caption = "<b><i>Объявление для учеников "+clas+" класса</i></b>\nОт "+ db.get(message.from_user.id, 'name')+ " "+ db.get(message.from_user.id, 'class'))
        await message.answer(localization.get_string("notyce_successfuly_sended"))
    
    # photo for homework
    if db.get(message.from_user.id, 'add_hw')//100 == 1:
        clas = db.get(message.from_user.id, 'class')
        today = db.get(message.from_user.id, 'add_hw')%10
        old = db.get(message.from_user.id, "hw"+str(today))
        if (message.caption):
            new = str(old) + "\n➜"+  str(message.photo[0].file_id)+"➜<i>Фото:</i> "+message.caption
        else:
            new = str(old) + "\n➜"+  str(message.photo[0].file_id)+"➜"
        db.update(clas, "hw"+str(today), new)
        db.update(message.from_user.id, 'add_hw', 0)
        await message.answer(localization.get_string("homework_successfuly_added"))
        for send in db.debug():
            if (send[3] == clas) and (send[2]!=6) and (send[2]!=3) and (str(send[1])!=str(message.from_user.id)) and (send[2]!=22):
                await message.bot.send_photo(send[1], message.photo[0].file_id, caption = "<b><i>Добавлено домашнее задание</i></b>\n"+day(today)+"\n"+"для просмотра полного задания посмотрите домашнее задание на этот день недели через главное меню.")

    # photo for lessons list
    elif db.get(message.from_user.id, 'add_hw')//100 == 8:
        clas = db.get(message.from_user.id, 'class')
        today = db.get(message.from_user.id, 'add_hw')%10
        old = str(db.get_lesson(clas, 'status'))
        old += str(today)
        if (message.caption):
            db.add_new_rasp(clas, today, "<b>Изменённое расписание на " + day(today) + "</b>\n➜" +  str(message.photo[0].file_id)+"➜"+message.caption)
        else:
            db.add_new_rasp(clas, today, "<b>Изменённое расписание на " + day(today) + "</b>\n➜" +  str(message.photo[0].file_id))
        db.set_upd_rasp(clas, int(old))
        db.update(message.from_user.id, 'add_hw', 0)
        await message.answer(localization.get_string("lessons_list_successfuly_added"))
        for send in db.debug():
            if (clas in send[3]) and (send[2]!=6) and (send[2]!=3) and (str(send[1])!=str(message.from_user.id)) and (send[2]!=22):
                if (message.caption):
                    await message.bot.send_photo(send[1], message.photo[0].file_id, caption = "<b><i>Изменено расписание на "+day(today)+" </i></b>\n"+message.caption)
                else:
                    await message.bot.send_photo(send[1], message.photo[0].file_id, caption = "<b><i>Изменено расписание на "+day(today)+" </i></b>\n")

    # photo notice for class
    elif db.get(message.from_user.id, 'add_hw') == 300:
        clas = db.get(message.from_user.id, 'class')
        db.update(message.from_user.id, 'add_hw', 0)
        await message.answer(localization.get_string("notyce_successfuly_sended"))
        for send in db.debug():
            if (send[3] == clas) and (send[2]!=6) and (send[2]!=3) and (str(send[1])!=str(message.from_user.id)) and (send[2]!=22):
                if (message.caption):
                    await message.bot.send_photo(send[1], message.photo[0].file_id, caption = "<b><i>Добавлено объявление для вашего класса</i></b>\n"+message.caption)
                else:
                    await message.bot.send_photo(send[1], message.photo[0].file_id, caption = "<b><i>Добавлено объявление для вашего класса</i></b>")

    else:
        await message.answer(localization.get_string("unknow_message"))


# other text messages
@dp.message_handler(content_types = ['text'])
async def send(message: types.Message):
	if db.get(message.from_user.id, 'status')!=6:

		UPDdLastView(message.from_user.id)
		
		# add and delete homework
		if db.get(message.from_user.id, 'add_hw')//100 == 1:
			if "/cls" in message.text.lower():
				clas = db.get(message.from_user.id, 'class')
				today = db.get(message.from_user.id, 'add_hw')%10
				db.update(clas, "hw"+str(today), "")
				db.update(message.from_user.id, 'add_hw', 0)
				await message.answer(localization.get_string("homework_successfuly_deleted"))
			else:
				clas = db.get(message.from_user.id, 'class')
				today = db.get(message.from_user.id, 'add_hw')%10
				old = db.get(message.from_user.id, "hw"+str(today))
				new = str(old) + "\n"+ str(message.text)
				db.update(clas, "hw"+str(today), new)
				db.update(message.from_user.id, 'add_hw', 0)
				await message.answer(localization.get_string("homework_successfuly_added"))
				for send in db.debug():
					if (send[3] == clas) and (send[2]!=6) and (send[2]!=3) and (str(send[1])!=str(message.from_user.id)) and (send[2]!=22):
						await message.bot.send_message(send[1], "<b><i>Добавлено домашнее задание</i></b>\n"+day(today)+"\n"+new)
		
		# notice for all classes
		elif db.get(message.from_user.id, 'add_hw') == 900:
			clas = db.get(message.from_user.id, 'class')
			if len(clas) == 3:
				clas = clas[:2]
			elif len(clas) == 2:
				clas = clas[0]
			db.update(message.from_user.id, 'add_hw', 0)
			for send in db.debug():
				if (clas in send[3]) and (send[2]!=6) and (send[2]!=3) and (str(send[1])!=str(message.from_user.id)) and (send[2]!=22):
					await message.bot.send_message(send[1], "<b><i>Объявление для учеников "+clas+" класса</i></b>\nОт "+ db.get(message.from_user.id, 'name')+ " "+ db.get(message.from_user.id, 'class')+"\n"+message.text)
			await message.answer(localization.get_string("notyce_successfuly_sended"))

		# cerate and delete lessons list
		elif db.get(message.from_user.id, 'add_hw')//100 == 8:
			if "/cls" in message.text.lower():
				clas = db.get(message.from_user.id, 'class')
				today = db.get(message.from_user.id, 'add_hw')%10
				db.add_new_rasp(clas, today, "Уроки по расписанию")
				old = str(db.get_lesson(clas, 'status'))
				old = old.replace(str(today),"")
				db.set_upd_rasp(clas, int(old))
				db.update(message.from_user.id, 'add_hw', 0)
				await message.answer(localization.get_string("lessons_list_successfuly_deleted"))
			else:	
				clas = db.get(message.from_user.id, 'class')
				today = db.get(message.from_user.id, 'add_hw')%10
				old = str(db.get_lesson(clas, 'status'))
				old += str(today)
				db.add_new_rasp(clas, today, "<b>Изменённое расписание на" + day(today) + "</b>\n" + message.text)
				db.set_upd_rasp(clas, int(old))
				db.update(message.from_user.id, 'add_hw', 0)
				await message.answer(localization.get_string("lessons_list_successfuly_added"))
				for send in db.debug():
					if (clas in send[3]) and (send[2]!=6) and (send[2]!=3) and (str(send[1])!=str(message.from_user.id)) and (send[2]!=22):
						await message.bot.send_message(send[1], "<b><i>Изменено расписание на "+day(today)+" </i></b>\n"+message.text)

		# add and delete notice for class
		elif db.get(message.from_user.id, 'add_hw') == 300:
			if "/cls" in message.text.lower():
				clas = db.get(message.from_user.id, 'class')
				db.update(clas, 'noten', "")
				db.update(message.from_user.id, 'add_hw', 0)
				await message.answer(localization.get_string("notyce_successfuly_deleted"))
			else:
				clas = db.get(message.from_user.id, 'class')
				old = db.get(message.from_user.id, 'noten')
				new = str(old)+ "\n" + str(message.text)
				db.update(clas, 'noten', new)
				db.update(message.from_user.id, 'add_hw', 0)
				await message.answer(localization.get_string("notyce_successfuly_added"))
				for send in db.debug():
					if (send[3] == clas) and (send[2]!=6) and (send[2]!=3) and (str(send[1])!=str(message.from_user.id)) and (send[2]!=22):
						await message.bot.send_message(send[1], "<b><i>Добавлено объявление для вашего класса</i></b>\n"+new)

		# unswer for hello
		elif  ('привет' in message.text.lower()) or ('ку' in message.text.lower()) or ('здравству' in message.text.lower()) or (fuzz.ratio(message.text.lower(), 'привет')>50) or (fuzz.ratio(message.text.lower(), 'здравствуй')>50):
			await message.answer(localization.get_string("hello_message"))

		# kniw lessons
		elif (("/lessons" in message.text.lower()) or ("урок" in message.text.lower()) or ("расписани" in message.text.lower()) or ("предмет" in message.text.lower()) or
				(fuzz.ratio(message.text.lower(), 'уроки')>70) or (fuzz.ratio(message.text.lower(), 'расписание')>70) or (fuzz.ratio(message.text.lower(), 'предметы')>70)):
			clas=0
			if ("11а" in message.text.lower()) or ("11 а" in message.text.lower()):
				clas = '11A'
			elif ("11м" in message.text.lower()) or ("11 м" in message.text.lower()):
				clas = '11M'
			elif ("11и" in message.text.lower()) or ("11 и" in message.text.lower()):
				clas = '11I'
			elif ("11фм" in message.text.lower()) or ("11 фм" in message.text.lower()) or ("11ф" in message.text.lower()) or ("11 ф" in message.text.lower()):
				clas = '11FM'

			elif ("10а" in message.text.lower()) or ("10 а" in message.text.lower()):
				clas = '10A'
			elif ("10м" in message.text.lower()) or ("10 м" in message.text.lower()):
				clas = '10M'
			elif ("10и" in message.text.lower()) or ("10 и" in message.text.lower()):
				clas = '10I'
			elif ("10фм" in message.text.lower()) or ("10 фм" in message.text.lower()) or ("10ф" in message.text.lower()) or ("10 ф" in message.text.lower()):
				clas = '10FM'
			elif ("10б" in message.text.lower()) or ("10 б" in message.text.lower()):
				clas = '10B'
			elif ("10в" in message.text.lower()) or ("10 в" in message.text.lower()):
				clas = '10V'

			elif ("9а" in message.text.lower()) or ("9 а" in message.text.lower()):
				clas = '9A'
			elif ("9м" in message.text.lower()) or ("9 м" in message.text.lower()):
				clas = '9M'
			elif ("9и" in message.text.lower()) or ("9 и" in message.text.lower()):
				clas = '9I'
			elif ("9фм" in message.text.lower()) or ("9 фм" in message.text.lower()) or ("9ф" in message.text.lower()) or ("9 ф" in message.text.lower()):
				clas = '9FM'
			elif ("9б" in message.text.lower()) or ("9 б" in message.text.lower()):
				clas = '9B'
			elif ("9в" in message.text.lower()) or ("9 в" in message.text.lower()):
				clas = '9V'

			if clas!=0:
				if ("завтра" in message.text.lower()) or ("понедел" in message.text.lower()) or ("вторн" in message.text.lower()) or ("сред" in message.text.lower()) or ("четвер" in message.text.lower()) or ("пятниц" in message.text.lower()) or ("суббот" in message.text.lower()) or ("вчера" in message.text.lower()):
					today = datetime.datetime.today().weekday()
					if (str(les.lessons(today, message.text.lower(), 3)) in str(db.get_upd_rasp(clas))):
						msg = "<b>Расписание "+clas.lower()+" класса</b>\n" + db.get_lesson(clas, les.lessons(today, message.text.lower(), 2))
						if "➜" in msg:
							msg = msg.split("➜")
							if len(msg) == 3:
								await message.bot.send_photo(message.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
							else:
								await message.bot.send_photo(message.from_user.id, msg[1], caption = msg[0])
						else:
							await message.answer(msg)
					else:
						msg = "<b>Расписание "+clas+" класса</b>\n" + db.get_lesson(clas, les.lessons(today, message.text.lower(), 0))
						time_lesson_show = types.InlineKeyboardMarkup(row_width=1)
						item1 = types.InlineKeyboardButton("Показать время", callback_data='show_time')
						time_lesson_show.add(item1)
						await message.answer(msg,  reply_markup=time_lesson_show)
				else:
					await message.answer("<b>Расписание "+clas.lower()+" класса</b>")
					for i in range (0,6):
						if str(i) in str(db.get_upd_rasp(clas)):
							msg = day(i)+"\n" + db.get_lesson(clas, les.lessons(i, "", 2))
							if "➜" in msg:
								msg = msg.split("➜")
								if len(msg) == 3:
									await message.bot.send_photo(message.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
								else:
									await message.bot.send_photo(message.from_user.id, msg[1], caption = msg[0])
							else:
								await message.answer(msg)
						else: 
							msg = db.get_lesson(clas, les.lessons(i, "", 0))
							await message.answer(msg)
			
			# for your class
			else:
				if ("завтра" in message.text.lower()) or ("понедел" in message.text.lower()) or ("вторн" in message.text.lower()) or ("сред" in message.text.lower()) or ("четвер" in message.text.lower()) or ("пятниц" in message.text.lower()) or ("суббот" in message.text.lower()) or ("вчера" in message.text.lower()):
					today = datetime.datetime.today().weekday()
					clas = db.get(message.from_user.id, 'class')
					await message.answer("<b>Уведомление для учеников " + clas.lower()+" класса</b>\n" + str(db.get(message.from_user.id, 'noten')))
					if (str(les.lessons(today, message.text.lower(), 3)) in str(db.get_upd_rasp(clas))):
						msg = db.get_lesson(clas, les.lessons(today, message.text.lower(), 2))
						if "➜" in msg:
							msg = msg.split("➜")
							if len(msg) == 3:
								await message.bot.send_photo(message.from_user.id, msg[1], caption = msg[0]+"\n"+msg[2])
							else:
								await message.bot.send_photo(message.from_user.id, msg[1], caption = msg[0])
						else:
							await message.answer(msg)
					else:
						msg = db.get_lesson(clas, les.lessons(today, message.text.lower(), 0))
						time_lesson_show = types.InlineKeyboardMarkup(row_width=1)
						item1 = types.InlineKeyboardButton("Показать время", callback_data='show_time')
						time_lesson_show.add(item1)
						await message.answer(msg, reply_markup=time_lesson_show)
				else:
					clas = db.get(message.from_user.id, 'class')
					lessons = types.InlineKeyboardMarkup(row_width=2, row_height = 2)
					item1 = types.InlineKeyboardButton("На сегодня", callback_data='l_today')
					item2 = types.InlineKeyboardButton("На завтра", callback_data='l_tomorrow')
					item3 = types.InlineKeyboardButton("На другой день недели", callback_data='l_other_day')
					lessons.add(item1, item2, item3)
					await message.answer("<b>Уведомление для учеников " + str(clas)+" класса</b>\n" + str(db.get(message.from_user.id, 'noten')))
					await message.answer(localization.get_string("get_lessons"), reply_markup=lessons)

		# homework
		elif (  ("/homework" in message.text.lower()) or ("дз" in message.text.lower()) or ("домаш" in message.text.lower()) or ("зада" in message.text.lower()) or
				(fuzz.ratio(message.text.lower(), 'домашнее')>70) or (fuzz.ratio(message.text.lower(), 'задание')>70) or (fuzz.ratio(message.text.lower(), 'задали')>70)):
			homework = types.InlineKeyboardMarkup(row_width = 1, row_height=2)
			item1 = types.InlineKeyboardButton("Узнать задание", callback_data='know_hw')
			item2 = types.InlineKeyboardButton("Добавить задание", callback_data='add_hw')
			homework.add(item1, item2)
			clas = db.get(message.from_user.id, 'class')
			await message.answer("<b>Уведомление для учеников " + str(clas)+" класса</b>\n" + str(db.get(message.from_user.id, 'noten')))
			await message.answer(localization.get_string("what_du_you_want"), reply_markup=homework)
			
		# edit lessons
		elif IsPermitUser(message.from_user.id) and ("/edit_lessons" in message.text.lower()):
			rasp = types.InlineKeyboardMarkup(row_width=2,row_height = 3)
			item1 = types.InlineKeyboardButton("Понедельник", callback_data='e_monday')
			item2 = types.InlineKeyboardButton("Вторник", callback_data='e_tuesday')
			item3 = types.InlineKeyboardButton("Среда", callback_data='e_wednesday')
			item4 = types.InlineKeyboardButton("Четверг", callback_data='e_thursday')
			item5 = types.InlineKeyboardButton("Пятница", callback_data='e_friday')
			item6 = types.InlineKeyboardButton("Суббота", callback_data='e_saturday')
			rasp.add(item1, item4, item2, item5, item3, item6)
			await message.answer(localization.get_string("edit_lessons"), reply_markup = rasp)

		elif IsPermitUser(message.from_user.id) and ((fuzz.ratio(message.text.lower(), 'спасибо')>60) or (fuzz.ratio(message.text.lower(), 'благодарю')>60)):
			await message.answer(localization.get_string("thanks_message"))

		elif IsPermitUser(message.from_user.id):
			await message.answer(localization.get_string("unknow_message"))
		else:
			await message.answer(localization.get_string("access_denied"))
	else:
		await message.answer(localization.get_string("access_denied"))
