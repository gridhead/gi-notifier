from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.transience import Transience


class ShikanoinHeizou(CharacterBase):
    @property
    def name(self) -> str:
        return "Shikanoin Heizou"

    @property
    def talent_book(self):
        return Transience().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Runic Fang",
                f"https://genshin-impact.fandom.com/wiki/{quote("Runic_Fang")}",
            ),
            source=Source(
                "Ruin Serpent",
                f"https://genshin-impact.fandom.com/wiki/{quote("Ruin_Serpent")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "The Meaning of Aeons",
                f"https://genshin-impact.fandom.com/wiki/{quote("The_Meaning_of_Aeons")}",
            ),
            source=Source(
                "End of the Oneiric Euthymia",
                f"https://genshin-impact.fandom.com/wiki/{quote("End_of_the_Oneiric_Euthymia")}",
            ),
        )
