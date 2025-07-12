from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.prosperity import Prosperity


class Yelan(CharacterBase):
    @property
    def name(self) -> str:
        return "Yelan"

    @property
    def talent_book(self):
        return Prosperity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Runic Fang",
                f"https://genshin-impact.fandom.com/wiki/{quote("Runic_Fang")}",
            ),
            source=Source(
                "Ruin Serpent",
                f"https://genshin-impact.fandom.com/wiki/{quote("Ruin_Serpent")}",
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
