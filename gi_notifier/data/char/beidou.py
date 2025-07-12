from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.gold import Gold


class Beidou(CharacterBase):
    @property
    def name(self) -> str:
        return "Beidou"

    @property
    def talent_book(self):
        return Gold().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Lightning Prism", f"https://genshin-impact.fandom.com/wiki/{quote("Lightning_Prism")}"),
            source = Source("Electro Hypostasis", f"https://genshin-impact.fandom.com/wiki/{quote("Electro_Hypostasis")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Dvalin's Sigh", f"https://genshin-impact.fandom.com/wiki/{quote("Dvalin's_Sigh")}"),
            source = Source("Confront Stormterror", f"https://genshin-impact.fandom.com/wiki/{quote("Confront_Stormterror")}")
        )
