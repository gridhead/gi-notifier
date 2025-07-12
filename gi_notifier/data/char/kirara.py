from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.transience import Transience


class Kirara(CharacterBase):
    @property
    def name(self) -> str:
        return "Kirara"

    @property
    def talent_book(self):
        return Transience().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Evergloom Ring",
                f"https://genshin-impact.fandom.com/wiki/{quote("Evergloom_Ring")}",
            ),
            source=Source(
                "Iniquitous Baptist",
                f"https://genshin-impact.fandom.com/wiki/{quote("Iniquitous_Baptist")}",
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
