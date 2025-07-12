from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.praxis import Praxis


class Collei(CharacterBase):
    @property
    def name(self) -> str:
        return "Collei"

    @property
    def talent_book(self):
        return Praxis().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Majestic Hooked Beak",
                f"https://genshin-impact.fandom.com/wiki/{quote("Majestic_Hooked_Beak")}",
            ),
            source=Source(
                "Jadeplume Terrorshroom",
                f"https://genshin-impact.fandom.com/wiki/{quote("Jadeplume_Terrorshroom")}",
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
