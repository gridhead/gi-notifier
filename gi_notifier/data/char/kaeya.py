from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ballad import Ballad


class Kaeya(CharacterBase):
    @property
    def name(self) -> str:
        return "Kaeya"

    @property
    def talent_book(self):
        return Ballad().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Hoarfrost Core",
                f"https://genshin-impact.fandom.com/wiki/{quote("Hoarfrost_Core")}",
            ),
            source=Source(
                "Cryo Regisvine",
                f"https://genshin-impact.fandom.com/wiki/{quote("Cryo_Regisvine")}",
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
                "Wolf of the North Challenge",
                f"https://genshin-impact.fandom.com/wiki/{quote("Wolf_of_the_North_Challenge")}",
            ),
        )
