from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.equity import Equity


class Neuvillette(CharacterBase):
    @property
    def name(self) -> str:
        return "Neuvillette"

    @property
    def talent_book(self):
        return Equity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Fontemer Unihorn",
                f"https://genshin-impact.fandom.com/wiki/{quote("Fontemer_Unihorn")}",
            ),
            source=Source(
                "Millennial Pearl Seahorse",
                f"https://genshin-impact.fandom.com/wiki/{quote("Millennial_Pearl_Seahorse")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Everamber",
                f"https://genshin-impact.fandom.com/wiki/{quote("Everamber")}",
            ),
            source=Source(
                "The Realm of Beginnings",
                f"https://genshin-impact.fandom.com/wiki/{quote("The_Realm_of_Beginnings")}",
            ),
        )
