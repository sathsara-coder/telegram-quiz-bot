#!/usr/bin/env python3
"""
Sinhala Commerce Quiz Bot
✔ Sends quizzes automatically at specific times
✔ Keeps quiz order (1 → 2 → 3...)
✔ Supports manual commands
"""

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

# 👉 Track quiz order
current_index = 0


# ✅ Send quiz function (SEQUENTIAL)
async def send_quiz(bot: Bot, count: int = 1) -> None:
    global current_index

    total = len(QUIZZES)

    for _ in range(count):
        if current_index >= total:
            current_index = 0  # reset

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
            logger.error(f"Failed to send quiz: {e}")


# ✅ Scheduled job
async def scheduled_quiz(context: ContextTypes.DEFAULT_TYPE):
    logger.info("⏰ Sending scheduled quizzes...")
    await send_quiz(context.bot, count=5)


# ✅ Commands
async def cmd_start(update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎓 *Sinhala Commerce Quiz Bot*\n\n"
        "Commands:\n"
        "/quiz — Send 1 quiz\n"
        "/quiz5 — Send 5 quizzes\n"
        "/help — Help menu",
        parse_mode="Markdown",
    )


async def cmd_quiz(update, context: ContextTypes.DEFAULT_TYPE):
    await send_quiz(context.bot, count=1)


async def cmd_quiz5(update, context: ContextTypes.DEFAULT_TYPE):
    await send_quiz(context.bot, count=5)


async def cmd_help(update, context: ContextTypes.DEFAULT_TYPE):
    await cmd_start(update, context)


# ✅ Main function
def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    # 👉 Add commands
    application.add_handler(CommandHandler("start", cmd_start))
    application.add_handler(CommandHandler("help", cmd_help))
    application.add_handler(CommandHandler("quiz", cmd_quiz))
    application.add_handler(CommandHandler("quiz5", cmd_quiz5))

    # 👉 Setup scheduler
    tz = pytz.timezone(TIMEZONE)

    for t in QUIZ_TIMES:
        hour, minute = map(int, t.split(":"))

        application.job_queue.run_daily(
            scheduled_quiz,
            time=time(hour=hour, minute=minute, tzinfo=tz),
        )

    logger.info("🤖 Bot is running...")
    application.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
