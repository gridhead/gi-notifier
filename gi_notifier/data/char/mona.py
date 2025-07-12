from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.resistance import Resistance


class Mona(CharacterBase):
    @property
    def name(self) -> str:
        return "Mona"

    @property
    def talent_book(self):
        return Resistance().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Cleansing Heart",
                f"https://genshin-impact.fandom.com/wiki/{quote("Cleansing_Heart")}",
            ),
            source=Source(
                "Rhodeia of Loch",
                f"https://genshin-impact.fandom.com/wiki/{quote("Rhodeia_of_Loch")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Ring of Boreas",
                f"https://genshin-impact.fandom.com/wiki/{quote("Ring_of_Boreas")}",
            ),
            source=Source(
                "Wolf of the North Challenge",
                f"https://genshin-impact.fandom.com/wiki/{quote("Wolf_of_the_North_Challenge")}",
            ),
        )
