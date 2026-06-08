import os
import logging
from aiogram import Bot, Dispatcher, executor, types

# Симуляція коду Telegram-бота для команди UniSuper Star
API_TOKEN = os.getenv('BOT_TOKEN', 'dummy_token_for_practical_6')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Вітаємо у криптоспільноті UniSuper Star! Бот готовий до роботи.")

@dp.message_handler(commands=['signal'])
async def send_signal(message: types.Message):
    # Блок коду, який нібито писав інший член команди (де виник конфлікт при злитті)
    await message.reply("Аналіз ринку завершено. Рекомендація: HOLD.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)