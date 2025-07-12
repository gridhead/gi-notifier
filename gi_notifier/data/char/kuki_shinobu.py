from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.elegance import Elegance


class KukiShinobu(CharacterBase):
    @property
    def name(self) -> str:
        return "Kuki Shinobu"

    @property
    def talent_book(self):
        return Elegance().as_material_group()

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
                "Tears of the Calamitous God",
                f"https://genshin-impact.fandom.com/wiki/{quote("Tears_of_the_Calamitous_God")}",
            ),
            source=Source(
                "End of the Oneiric Euthymia",
                f"https://genshin-impact.fandom.com/wiki/{quote("End_of_the_Oneiric_Euthymia")}",
            ),
        )
