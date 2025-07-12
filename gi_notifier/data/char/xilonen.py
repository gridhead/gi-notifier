from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.kindling import Kindling


class Xilonen(CharacterBase):
    @property
    def name(self) -> str:
        return "Xilonen"

    @property
    def talent_book(self):
        return Kindling().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Gold-Inscribed Secret Source Core",
                f"https://genshin-impact.fandom.com/wiki/{quote("Gold-Inscribed_Secret_Source_Core")}",
            ),
            source=Source(
                "Secret Source Automaton: Configuration Device",
                f"https://genshin-impact.fandom.com/wiki/{quote("Secret_Source_Automaton:_Configuration_Device")}",
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
