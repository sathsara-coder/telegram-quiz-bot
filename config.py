import os

BOT_TOKEN     = os.environ["BOT_TOKEN"]
GROUP_CHAT_ID = int(os.environ["GROUP_CHAT_ID"])
QUIZ_TIMES = [
    "06:00",   # Morning quiz
    "15:00",   # Afternoon quiz
    "20:00",   # Evening quiz
]

# 4. Your local timezone
#    Full list: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TIMEZONE = "Asia/Colombo"   # Sri Lanka Standard Time (UTC+5:30)
