from telegram import Update
from telegram.ext import ContextTypes

from .. import config
from ..data.char import __charmaps__
from ..file import load_data, save_data
from ..util import generate_daily_resin_plan, get_today


async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat_id = update.effective_chat.id

    user_id = str(user.id)
    data = load_data()

    if user_id not in data:
        data[user_id] = {
            "user_id": user.id,
            "chat_bot_id": chat_id,
            "group_bot_id": []
        }
        save_data(data)

    username = user.username or user.full_name
    await update.message.reply_text(f"Hello, {username}! Welcome to the Genshin Impact Resin Planner Bot.")  #noqa: E501
    config.logger.debug(f"User started bot: id={user.id}, username={username} & Chat id={chat_id}")

async def handel_resinplan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.effective_message.reply_text("Please specify a character name, e.g. /ResinPlan Amber")  #noqa: E501

    name = " ".join(context.args).title()
    try:
        character = [__charmaps__.get(name)()]
        today = get_today()
        resin_plan = generate_daily_resin_plan(today, character)

        await update.effective_message.reply_text(resin_plan, parse_mode="HTML")
    except Exception:
        await update.effective_message.reply_text(f"Character '{name}' not found.")
