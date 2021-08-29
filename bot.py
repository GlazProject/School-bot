from aiogram import executor
from dispatcher import dp
import handlers
import announcements
import asyncio


# all included classes
classes = ['11A', '11M', '11FM', '11I', '10A', '10B', '10V', '10M', '10FM', '10I', '9A', '9B', '9V', '9M', '9FM', '9I' ]

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.create_task(announcements.scheduler())
	executor.start_polling(dp, skip_updates=True)