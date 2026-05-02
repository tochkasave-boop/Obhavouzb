import asyncio
import json
import urllib.request
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import logging
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8792418869:AAG0fDwDh0UkSz_ceEFP4KDr1o-hKsvOAco")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "b0ca82f6eea240f78bb191657260105")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key={b0ca82f6eea240f78bb191657260105}&q={city}&lang=ru"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return json.loads(response.read().decode())
    except:
        return None

def format_weather(data):
    if not data:
        return "❌ Город не найден"
    try:
        location = data["location"]
        current = data["current"]
        city = location["name"]
        country = location["country"]
        temp = current["temp_c"]
        condition = current["condition"]["text"]
        humidity = current["humidity"]
        wind = current["wind_kph"]
        feels_like = current["feelslike_c"]
        emoji = "☀️" if current["is_day"] else "🌙"
        return f"{emoji} <b>{city}, {country}</b>\n\n🌡️ Температура: <b>{temp}°C</b> (ощущается {feels_like}°C)\n🌤️ Условия: {condition}\n💧 Влажность: {humidity}%\n💨 Ветер: {wind} км/ч"
    except:
        return "❌ Ошибка при обработке данных"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("👋 Привет! Я бот для проверки погоды.\n\n/weather <город> - узнать погоду\n\nИли просто напиши название города!", parse_mode="HTML")

@dp.message(Command("weather"))
async def weather_cmd(message: types.Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Укажи город: /weather <город>")
        return
    city = args[1]
    await message.answer(format_weather(get_weather(city)), parse_mode="HTML")

@dp.message()
async def any_message(message: types.Message):
    await message.answer(format_weather(get_weather(message.text)), parse_mode="HTML")

async def main():
    logger.info("🤖 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
