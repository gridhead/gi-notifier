from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.diligence import Diligence


class HuTao(CharacterBase):
    @property
    def name(self) -> str:
        return "Hu Tao"

    @property
    def talent_book(self):
        return Diligence().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Juvenile Jade", f"https://genshin-impact.fandom.com/wiki/{quote("Juvenile_Jade")}"),
            source = Source("Primo Geovishap", f"https://genshin-impact.fandom.com/wiki/{quote("Primo_Geovishap")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Shard of a Foul Legacy", f"https://genshin-impact.fandom.com/wiki/{quote("Shard_of_a_Foul_Legacy")}"),
            source = Source("Enter the Golden House", f"https://genshin-impact.fandom.com/wiki/{quote("Enter_the_Golden_House")}")
        )
