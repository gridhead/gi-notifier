from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.resistance import Resistance


class Razor(CharacterBase):
    @property
    def name(self) -> str:
        return "Razor"

    @property
    def talent_book(self):
        return Resistance().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Lightning Prism", f"https://genshin-impact.fandom.com/wiki/{quote("Lightning_Prism")}"),
            source = Source("Electro Hypostasis", f"https://genshin-impact.fandom.com/wiki/{quote("Electro_Hypostasis")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Dvalin's Claw", f"http://genshin-impact.fandom.com/wiki/{quote("Dvalin's_Claw")}"),
            source = Source("Confront Stormterror", f"https://genshin-impact.fandom.com/wiki/{quote("Confront_Stormterror")}")
        )
