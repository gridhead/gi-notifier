from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ballad import Ballad


class Albedo(CharacterBase):
    @property
    def name(self) -> str:
        return "Albedo"

    @property
    def talent_book(self):
        return Ballad().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Basalt Pillar", f"https://genshin-impact.fandom.com/wiki/{quote("Basalt_Pillar")}"),
            source = Source("Geo Hypostasis", f"https://genshin-impact.fandom.com/wiki/{quote("Geo_Hypostasis")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Tusk of Monoceros Caeli", f"https://genshin-impact.fandom.com/wiki/{quote("Tusk_of_Monoceros_Caeli")}"),
            source = Source("Enter the Golden House", f"https://genshin-impact.fandom.com/wiki/{quote("Enter_the_Golden_House")}")
        )
