# 📚 Sinhala Commerce Quiz Bot

A Telegram bot that automatically sends Sinhala Commerce quiz questions to your group at scheduled times.

---

## ✅ Features

- Sends native **Telegram quiz polls** (auto-graded by Telegram)
- **Scheduled delivery** — 3 times daily (Morning / Afternoon / Evening)
- **20 ready-made questions** covering Accounting, Business Studies & Economics in Sinhala
- Tracks sent questions — **no repeats** within the same day
- `/quiz` command for instant manual quiz
- Easily **add your own questions** in `quiz_bank.py`

---

## 🚀 Setup (Step-by-Step)

### Step 1 — Create your Telegram Bot

1. Open Telegram → search **@BotFather**
2. Send `/newbot`
3. Enter a name: `Sinhala Commerce Quiz`
4. Enter a username: `SinhalaCommerceQuizBot` (must end in `bot`)
5. Copy the **token** BotFather gives you (looks like `123456:ABC-DEF...`)

---

### Step 2 — Add the Bot to your Group

1. Open your group **"Sinhala Commerce Quizz"**
2. Go to **Add Members** → search your bot's username → Add
3. Make the bot an **Admin** (so it can send polls):
   - Group Settings → Admins → Add Admin → select your bot

---

### Step 3 — Get your Group Chat ID

1. Add **@userinfobot** to the group temporarily
2. Send `/start` in the group
3. It will reply with the group's Chat ID (a negative number like `-1001234567890`)
4. Copy that number

---

### Step 4 — Configure the bot

Open `config.py` and fill in:

```python
BOT_TOKEN    = "YOUR_BOT_TOKEN_HERE"       # From BotFather
GROUP_CHAT_ID = -1001234567890             # Your group's Chat ID

QUIZ_TIMES = [
    "08:00",   # Morning
    "13:00",   # Afternoon
    "19:00",   # Evening
]

TIMEZONE = "Asia/Colombo"   # Sri Lanka (UTC+5:30)
```

---

### Step 5 — Install & Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the bot
python bot.py
```

The bot will now send quizzes automatically at the times you set. Keep the terminal open (or use a server / screen session).

---

## 🖥️ Run 24/7 on a Server (Optional)

To keep the bot always online, use **screen** on a Linux VPS:

```bash
screen -S quizbot
python bot.py
# Press Ctrl+A then D to detach
# Reconnect: screen -r quizbot
```

Or use **systemd** / **PM2** for production deployments.

---

## ➕ Adding Your Own Questions

Open `quiz_bank.py` and add a new dict to the `QUIZZES` list:

```python
{
    "id": 21,                         # Unique number
    "question": "Your question here?",
    "options": [
        "Option A",
        "Option B",
        "Option C",
        "Option D",
    ],
    "correct_option_id": 0,           # 0 = A, 1 = B, 2 = C, 3 = D
    "explanation": "Explanation shown after answering.",
},
```

---

## 📋 Bot Commands

| Command     | Description                    |
|-------------|-------------------------------|
| `/start`    | Show welcome message           |
| `/quiz`     | Send a quiz immediately        |
| `/schedule` | Show today's quiz schedule     |
| `/help`     | Show help message              |

---

## 📁 File Structure

```
telegram-quiz-bot/
├── bot.py          ← Main bot logic & scheduler
├── config.py       ← Your token, chat ID & times  ⚠️ Edit this!
├── quiz_bank.py    ← All quiz questions            ✏️ Add more here
├── requirements.txt
└── README.md
```

---

## ⚠️ Troubleshooting

| Problem | Fix |
|--------|-----|
| Bot not sending | Make sure it's an Admin in the group |
| Wrong chat ID | Use @userinfobot or @RawDataBot in the group |
| Polls not showing | Ensure `type="quiz"` is supported (bot must be admin) |
| Time is wrong | Check `TIMEZONE` in config.py |
