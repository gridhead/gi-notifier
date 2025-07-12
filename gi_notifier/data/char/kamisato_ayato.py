from urllib.parse import quote
from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.elegance import Elegance


class KamisatoAyato(CharacterBase):
    @property
    def name(self) -> str:
        return "Kamisato Ayato"

    @property
    def talent_book(self):
        return Elegance().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Dew of Repudiation", f"https://genshin-impact.fandom.com/wiki/{quote("Dew_of_Repudiation")}"),
            source = Source("Hydro Hypostases", f"https://genshin-impact.fandom.com/wiki/{quote("Hydro_Hypostases")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Mudra of the Malefic General", f"https://genshin-impact.fandom.com/wiki/{quote("Mudra_of_the_Malefic_General")}"),
            source = Source("End of the Oneiric Euthymia", f"https://genshin-impact.fandom.com/wiki/{quote("End_of_the_Oneiric_Euthymia")}")
        )
