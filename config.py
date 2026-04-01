# ─────────────────────────────────────────────────────────
#  config.py  –  Sinhala Commerce Quiz Bot Configuration
# ─────────────────────────────────────────────────────────

# 1. Get your token from @BotFather on Telegram
BOT_TOKEN = "8780959638:AAExagenvIfix8jxhZIo5tKD9WBrcoM7IUU"

# 2. Your group chat ID (negative number, e.g. -1001234567890)
#    Run /id in the group after adding the bot, or use @userinfobot
GROUP_CHAT_ID = -1001234567890

# 3. Times to send quizzes daily (24-hour format, HH:MM)
#    All times are in the timezone below
QUIZ_TIMES = [
    "08:00",   # Morning quiz
    "13:00",   # Afternoon quiz
    "19:00",   # Evening quiz
]

# 4. Your local timezone
#    Full list: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TIMEZONE = "Asia/Colombo"   # Sri Lanka Standard Time (UTC+5:30)
