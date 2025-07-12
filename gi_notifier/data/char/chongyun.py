from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.diligence import Diligence


class Chongyun(CharacterBase):
    @property
    def name(self) -> str:
        return "Chongyun"

    @property
    def talent_book(self):
        return Diligence().as_material_group()

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
                "Dvalin's Sigh",
                f"https://genshin-impact.fandom.com/wiki/{quote("Dvalin's_Sigh")}",
            ),
            source=Source(
                "Confront Stormterror",
                f"https://genshin-impact.fandom.com/wiki/{quote("Confront_Stormterror")}",
            ),
        )
