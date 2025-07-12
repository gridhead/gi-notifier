from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.conflict import Conflict


class Varesa(CharacterBase):
    @property
    def name(self) -> str:
        return "Varesa"

    @property
    def talent_book(self):
        return Conflict().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Sparkless Statue Core",
                f"https://genshin-impact.fandom.com/wiki/{quote("Sparkless_Statue_Core")}",
            ),
            source=Source(
                "Lava Dragon Statue",
                f"https://genshin-impact.fandom.com/wiki/{quote("Lava_Dragon_Statue")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Eroded Scale-Feather",
                f"https://genshin-impact.fandom.com/wiki/{quote("Eroded_Scale-Feather")}",
            ),
            source=Source(
                "Lord of Eroded Primal Fire",
                f"https://genshin-impact.fandom.com/wiki/{quote("Lord_of_Eroded_Primal_Fire")}",
            ),
        )
