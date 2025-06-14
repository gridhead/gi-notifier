from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ballad import Ballad


class Mika(CharacterBase):
    @property
    def name(self) -> str:
        return "Mika"

    @property
    def talent_book(self):
        return Ballad().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Pseudo-Stamens", f"https://genshin-impact.fandom.com/wiki/{quote("Pseudo-Stamens")}"),
            source = Source("Setekh Wenut", f"https://genshin-impact.fandom.com/wiki/{quote("Setekh_Wenut")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Mirror of Mushin", f"https://genshin-impact.fandom.com/wiki/{quote("Mirror_of_Mushin")}"),
            source = Source("Joururi Workshop", f"https://genshin-impact.fandom.com/wiki/{quote("Joururi_Workshop")}")
        )
