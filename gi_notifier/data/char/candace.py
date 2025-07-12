from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.admonition import Admonition


class Candace(CharacterBase):
    @property
    def name(self) -> str:
        return "Candace"

    @property
    def talent_book(self):
        return Admonition().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Light Guiding Tetrahedron",
                f"https://genshin-impact.fandom.com/wiki/{quote("Light_Guiding_Tetrahedron")}",
            ),
            source=Source(
                "Algorithm of Semi-Intransient Matrix of Overseer Network",
                f"https://genshin-impact.fandom.com/wiki/{quote("Algorithm_of_Semi-Intransient_Matrix_of_Overseer_Network")}",
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
