import logging

from aiogram import Bot, Dispatcher, executor, types
from checkWord import checkWord

import settings

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать в CheckingBot!")


@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    await message.reply('Чтобы использовать бот отправьте сообщение.')


@dp.message_handler()
async def checkBot(message: types.Message):
    word = message.text
    result = checkWord(word)
    if result['available']:
        response = f'✅ {word.capitalize()}'
    else:
        response = f'❌ {word.capitalize()}\n'
        for text in result['matches']:
            response += f'✅ {text.capitalize()}\n'
    await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
