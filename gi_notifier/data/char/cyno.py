from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.admonition import Admonition


class Cyno(CharacterBase):
    @property
    def name(self) -> str:
        return "Cyno"

    @property
    def talent_book(self):
        return Admonition().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Thunderclap Fruitcore", f"https://genshin-impact.fandom.com/wiki/{quote("Thunderclap_Fruitcore")}"),
            source = Source("Electro Regisvines", f"https://genshin-impact.fandom.com/wiki/{quote("Electro_Regisvines")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Mudra of the Malefic General", f"https://genshin-impact.fandom.com/wiki/{quote("Mudra_of_the_Malefic_General")}"),
            source = Source("End of the Oneiric Euthymia", f"https://genshin-impact.fandom.com/wiki/{quote("End_of_the_Oneiric_Euthymia")}")
        )
