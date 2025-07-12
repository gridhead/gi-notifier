from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.diligence import Diligence


class Xiangling(CharacterBase):
    @property
    def name(self) -> str:
        return "Xiangling"

    @property
    def talent_book(self):
        return Diligence().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Everflame Seed", f"https://genshin-impact.fandom.com/wiki/{quote("Everflame_Seed")}"),
            source = Source("Pyro Regisvine", f"https://genshin-impact.fandom.com/wiki/{quote("Pyro_Regisvine")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Dvalin's Claw", f"http://genshin-impact.fandom.com/wiki/{quote("Dvalin's_Claw")}"),
            source = Source("Confront Stormterror", f"https://genshin-impact.fandom.com/wiki/{quote("Confront_Stormterror")}")
        )
