from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.diligence import Diligence


class KaedeharaKazuha(CharacterBase):
    @property
    def name(self) -> str:
        return "Kaedehara Kazuha"

    @property
    def talent_book(self):
        return Diligence().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Marionette Core",
                f"https://genshin-impact.fandom.com/wiki/{quote("Marionette_Core")}",
            ),
            source=Source(
                "Maguu Kenki",
                f"https://genshin-impact.fandom.com/wiki/{quote("Maguu_Kenki")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Gilded Scale",
                f"https://genshin-impact.fandom.com/wiki/{quote("Gilded_Scale")}",
            ),
            source=Source(
                "Beneath the Dragon-Queller",
                f"https://genshin-impact.fandom.com/wiki/{quote("Beneath_the_Dragon-Queller")}",
            ),
        )
