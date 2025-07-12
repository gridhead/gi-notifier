from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.freedom import Freedom


class Klee(CharacterBase):
    @property
    def name(self) -> str:
        return "Klee"

    @property
    def talent_book(self):
        return Freedom().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Everflame Seed",
                f"https://genshin-impact.fandom.com/wiki/{quote("Everflame_Seed")}",
            ),
            source=Source(
                "Pyro Regisvines",
                f"https://genshin-impact.fandom.com/wiki/{quote("Pyro_Regisvines")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Ring of Boreas",
                f"https://genshin-impact.fandom.com/wiki/{quote("Ring_of_Boreas")}",
            ),
            source=Source(
                "Wolf of the North Challenge",
                f"https://genshin-impact.fandom.com/wiki/{quote("Wolf_of_the_North_Challenge")}",
            ),
        )
