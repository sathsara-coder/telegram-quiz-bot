import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
GROUP_CHAT_ID = int(os.environ["GROUP_CHAT_ID"])

# Times to send quizzes automatically
QUIZ_TIMES = [
    "06:00",   # Morning
    "15:00",   # Afternoon
    "20:00",   # Evening
]

# Sri Lanka timezone
TIMEZONE = "Asia/Colombo"
