from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ballad import Ballad


class Venti(CharacterBase):
    @property
    def name(self) -> str:
        return "Venti"

    @property
    def talent_book(self):
        return Ballad().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Hurricane Seed", f"https://genshin-impact.fandom.com/wiki/{quote("Hurricane_Seed")}"),
            source = Source("Anemo Hypostasis", f"https://genshin-impact.fandom.com/wiki/{quote("Anemo_Hypostasis")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Tail of Boreas", f"https://genshin-impact.fandom.com/wiki/{quote("Tail_of_Boreas")}"),
            source = Source("Andrius", f"https://genshin-impact.fandom.com/wiki/{quote("Andrius")}")
        )
