from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.kindling import Kindling


class Citlali(CharacterBase):
    @property
    def name(self) -> str:
        return "Citlali"

    @property
    def talent_book(self):
        return Kindling().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Talisman of the Enigmatic Land",
                f"https://genshin-impact.fandom.com/wiki/{quote("Talisman_of_the_Enigmatic_Land")}",
            ),
            source=Source(
                "Wayward Hermetic Spiritspeaker",
                f"https://genshin-impact.fandom.com/wiki/{quote("Wayward_Hermetic_Spiritspeaker")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Denial and Judgment",
                f"https://genshin-impact.fandom.com/wiki/{quote("Denial_and_Judgment")}",
            ),
            source=Source(
                "The Knave",
                f"https://genshin-impact.fandom.com/wiki/{quote("The_Knave")}",
            ),
        )
