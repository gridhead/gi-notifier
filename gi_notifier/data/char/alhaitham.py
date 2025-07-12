from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ingenuity import Ingenuity


class Alhaitham(CharacterBase):
    @property
    def name(self) -> str:
        return "Alhaitham"

    @property
    def talent_book(self):
        return Ingenuity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Pseudo-Stamens",
                f"https://genshin-impact.fandom.com/wiki/{quote("Pseudo-Stamens")}",
            ),
            source=Source(
                "Setekh Wenut",
                f"https://genshin-impact.fandom.com/wiki/{quote("Setekh_Wenut")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Mirror of Mushin",
                f"https://genshin-impact.fandom.com/wiki/{quote("Mirror_of_Mushin")}",
            ),
            source=Source(
                "Joururi Workshop",
                f"https://genshin-impact.fandom.com/wiki/{quote("Joururi_Workshop")}",
            ),
        )
