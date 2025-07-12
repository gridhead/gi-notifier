from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.freedom import Freedom


class Sucrose(CharacterBase):
    @property
    def name(self) -> str:
        return "Sucrose"

    @property
    def talent_book(self):
        return Freedom().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Hurricane Seed",
                f"https://genshin-impact.fandom.com/wiki/{quote("Hurricane_Seed")}",
            ),
            source=Source(
                "Anemo Hypostasis",
                f"https://genshin-impact.fandom.com/wiki/{quote("Anemo_Hypostasis")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Spirit Locket of Boreas",
                f"https://genshin-impact.fandom.com/wiki/{quote("Spirit_Locket_of_Boreas")}",
            ),
            source=Source(
                "Andrius", f"https://genshin-impact.fandom.com/wiki/{quote("Andrius")}"
            ),
        )
