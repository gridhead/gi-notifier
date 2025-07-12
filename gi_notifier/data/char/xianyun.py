from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.gold import Gold


class Xianyun(CharacterBase):
    @property
    def name(self) -> str:
        return "Xianyun"

    @property
    def talent_book(self):
        return Gold().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Cloudseam Scale", f"https://genshin-impact.fandom.com/wiki/{quote("Cloudseam_Scale")}"),
            source = Source("Solitary Suanni", f"https://genshin-impact.fandom.com/wiki/{quote("Solitary_Suanni")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Lightless Eye of the Maelstrom", f"https://genshin-impact.fandom.com/wiki/{quote("Lightless_Eye_of_the_Maelstrom")}"),
            source = Source("All-Devouring Narwhal", f"https://genshin-impact.fandom.com/wiki/{quote("All-Devouring_Narwhal")}")
        )
