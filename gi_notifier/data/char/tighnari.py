from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.admonition import Admonition


class Tighnari(CharacterBase):
    @property
    def name(self) -> str:
        return "Tighnari"

    @property
    def talent_book(self):
        return Admonition().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Majestic Hooked Beak", f"https://genshin-impact.fandom.com/wiki/{quote("Majestic_Hooked_Beak")}"),
            source = Source("Jadeplume Terrorshroom", f"https://genshin-impact.fandom.com/wiki/{quote("Jadeplume_Terrorshroom")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("The Meaning of Aeons", f"https://genshin-impact.fandom.com/wiki/{quote("The_Meaning_of_Aeons")}"),
            source = Source("End of the Oneiric Euthymia", f"https://genshin-impact.fandom.com/wiki/{quote("End_of_the_Oneiric_Euthymia")}")
        )
