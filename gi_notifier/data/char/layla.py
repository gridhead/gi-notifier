from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ingenuity import Ingenuity


class Layla(CharacterBase):
    @property
    def name(self) -> str:
        return "Layla"

    @property
    def talent_book(self):
        return Ingenuity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Perpetual Caliber", f"https://genshin-impact.fandom.com/wiki/{quote("Perpetual_Caliber")}"),
            source = Source("Aeonblight Drake: Configuration Device", f"https://genshin-impact.fandom.com/wiki/{quote("Aeonblight_Drake")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Mirror of Mushin", f"https://genshin-impact.fandom.com/wiki/{quote("Mirror_of_Mushin")}"),
            source = Source("Joururi Workshop", f"https://genshin-impact.fandom.com/wiki/{quote("Joururi_Workshop")}")
        )
