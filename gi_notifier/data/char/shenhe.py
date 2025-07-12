from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.prosperity import Prosperity


class Shenhe(CharacterBase):
    @property
    def name(self) -> str:
        return "Shenhe"

    @property
    def talent_book(self):
        return Prosperity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Dragonheir's False Fin",
                f"https://genshin-impact.fandom.com/wiki/{quote("Dragonheir's_False_Fin")}",
            ),
            source=Source(
                "Coral Defenders",
                f"https://genshin-impact.fandom.com/wiki/{quote("Coral_Defenders")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Hellfire Butterfly",
                f"https://genshin-impact.fandom.com/wiki/{quote("Hellfire_Butterfly")}",
            ),
            source=Source(
                "Narukami Island: Tenshukaku",
                f"https://genshin-impact.fandom.com/wiki/{quote("Narukami_Island:_Tenshukaku")}",
            ),
        )
