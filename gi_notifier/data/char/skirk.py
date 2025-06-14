from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.contention import Contention


class Skirk(CharacterBase):
    @property
    def name(self) -> str:
        return "Skirk"

    @property
    def talent_book(self):
        return Contention().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Ensnaring Gaze", f"https://genshin-impact.fandom.com/wiki/{quote("Ensnaring_Gaze")}"),
            source = Source("Tenebrous Papilla", f"https://genshin-impact.fandom.com/wiki/{quote("Tenebrous_Papilla")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Ascended Sample: Knight", f"https://genshin-impact.fandom.com/wiki/{quote("Ascended_Sample:_Knight")}"),
            source = Source("Unresolved Chess Game", f"https://genshin-impact.fandom.com/wiki/{quote("Unresolved_Chess_Game")}")
        )
