from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.transience import Transience


class SangonomiyaKokomi(CharacterBase):
    @property
    def name(self) -> str:
        return "Sangonomiya Kokomi"

    @property
    def talent_book(self):
        return Transience().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Dew of Repudiation",
                f"https://genshin-impact.fandom.com/wiki/{quote("Dew_of_Repudiation")}",
            ),
            source=Source(
                "Hydro Hypostases",
                f"https://genshin-impact.fandom.com/wiki/{quote("Hydro_Hypostases")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Hellfire Butterfly",
                f"https://genshin-impact.fandom.com/wiki/{quote("Hellfire_Butterfly")}",
            ),
            source=Source(
                "Narukami Island: Tenshukaku",
                f"https://genshin-impact.fandom.com/wiki/{quote("Narukami_Island:_Tenshukaku")}",
            ),
        )
