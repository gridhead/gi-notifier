from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.contention import Contention


class Iansan(CharacterBase):
    @property
    def name(self) -> str:
        return "Iansan"

    @property
    def talent_book(self):
        return Contention().as_material_group()

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
                "Denial and Judgment",
                f"https://genshin-impact.fandom.com/wiki/{quote("Denial_and_Judgment")}",
            ),
            source=Source(
                "The Knave",
                f"https://genshin-impact.fandom.com/wiki/{quote("The_Knave")}",
            ),
        )
