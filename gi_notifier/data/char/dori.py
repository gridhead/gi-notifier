from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ingenuity import Ingenuity


class Dori(CharacterBase):
    @property
    def name(self) -> str:
        return "Dori"

    @property
    def talent_book(self):
        return Ingenuity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Thunderclap Fruitcore",
                f"https://genshin-impact.fandom.com/wiki/{quote("Thunderclap_Fruitcore")}",
            ),
            source=Source(
                "Electro Regisvines",
                f"https://genshin-impact.fandom.com/wiki/{quote("Electro_Regisvines")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Bloodjade Branch",
                f"https://genshin-impact.fandom.com/wiki/{quote("Bloodjade_Branch")}",
            ),
            source=Source(
                "Beneath the Dragon-Queller",
                f"https://genshin-impact.fandom.com/wiki/{quote("Beneath_the_Dragon-Queller")}",
            ),
        )
