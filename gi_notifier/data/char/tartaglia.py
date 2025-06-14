from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.freedom import Freedom


class Tartaglia(CharacterBase):
    @property
    def name(self) -> str:
        return "Tartaglia"

    @property
    def talent_book(self):
        return Freedom().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Cleansing Heart", f"https://genshin-impact.fandom.com/wiki/{quote("Cleansing_Heart")}"),
            source = Source("Rhodeia of Loch", f"https://genshin-impact.fandom.com/wiki/{quote("Rhodeia_of_Loch")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Shard of a Foul Legacy", f"https://genshin-impact.fandom.com/wiki/{quote("Shard_of_a_Foul_Legacy")}"),
            source = Source("Enter the Golden House", f"https://genshin-impact.fandom.com/wiki/{quote("Enter_the_Golden_House")}")
        )
