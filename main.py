from aiogram import executor
import handlers
from bot import dp, bot

async def on_startup(dp):
    print('Бот в работе')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)