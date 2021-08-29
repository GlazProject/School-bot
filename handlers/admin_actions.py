from time import time
from aiogram import types
from aiogram.types import message, InputFile
from configurator import config
from dispatcher import dp, db
import localization
from sqlighter import SQLighter
from fuzzywuzzy import fuzz
import datetime


# change user data
@dp.message_handler(is_admin=True, commands = ['change_permissions'])
async def admin(message: types.Message):
    msg_get = message.text.split("/change_permissions ", maxsplit = 1)[1]
    msg = msg_get.split(";")
    db.update(msg[0], str(msg[1]), str(msg[2]))
    await message.answer(localization.get_string("change_permission_ok").format(edit_user_data=f"user_id = {msg[0]}\ncase = {msg[1]}\nnew_data = {msg[2]}"))


# comand lisf for admin
@dp.message_handler(is_admin=True, commands = ['admin_help'])
async def admin(message: types.Message):
    await message.answer(localization.get_string("command_list_for_admin"))

# send all users list
@dp.message_handler(is_admin=True, commands = ['all_users'])
async def debug(message: types.Message):
    msg = "<pre>\n"
    msg += "  #   user_id     status  class     name    username      last_view\n"
    i=0
    for de in db.debug():
        if de[1]!="test":
            i+=1
            msg+="\n"
            k = len(str(i))
            while k!=3:
                msg+=" "
                k+=1
            msg+=str(i)+") " + str(de[1])
            k = len(str(de[1]))
            while k!=12:
                msg+=" "
                k+=1
            msg+=str(de[2])
            k = len(str(de[2]))
            while k!=8:
                msg+=" "
                k+=1
            msg+=str(de[3])
            k = len(str(de[3]))
            while k!=7:
                msg+=" "
                k+=1
            msg+=str(de[12])
            k = len(str(de[12]))
            while k!=12:
                msg+=" "
                k+=1
            msg+=str(de[13])
            k = len(str(de[13]))
            while k!=14:
                msg+=" "
                k+=1
            msg+=str(de[14])
    msg+="\n</pre>"
    await message.answer(msg)


@dp.message_handler(is_admin=True, commands = ['get_db'])
async def send_db(message: types.Message):
    doc = InputFile("hom.db", filename="hom.db")
    await message.bot.send_document(chat_id = message.from_user.id, document = doc)