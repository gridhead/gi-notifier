from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.prosperity import Prosperity


class Keqing(CharacterBase):
    @property
    def name(self) -> str:
        return "Keqing"

    @property
    def talent_book(self):
        return Prosperity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Lightning Prism", f"https://genshin-impact.fandom.com/wiki/{quote("Lightning_Prism")}"),
            source = Source("Electro Hypostasis", f"https://genshin-impact.fandom.com/wiki/{quote("Electro_Hypostasis")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Ring of Boreas", f"https://genshin-impact.fandom.com/wiki/{quote("Ring_of_Boreas")}"),
            source = Source("Wolf of the North Challenge", f"https://genshin-impact.fandom.com/wiki/{quote("Wolf_of_the_North_Challenge")}")
        )
