from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.conflict import Conflict


class Kachina(CharacterBase):
    @property
    def name(self) -> str:
        return "Kachina"

    @property
    def talent_book(self):
        return Conflict().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Overripe Flamegranate",
                f"https://genshin-impact.fandom.com/wiki/{quote("Overripe_Flamegranate")}",
            ),
            source=Source(
                "Gluttonous Yumkasaur Mountain King",
                f"https://genshin-impact.fandom.com/wiki/{quote("Gluttonous_Yumkasaur_Mountain_King")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Fading Candle",
                f"https://genshin-impact.fandom.com/wiki/{quote("Fading_Candle")}",
            ),
            source=Source(
                "The Knave",
                f"https://genshin-impact.fandom.com/wiki/{quote("The_Knave")}",
            ),
        )
