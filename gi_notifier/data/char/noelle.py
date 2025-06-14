from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.resistance import Resistance


class Noelle(CharacterBase):
    @property
    def name(self) -> str:
        return "Noelle"

    @property
    def talent_book(self):
        return Resistance().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Basalt Pillar", f"https://genshin-impact.fandom.com/wiki/{quote("Basalt_Pillar")}"),
            source = Source("Geo Hypostasis", f"https://genshin-impact.fandom.com/wiki/{quote("Geo_Hypostasis")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Dvalin's Claw", f"http://genshin-impact.fandom.com/wiki/{quote("Dvalin's_Claw")}"),
            source = Source("Confront Stormterror", f"https://genshin-impact.fandom.com/wiki/{quote("Confront_Stormterror")}")
        )
