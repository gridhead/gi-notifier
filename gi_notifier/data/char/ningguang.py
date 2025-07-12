from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.prosperity import Prosperity


class Ningguang(CharacterBase):
    @property
    def name(self) -> str:
        return "Ningguang"

    @property
    def talent_book(self):
        return Prosperity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Basalt Pillar", f"https://genshin-impact.fandom.com/wiki/{quote("Basalt_Pillar")}"),
            source = Source("Geo Hypostasis", f"https://genshin-impact.fandom.com/wiki/{quote("Geo_Hypostasis")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Spirit Locket of Boreas", f"https://genshin-impact.fandom.com/wiki/{quote("Spirit_Locket_of_Boreas")}"),
            source = Source("Wolf of the North Challenge", f"https://genshin-impact.fandom.com/wiki/{quote("Wolf_of_the_North_Challenge")}")
        )
