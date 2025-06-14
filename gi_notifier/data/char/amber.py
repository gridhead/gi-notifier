from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.freedom import Freedom


class Amber(CharacterBase):
    @property
    def name(self) -> str:
        return "Amber"

    @property
    def talent_book(self):
        return Freedom().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Everflame Seed", f"https://genshin-impact.fandom.com/wiki/{quote("Everflame_Seed")}"),
            source = Source("Pyro Regisvines", f"https://genshin-impact.fandom.com/wiki/{quote("Pyro_Regisvines")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Dvalin's Sigh", f"https://genshin-impact.fandom.com/wiki/{quote("Dvalin's_Sigh")}"),
            source = Source("Confront Stormterror", f"https://genshin-impact.fandom.com/wiki/{quote("Confront_Stormterror")}")
        )
