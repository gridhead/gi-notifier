from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.equity import Equity


class Lyney(CharacterBase):
    @property
    def name(self) -> str:
        return "Lyney"

    @property
    def talent_book(self):
        return Equity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Emperor's Resolution",
                f"https://genshin-impact.fandom.com/wiki/{quote("Emperor's_Resolution")}",
            ),
            source=Source(
                "Emperor of Fire and Iron",
                f"https://genshin-impact.fandom.com/wiki/{quote("Emperor_of_Fire_and_Iron")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Primordial Greenbloom",
                f"https://genshin-impact.fandom.com/wiki/{quote("Primordial_Greenbloom")}",
            ),
            source=Source(
                "The Realm of Beginnings",
                f"https://genshin-impact.fandom.com/wiki/{quote("The_Realm_of_Beginnings")}",
            ),
        )
