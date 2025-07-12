from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.conflict import Conflict


class Chasca(CharacterBase):
    @property
    def name(self) -> str:
        return "Chasca"

    @property
    def talent_book(self):
        return Conflict().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Ensnaring Gaze",
                f"https://genshin-impact.fandom.com/wiki/{quote("Ensnaring_Gaze")}",
            ),
            source=Source(
                "Tenebrous Papilla",
                f"https://genshin-impact.fandom.com/wiki/{quote("Tenebrous_Papilla")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Silken Feather",
                f"https://genshin-impact.fandom.com/wiki/{quote("Silken_Feather")}",
            ),
            source=Source(
                "The Knave",
                f"https://genshin-impact.fandom.com/wiki/{quote("The_Knave")}",
            ),
        )
