from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.justice import Justice


class Furina(CharacterBase):
    @property
    def name(self) -> str:
        return "Furina"

    @property
    def talent_book(self):
        return Justice().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Water That Failed To Transcend",
                f"https://genshin-impact.fandom.com/wiki/{quote("Water_That_Failed_To_Transcend")}",
            ),
            source=Source(
                "Hydro Tulpa",
                f"https://genshin-impact.fandom.com/wiki/{quote("Hydro_Tulpa")}",
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
