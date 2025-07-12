from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.gold import Gold


class Yanfei(CharacterBase):
    @property
    def name(self) -> str:
        return "Yanfei"

    @property
    def talent_book(self):
        return Gold().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Juvenile Jade", f"https://genshin-impact.fandom.com/wiki/{quote("Juvenile_Jade")}"),
            source = Source("Primo Geovishap", f"https://genshin-impact.fandom.com/wiki/{quote("Primo_Geovishap")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Bloodjade Branch", f"https://genshin-impact.fandom.com/wiki/{quote("Bloodjade_Branch")}"),
            source = Source("Beneath the Dragon-Queller", f"https://genshin-impact.fandom.com/wiki/{quote("Beneath_the_Dragon-Queller")}")
        )
