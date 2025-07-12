from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.gold import Gold


class Zhongli(CharacterBase):
    @property
    def name(self) -> str:
        return "Zhongli"

    @property
    def talent_book(self):
        return Gold().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Basalt Pillar",
                f"https://genshin-impact.fandom.com/wiki/{quote("Basalt_Pillar")}",
            ),
            source=Source(
                "Geo Hypostasis",
                f"https://genshin-impact.fandom.com/wiki/{quote("Geo_Hypostasis")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Tusk of Monoceros Caeli",
                f"https://genshin-impact.fandom.com/wiki/{quote("Tusk_of_Monoceros_Caeli")}",
            ),
            source=Source(
                "Enter the Golden House",
                f"https://genshin-impact.fandom.com/wiki/{quote("Enter_the_Golden_House")}",
            ),
        )
