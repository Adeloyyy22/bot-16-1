from aiogram import executor
from config import dp
from handlers import fsmAdminMenu, client
import logging
from database import bot_db

async def on_start_up():
    bot_db.sql_create()


client.register_handlers_client(dp)
fsmAdminMenu.register_hendler_fsmAdminMenu(dp)




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start(dp, skip_updates=False , on_startup=(on_start_up))