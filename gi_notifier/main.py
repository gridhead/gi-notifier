from asyncio import run
from pathlib import Path as pathtype

from click import Path, command, option

from . import config, runner


@command()
@option("--bottoken", required=True, help="Telegram Bot token")
@option(
    "--timezone",
    required=False,
    default=config.TIMEZONE,
    help="Timezone of the place for running the telegram bot",
)
@option(
    "--database",
    required=False,
    type=Path(dir_okay=False),
    help="Path to the user data JSON file",
)
def main(bottoken: str, timezone: str, database: Path):
    config.BOTTOKEN = bottoken
    config.TIMEZONE = timezone
    if database:
        config.DATA_FILE = pathtype(database)
    run(runner.runner())
