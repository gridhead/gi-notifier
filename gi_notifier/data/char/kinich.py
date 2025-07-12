from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.kindling import Kindling


class Kinich(CharacterBase):
    @property
    def name(self) -> str:
        return "Kinich"

    @property
    def talent_book(self):
        return Kindling().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Lightning Prism",
                f"https://genshin-impact.fandom.com/wiki/{quote("Lightning_Prism")}",
            ),
            source=Source(
                "Electro Hypostasis",
                f"https://genshin-impact.fandom.com/wiki/{quote("Electro_Hypostasis")}",
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
