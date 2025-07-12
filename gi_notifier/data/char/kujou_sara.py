from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.elegance import Elegance


class KujouSara(CharacterBase):
    @property
    def name(self) -> str:
        return "Kujou Sara"

    @property
    def talent_book(self):
        return Elegance().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Storm Beads",
                f"https://genshin-impact.fandom.com/wiki/{quote("Storm_Beads")}",
            ),
            source=Source(
                "Thunder Manifestation",
                f"https://genshin-impact.fandom.com/wiki/{quote("Thunder_Manifestation")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Ashen Heart",
                f"https://genshin-impact.fandom.com/wiki/{quote("Ashen_Heart")}",
            ),
            source=Source(
                "Narukami Island: Tenshukaku",
                f"https://genshin-impact.fandom.com/wiki/{quote("Narukami_Island:_Tenshukaku")}",
            ),
        )
