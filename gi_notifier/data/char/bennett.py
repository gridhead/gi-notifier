from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.resistance import Resistance


class Bennett(CharacterBase):
    @property
    def name(self) -> str:
        return "Bennett"

    @property
    def talent_book(self):
        return Resistance().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Everflame Seed", f"https://genshin-impact.fandom.com/wiki/{quote("Everflame_Seed")}"),
            source = Source("Pyro Regisvines", f"https://genshin-impact.fandom.com/wiki/{quote("Pyro_Regisvines")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Dvalin's Plume", f"https://genshin-impact.fandom.com/wiki/{quote("Dvalin's_Plume")}"),
            source = Source("Confront Stormterror", f"https://genshin-impact.fandom.com/wiki/{quote("Confront_Stormterror")}")
        )
