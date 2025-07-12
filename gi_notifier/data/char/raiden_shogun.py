from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.light import Light


class RaidenShogun(CharacterBase):
    @property
    def name(self) -> str:
        return "Raiden Shogun"

    @property
    def talent_book(self):
        return Light().as_material_group()

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
                "Molten Moment",
                f"https://genshin-impact.fandom.com/wiki/{quote("Molten_Moment")}",
            ),
            source=Source(
                "Narukami Island: Tenshukaku",
                f"https://genshin-impact.fandom.com/wiki/{quote("Narukami_Island:_Tenshukaku")}",
            ),
        )
