from datetime import datetime

from . import resin_management
from ..model import Resin


CHARACTERS = ["SKIRK", "ESCOFFIER"]
WEEKDAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

TRANSIENT_RESIN = {
    "Monday": Resin().transient_resin
}


def todays_message():
    """
    Generate the message body to be sent by the Telegram bot for today only.
    """
    index = datetime.now().weekday()
    day = WEEKDAY_NAMES[index]

    lines = [f"<b>{day}</b>"]

    for char in CHARACTERS:
        attr = f"WEEK_{char}_{day.upper()}"
        lines.append(getattr(resin_management, attr, None))

    if day in TRANSIENT_RESIN:
        lines.append(TRANSIENT_RESIN[day])

    return "\n".join(lines)
