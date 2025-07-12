from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.prosperity import Prosperity


class Gaming(CharacterBase):
    @property
    def name(self) -> str:
        return "Gaming"

    @property
    def talent_book(self):
        return Prosperity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Emperor's Resolution",
                f"https://genshin-impact.fandom.com/wiki/{quote("Emperor's_Resolution")}",
            ),
            source=Source(
                "Emperor of Fire and Iron",
                f"https://genshin-impact.fandom.com/wiki/{quote("Emperor_of_Fire_and_Iron")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Lightless Mass",
                f"https://genshin-impact.fandom.com/wiki/{quote("Lightless_Mass")}",
            ),
            source=Source(
                "All-Devouring Narwhal",
                f"https://genshin-impact.fandom.com/wiki/{quote("All-Devouring_Narwhal")}",
            ),
        )
