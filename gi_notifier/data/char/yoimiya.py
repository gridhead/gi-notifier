from urllib.parse import quote
from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.transience import Transience


class Yoimiya(CharacterBase):
    @property
    def name(self) -> str:
        return "Yoimiya"

    @property
    def talent_book(self):
        return Transience().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Smoldering Pearl", f"https://genshin-impact.fandom.com/wiki/{quote("Smoldering_Pearl")}"),
            source = Source("Pyro Hypostasis", f"https://genshin-impact.fandom.com/wiki/{quote("Pyro_Hypostasis")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Dragon Lord's Crown", f"https://genshin-impact.fandom.com/wiki/{quote("Dragon_Lord's_Crown")}"),
            source = Source("Beneath the Dragon-Queller", f"https://genshin-impact.fandom.com/wiki/{quote("Beneath_the_Dragon-Queller")}")
        )
