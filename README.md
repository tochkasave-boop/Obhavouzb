# 🌤️ Telegram Weather Bot

Бот для проверки погоды через Telegram с использованием API weatherapi.com

## 🚀 Запуск на Railway (облако)

### 1. Создай GitHub репозиторий
- Зайди на https://github.com
- Нажми "New repository"
- Назови: `weather-bot`
- Сделай Public
- Создай

### 2. Залей файлы на GitHub
```bash
git clone https://github.com/YOUR_USERNAME/weather-bot
cd weather-bot
# Скопируй сюда файлы:
# - weather_bot.py
# - requirements.txt
# - Procfile
# - .gitignore

git add .
git commit -m "Initial commit"
git push origin main
```

### 3. Deploy на Railway
- Зайди на https://railway.app
- Нажми "New Project"
- Выбери "Deploy from GitHub"
- Выбери свой репозиторий
- Нажми Deploy

### 4. Добавь переменные окружения
В Railway → Variables:
```
BOT_TOKEN=8792418869:AAG0fDwDh0UkSz_ceEFP4KDr1o-hKsvOAco
WEATHER_API_KEY=b0ca82f6eea240f78bb191657260105
```

### 5. Готово!
Бот будет работать 24/7 ☁️

---

## 📱 Использование

- `/start` - начало
- `/weather <город>` - погода (например: `/weather Ташкент`)
- Просто напиши город (например: `Москва`)

---

## 🔧 Локальный запуск (Termux)

```bash
mkdir weather_bot
cd weather_bot
# Скопируй файлы сюда

pip install aiogram
python weather_bot.py
```

---

**Made with ❤️**
