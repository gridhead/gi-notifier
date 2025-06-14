from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.praxis import Praxis


class Sethos(CharacterBase):
    @property
    def name(self) -> str:
        return "Sethos"

    @property
    def talent_book(self):
        return Praxis().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Cloudseam Scale", f"https://genshin-impact.fandom.com/wiki/{quote("Cloudseam_Scale")}"),
            source = Source("Solitary Suanni", f"https://genshin-impact.fandom.com/wiki/{quote("Solitary_Suanni")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Daka's Bell", f"https://genshin-impact.fandom.com/wiki/{quote("Daka's_Bell")}"),
            source = Source("Joururi Workshop", f"https://genshin-impact.fandom.com/wiki/{quote("Joururi_Workshop")}")
        )
