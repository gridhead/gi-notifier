from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.order import Order


class Wriothesley(CharacterBase):
    @property
    def name(self) -> str:
        return "Wriothesley"

    @property
    def talent_book(self):
        return Order().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Tourbillon Device",
                f"https://genshin-impact.fandom.com/wiki/{quote("\"Tourbillon_Device\"")}",
            ),
            source=Source(
                "Prototype Cal. Breguet",
                f"https://genshin-impact.fandom.com/wiki/{quote("Prototype_Cal._Breguet")}",
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
