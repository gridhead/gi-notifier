from asyncio import run

from click import command, option

from . import config, runner


@command()
@option("--bottoken", required=True)
@option("--timezone", required=False, default=config.TIMEZONE)
def main(bottoken, timezone):
    config.BOTTOKEN = bottoken
    config.TIMEZONE = timezone
    run(runner.runner())
