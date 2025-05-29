from logging import getLogger
from logging.config import dictConfig

from . import temp


BOTTOKEN = ""
CHATIDEN = ""
TIMEZONE = "Asia/Kolkata"

logrconf = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(message)s",
            "datefmt": "[%Y-%m-%d %I:%M:%S %z]",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
}

dictConfig(logrconf)

logger = getLogger(__name__)

HOURLIST = [iter for iter in range(24) if iter % 4 == 0]

WEEK_MONDAY = f"""
<b>Monday</b>
{temp.WEEK_SKIR_MONDAY}
{temp.WEEK_ESCO_MONDAY}
{temp.temp_tran}
"""

WEEK_TUESDAY = f"""
<b>Tuesday</b>
{temp.WEEK_SKIR_TUESDAY}
{temp.WEEK_ESCO_TUESDAY}
"""

WEEK_WEDNESDAY = f"""
<b>Wednesday</b>
{temp.WEEK_SKIR_WEDNESDAY}
{temp.WEEK_ESCO_WEDNESDAY}
"""

WEEK_THURSDAY = f"""
<b>Thursday</b>
{temp.WEEK_SKIR_THURSDAY}
{temp.WEEK_ESCO_THURSDAY}
"""

WEEK_FRIDAY = f"""
<b>Friday</b>
{temp.WEEK_SKIR_FRIDAY}
{temp.WEEK_ESCO_FRIDAY}
"""

WEEK_SATURDAY = f"""
<b>Saturday</b>
{temp.WEEK_SKIR_SATURDAY}
{temp.WEEK_ESCO_SATURDAY}
"""

WEEK_SUNDAY = f"""
<b>Sunday</b>
{temp.WEEK_SKIR_SUNDAY}
{temp.WEEK_ESCO_SUNDAY}
"""

WEEKDICT = {
    0: WEEK_MONDAY,
    1: WEEK_TUESDAY,
    2: WEEK_WEDNESDAY,
    3: WEEK_THURSDAY,
    4: WEEK_FRIDAY,
    5: WEEK_SATURDAY,
    6: WEEK_SUNDAY,
}
