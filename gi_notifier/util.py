from datetime import datetime

from .models.base import CharacterBase
from .models.models import Resin, Weekday


def get_today() -> Weekday:
    return Weekday(list(Weekday)[datetime.now().weekday()])

def generate_daily_resin_plan(today: Weekday, characters: list[CharacterBase]) -> str:
    message_lines = [f"<b>{today.value}</b>", ""]

    for character in characters:
        message_lines.append(f"<b>For {character.name}</b>\n")
        message_lines.append(character.constant_resource.resin.original_resin.to_use())

        points = []

        if character.is_talent_book_available_today(today):
            points.append(f"1. {character.talent_book.drop.to_obtain()}")
            points.append(f"2. {character.weekly_boss_drop.to_obtain()}")
            points.append(f"3. {character.normal_boss_drop.to_obtain()}")
            points.append(f"4. {character.constant_resource.mora.to_obtain()}")
            points.append(f"5. {character.constant_resource.experience.to_obtain()}")
            points.append(f"6. {character.constant_resource.resin.condensed_resin.to_make()}")
        else:
            points.append(f"1. {character.weekly_boss_drop.to_obtain()}")
            points.append(f"2. {character.normal_boss_drop.to_obtain()}")
            points.append(f"3. {character.constant_resource.mora.to_obtain()}")
            points.append(f"4. {character.constant_resource.experience.to_obtain()}")
            points.append(f"5. {character.constant_resource.resin.condensed_resin.to_make()}")

        message_lines.extend(points)
        message_lines.append("")

    if today.value == "Saturday":
        message_lines.append(Resin().transient_resin.to_claim())

    return "\n".join(message_lines)
