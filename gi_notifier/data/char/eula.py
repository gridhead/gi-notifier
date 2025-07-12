from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.resistance import Resistance


class Eula(CharacterBase):
    @property
    def name(self) -> str:
        return "Eula"

    @property
    def talent_book(self):
        return Resistance().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Crystalline Bloom",
                f"https://genshin-impact.fandom.com/wiki/{quote("Crystalline_Bloom")}",
            ),
            source=Source(
                "Cryo Hypostasis",
                f"https://genshin-impact.fandom.com/wiki/{quote("Cryo_Hypostasis")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Dragon Lord's Crown",
                f"https://genshin-impact.fandom.com/wiki/{quote("Dragon_Lord's_Crown")}",
            ),
            source=Source(
                "Beneath the Dragon-Queller",
                f"https://genshin-impact.fandom.com/wiki/{quote("Beneath_the_Dragon-Queller")}",
            ),
        )
