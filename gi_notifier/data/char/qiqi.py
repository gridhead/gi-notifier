from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.prosperity import Prosperity


class Qiqi(CharacterBase):
    @property
    def name(self) -> str:
        return "Qiqi"

    @property
    def talent_book(self):
        return Prosperity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Hoarfrost Core", f"https://genshin-impact.fandom.com/wiki/{quote("Hoarfrost_Core")}"),
            source = Source("Cryo Regisvine", f"https://genshin-impact.fandom.com/wiki/{quote("Cryo_Regisvine")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Tail of Boreas", f"https://genshin-impact.fandom.com/wiki/{quote("Tail_of_Boreas")}"),
            source = Source("Andrius", f"https://genshin-impact.fandom.com/wiki/{quote("Andrius")}")
        )
