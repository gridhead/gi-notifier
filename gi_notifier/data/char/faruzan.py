from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.admonition import Admonition


class Faruzan(CharacterBase):
    @property
    def name(self) -> str:
        return "Faruzan"

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
                "Puppet Strings",
                f"https://genshin-impact.fandom.com/wiki/{quote("Puppet_Strings")}",
            ),
            source=Source(
                "Joururi Workshop",
                f"https://genshin-impact.fandom.com/wiki/{quote("Joururi_Workshop")}",
            ),
        )
