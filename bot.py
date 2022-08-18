import asyncio
import aioschedule
from aiogram import Bot, Dispatcher, types
import logging
from aiogram.utils import executor, exceptions

from bs import data_from_lxml_using_bs4

API_TOKEN = '5782261045:AAHQu702M4dxeIbkc5wKkaLeU4ELZzMUsdo'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
data = []


async def send_message():
    if len(data) == 0:
        data.extend(data_from_lxml_using_bs4())
        for i in data_from_lxml_using_bs4():
            await bot.send_message('-1001649789391', i)
    else:
        unique = (list(set(data) - set(data_from_lxml_using_bs4())))
        print(f'unique: \n{unique}')
        print(f'data: \n{data}')
        if len(unique) > 0:
            data.extend(unique)
            for i in unique:
                await bot.send_message('-1001649789391', i)


@dp.errors_handler(exception=exceptions.RetryAfter)
async def exception_handler(update: types.Update, exception: exceptions.RetryAfter):
    await bot.send_message('-1001335100202', "wait some time")
    return True


async def scheduler():
    aioschedule.every(15).seconds.do(send_message)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
