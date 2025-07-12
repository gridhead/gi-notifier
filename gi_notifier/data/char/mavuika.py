from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.contention import Contention


class Mavuika(CharacterBase):
    @property
    def name(self) -> str:
        return "Mavuika"

    @property
    def talent_book(self):
        return Contention().as_material_group()

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
                "Eroded Horn",
                f"https://genshin-impact.fandom.com/wiki/{quote("Eroded_Horn")}",
            ),
            source=Source(
                "Stone Stele Records",
                f"https://genshin-impact.fandom.com/wiki/{quote("Stone_Stele_Records")}",
            ),
        )
