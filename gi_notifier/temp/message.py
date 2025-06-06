from datetime import datetime

from ..models import Resin
from .resin_management import week_escoffier, week_skirk

CHARACTERS = ["skirk", "escoffier"]
WEEKDAY_NAMES = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

TRANSIENT_RESIN = {
    "monday": Resin().transient_resin
}


def todays_notification():
    """
    Generate the message body to be sent by the Telegram bot for today only.
    """
    index = datetime.now().weekday()
    day = WEEKDAY_NAMES[index]

    lines = [f"<b>{day.capitalize()}</b>"]

    lines.append(getattr(week_skirk, day))
    lines.append(getattr(week_escoffier, day))

    if day in TRANSIENT_RESIN:
        lines.append(TRANSIENT_RESIN[day])

    return "\n".join(lines)
