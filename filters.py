from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from configurator import config
from sqlighter import SQLighter

# Initialize database
database = SQLighter('hom.db')

class IsAdminFilter(BoundFilter):
    """
    Custom class to asdd "is_admin" filter for some handlers below
    """
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        member = message.from_user.id
        return str(member) == config.bot.admin

def IsPermitUser(user_id):
    status = database.get(user_id, 'status')
    if (status == 1 or status == 7 or status == 0):
        return True
    elif (status == 6 or status == 3):
        return False