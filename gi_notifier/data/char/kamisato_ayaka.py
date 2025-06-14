from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.elegance import Elegance


class KamisatoAyaka(CharacterBase):
    @property
    def name(self) -> str:
        return "Kamisato Ayaka"

    @property
    def talent_book(self):
        return Elegance().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Perpetual Heart", f"https://genshin-impact.fandom.com/wiki/{quote("Perpetual_Heart")}"),
            source = Source("Perpetual Mechanical Array", f"https://genshin-impact.fandom.com/wiki/{quote("Perpetual_Mechanical_Array")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Bloodjade Branch", f"https://genshin-impact.fandom.com/wiki/{quote("Bloodjade_Branch")}"),
            source = Source("Beneath the Dragon-Queller", f"https://genshin-impact.fandom.com/wiki/{quote("Beneath_the_Dragon-Queller")}")
        )
