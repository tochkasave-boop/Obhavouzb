cat > /mnt/user-data/outputs/weather_bot_fixed.py << 'EOF'
import asyncio
import json
import urllib.request
import urllib.parse
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import logging
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8792418869:AAG0fDwDh0UkSz_ceEFP4KDr1o-hKsvOAco")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "b0ca82f6eea240f78bb191657260105")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_weather(city):
    try:
        city_encoded = urllib.parse.quote(city)
        url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city_encoded}&lang=ru&aqi=no"
        
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data
    except Exception as e:
        logger.error(f"Weather API Error: {e}")
        return None

def format_weather(data):
    if not data:
        return "❌ Город не найден или ошибка API"
    
    try:
        location = data.get("location", {})
        current = data.get("current", {})
        
        city = location.get("name", "Unknown")
        country = location.get("country", "")
        temp = current.get("temp_c", "N/A")
        condition = current.get("condition", {}).get("text", "Unknown")
        humidity = current.get("humidity", "N/A")
        wind = current.get("wind_kph", "N/A")
        feels_like = current.get("feelslike_c", temp)
        is_day = current.get("is_day", 1)
        
        emoji = "☀️" if is_day else "🌙"
        
        message = f"{emoji} <b>{city}, {country}</b>\n\n"
        message += f"🌡️ Температура: <b>{temp}°C</b>\n"
        message += f"Ощущается: {feels_like}°C\n"
        message += f"🌤️ Условия: {condition}\n"
        message += f"💧 Влажность: {humidity}%\n"
        message += f"💨 Ветер: {wind} км/ч"
        
        return message
    except Exception as e:
        logger.error(f"Format Error: {e}")
        return "❌ Ошибка при обработке данных"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Привет! Я бот для проверки погоды.\n\n"
        "📝 Команды:\n"
        "/weather <город> - узнать погоду\n\n"
        "💬 Или просто напиши название города!",
        parse_mode="HTML"
    )

@dp.message(Command("weather"))
async def weather_cmd(message: types.Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("❌ Укажи город: /weather <город>\n\nНапример: /weather Ташкент")
        return
    
    city = args[1]
    await message.answer("⏳ Получаю погоду...")
    
    data = get_weather(city)
    response = format_weather(data)
    await message.answer(response, parse_mode="HTML")

@dp.message()
async def any_message(message: types.Message):
    city = message.text.strip()
    data = get_weather(city)
    response = format_weather(data)
    await message.answer(response, parse_mode="HTML")

async def main():
    logger.info("🤖 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
EOF
cat /mnt/user-data/outputs/weather_bot_fixed.py
