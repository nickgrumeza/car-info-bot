from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os
from scraper import fetch_car_data

# Вставь свой токен бота
TOKEN = os.getenv("7688738879:AAEFD0WuVuRbsW-IsFrfF6i9bYvS4bT_I2s")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Отправьте ссылку на страницу поиска автомобилей")

@dp.message_handler()
async def handle_message(message: types.Message):
    url = message.text
    cars = fetch_car_data(url)
    if cars:
        for car in cars:
            await message.answer_photo(
                car.image_url,
                caption=f"{car.title}\nНетто: {car.price_net}\nБрутто: {car.price_gross}\n"
                        f"Пробег: {car.mileage}\nКоробка: {car.transmission}\nМощность: {car.power}\n"
                        f"Год выпуска: {car.year}\nТопливо: {car.fuel_type}\nВладельцы: {car.owners}"
            )
    else:
        await message.reply("Не удалось найти автомобили на данной странице. Проверьте URL и попробуйте снова.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
