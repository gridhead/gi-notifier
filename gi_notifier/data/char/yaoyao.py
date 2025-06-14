from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.diligence import Diligence


class Yaoyao(CharacterBase):
    @property
    def name(self) -> str:
        return "Yaoyao"

    @property
    def talent_book(self):
        return Diligence().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Quelled Creeper", f"https://genshin-impact.fandom.com/wiki/{quote("Quelled_Creeper")}"),
            source = Source("Dendro Hypostasis", f"https://genshin-impact.fandom.com/wiki/{quote("Dendro_Hypostasis")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Daka's Bell", f"https://genshin-impact.fandom.com/wiki/{quote("Daka's_Bell")}"),
            source = Source("Joururi Workshop", f"https://genshin-impact.fandom.com/wiki/{quote("Joururi_Workshop")}")
        )
