from asyncio import run

from click import command, option

from . import conf, core


@command()
@option("--bottoken", required=True)
@option("--chatiden", required=True)
@option("--timezone", required=False, default=conf.TIMEZONE)
def main(bottoken, chatiden, timezone):
    conf.BOTTOKEN = bottoken
    conf.CHATIDEN = chatiden
    conf.TIMEZONE = timezone
    run(core.schedule())
