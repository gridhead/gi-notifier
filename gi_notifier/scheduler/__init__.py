from telegram import Bot
from telegram.error import TelegramError

from .. import config
from ..file import load_data
from ..temp import characters
from ..util import generate_daily_resin_plan, get_today


async def scheduled_task():
    sender = Bot(config.BOTTOKEN)
    today = get_today()
    resin_plan = generate_daily_resin_plan(today, characters)

    data = load_data()
    sent_count = 0

    for _, user_info in data.items():
        group_ids = user_info.get("group_bot_id") or []
        dm_chat_id = user_info.get("chat_bot_id")

        targets = group_ids if group_ids else [dm_chat_id]

        for chat_id in targets:
            try:
                await sender.send_message(chat_id=chat_id, text=resin_plan, parse_mode="HTML")
                config.logger.debug(f"Scheduled message sent to chat_id={chat_id}")
                sent_count += 1
            except TelegramError as e:
                config.logger.warning(f"Failed to send message to chat_id={chat_id}: {e}")

    config.logger.debug(f"Scheduled Notification sent to {sent_count} chat(s).")
