from dispatcher import dp, db
from configurator import config
import localization
from time import time
import asyncio
import aioschedule as schedule
import datetime
from bot import classes

# clear all homework and noten 
async def clean():
	global classes
	today = datetime.datetime.today().weekday()
	if today != 6:
		for cl in classes:
			db.update(cl, "hw"+str(today),' ')

	today-=1
	if today<0: today = 5
	for cl in classes:
		clas = cl
		db.add_new_rasp(clas, today, "Уроки по расписанию")
		old = str(db.get_lesson(clas, 'status'))
		old = old.replace(str(today),"")
		db.set_upd_rasp(clas, int(old))

# send general announce every
async def announce_general():
	await dp.bot.send_message(
        config.groups.main,
        localization.get_string("announce_2"))

# send cov announce every
async def announce_cov():
	await dp.bot.send_message(
        config.groups.main,
        localization.get_string("announce_3"))


# schedule
async def scheduler():
    schedule.every().day.at("08:00").do(clean)
    

    # loop = asyncio.get_event_loop()
    while True:
        await schedule.run_pending()
        await asyncio.sleep(2)