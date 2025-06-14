from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.gold import Gold


class Xingqiu(CharacterBase):
    @property
    def name(self) -> str:
        return "Xingqiu"

    @property
    def talent_book(self):
        return Gold().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Cleansing Heart", f"https://genshin-impact.fandom.com/wiki/{quote("Cleansing_Heart")}"),
            source = Source("Rhodeia of Loch", f"https://genshin-impact.fandom.com/wiki/{quote("Rhodeia_of_Loch")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Tail of Boreas", f"https://genshin-impact.fandom.com/wiki/{quote("Tail_of_Boreas")}"),
            source = Source("Andrius", f"https://genshin-impact.fandom.com/wiki/{quote("Andrius")}")
        )
