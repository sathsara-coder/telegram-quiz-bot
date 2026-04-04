#!/usr/bin/env python3

import asyncio
import logging
from datetime import time

import pytz
from telegram import Bot
from telegram.ext import Application, CommandHandler, ContextTypes

from config import BOT_TOKEN, GROUP_CHAT_ID, QUIZ_TIMES, TIMEZONE
from quiz_bank import QUIZZES

# Logging
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ✅ Keep quiz order
current_index = 0


# ✅ Send quiz (SEQUENTIAL)
async def send_quiz(bot: Bot, count: int = 1):
    global current_index

    total = len(QUIZZES)

    for _ in range(count):
        if current_index >= total:
            current_index = 0

        quiz = QUIZZES[current_index]
        current_index += 1

        try:
            await bot.send_poll(
                chat_id=GROUP_CHAT_ID,
                question=f"📚 {quiz['question']}",
                options=quiz["options"],
                type="quiz",
                correct_option_id=quiz["correct_option_id"],
                explanation=quiz.get("explanation", ""),
                is_anonymous=False,
            )
            logger.info(f"Sent quiz id={quiz['id']}")
            await asyncio.sleep(2)

        except Exception as e:
            logger.error(f"Error sending quiz: {e}")


# ✅ Scheduled task
async def scheduled_quiz(context: ContextTypes.DEFAULT_TYPE):
    logger.info("⏰ Auto quiz triggered")
    await send_quiz(context.bot, count=5)


# ✅ Commands
async def cmd_start(update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎓 Sinhala Commerce Quiz Bot\n\n"
        "/quiz - Send 1 quiz\n"
        "/quiz5 - Send 5 quizzes\n"
        "/help - Help",
    )


async def cmd_quiz(update, context: ContextTypes.DEFAULT_TYPE):
    await send_quiz(context.bot, 1)


async def cmd_quiz5(update, context: ContextTypes.DEFAULT_TYPE):
    await send_quiz(context.bot, 5)


async def cmd_help(update, context: ContextTypes.DEFAULT_TYPE):
    await cmd_start(update, context)


# ✅ Main
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("quiz", cmd_quiz))
    app.add_handler(CommandHandler("quiz5", cmd_quiz5))
    app.add_handler(CommandHandler("help", cmd_help))

    # Scheduler
    tz = pytz.timezone(TIMEZONE)

    for t in QUIZ_TIMES:
        h, m = map(int, t.split(":"))

        app.job_queue.run_daily(
            scheduled_quiz,
            time=time(hour=h, minute=m, tzinfo=tz),
        )

    logger.info("✅ Bot running with scheduler...")
    app.run_polling()


if __name__ == "__main__":
    main()
