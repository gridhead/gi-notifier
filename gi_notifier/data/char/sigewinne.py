from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.equity import Equity


class Sigewinne(CharacterBase):
    @property
    def name(self) -> str:
        return "Sigewinne"

    @property
    def talent_book(self):
        return Equity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Water That Failed To Transcend",
                f"https://genshin-impact.fandom.com/wiki/{quote("Water_That_Failed_To_Transcend")}",
            ),
            source=Source(
                "Hydro Tulpa",
                f"https://genshin-impact.fandom.com/wiki/{quote("Hydro_Tulpa")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Lightless Eye of the Maelstrom",
                f"https://genshin-impact.fandom.com/wiki/{quote("Lightless_Eye_of_the_Maelstrom")}",
            ),
            source=Source(
                "All-Devouring Narwhal",
                f"https://genshin-impact.fandom.com/wiki/{quote("All-Devouring_Narwhal")}",
            ),
        )
