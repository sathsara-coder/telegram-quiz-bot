#!/usr/bin/env python3
"""
Sinhala Commerce Quiz Bot
Sends 5 quizzes on startup. Use /quiz to send more anytime.
"""

import asyncio
import logging
import random

from telegram import Bot
from telegram.ext import Application, CommandHandler, ContextTypes

from config import BOT_TOKEN, GROUP_CHAT_ID
from quiz_bank import QUIZZES

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

sent_today: set = set()


async def send_quiz(bot: Bot, count: int = 1) -> None:
    global sent_today

    for _ in range(count):
        available = [q for q in QUIZZES if q["id"] not in sent_today]
        if not available:
            sent_today.clear()
            available = QUIZZES
            logger.info("Pool reset.")

        quiz = random.choice(available)
        sent_today.add(quiz["id"])

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
            logger.info(f"Sent quiz id={quiz['id']}: {quiz['question'][:60]}...")
            await asyncio.sleep(2)
        except Exception as e:
            logger.error(f"Failed to send quiz: {e}")


async def send_startup_quizzes(application: Application) -> None:
    logger.info("Sending 5 startup quizzes...")
    await send_quiz(application.bot, count=5)


async def cmd_start(update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🎓 *Sinhala Commerce Quiz Bot*\n\n"
        "Commands:\n"
        "/quiz — Send a quiz now\n"
        "/quiz5 — Send 5 quizzes now\n"
        "/help — Show this message",
        parse_mode="Markdown",
    )

async def cmd_quiz(update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_quiz(context.bot, count=1)

async def cmd_quiz5(update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_quiz(context.bot, count=5)

async def cmd_help(update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await cmd_start(update, context)


def main() -> None:
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(send_startup_quizzes)
        .build()
    )

    application.add_handler(CommandHandler("start", cmd_start))
    application.add_handler(CommandHandler("help", cmd_help))
    application.add_handler(CommandHandler("quiz", cmd_quiz))
    application.add_handler(CommandHandler("quiz5", cmd_quiz5))

    logger.info("Bot is running...")
    application.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
