from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.freedom import Freedom


class Aloy(CharacterBase):
    @property
    def name(self) -> str:
        return "Aloy"

    @property
    def talent_book(self):
        return Freedom().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Crystalline Bloom",
                f"https://genshin-impact.fandom.com/wiki/{quote("Crystalline_Bloom")}",
            ),
            source=Source(
                "Cryo Hypostasis",
                f"https://genshin-impact.fandom.com/wiki/{quote("Cryo_Hypostasis")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Molten Moment",
                f"https://genshin-impact.fandom.com/wiki/{quote("Molten_Moment")}",
            ),
            source=Source(
                "Narukami Island: Tenshukaku",
                f"https://genshin-impact.fandom.com/wiki/{quote("Narukami_Island:_Tenshukaku")}",
            ),
        )
