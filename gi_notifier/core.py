from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from . import conf
from datetime import datetime
from pytz import timezone
from asyncio import Event


async def task():
    sender = Bot(conf.BOTTOKEN)
    text = conf.WEEKDICT.get(datetime.now().weekday())
    await sender.send_message(chat_id=conf.CHATIDEN, text=text, parse_mode="HTML")
    conf.logger.info("Notification sent")


async def schedule():
    schedule_author = AsyncIOScheduler(timezone=timezone(conf.TIMEZONE))
    for iter in conf.HOURLIST:
        schedule_author.add_job(task, trigger="cron", hour=iter, minute=0)
    schedule_author.start()
    try:
        await Event().wait()
    except (KeyboardInterrupt, SystemExit):
        conf.logger.warning("Shutting down")
