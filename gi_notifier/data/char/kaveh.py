from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ingenuity import Ingenuity


class Kaveh(CharacterBase):
    @property
    def name(self) -> str:
        return "Kaveh"

    @property
    def talent_book(self):
        return Ingenuity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Quelled Creeper", f"https://genshin-impact.fandom.com/wiki/{quote("Quelled_Creeper")}"),
            source = Source("Dendro Hypostasis", f"https://genshin-impact.fandom.com/wiki/{quote("Dendro_Hypostasis")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Primordial Greenbloom", f"https://genshin-impact.fandom.com/wiki/{quote("Primordial_Greenbloom")}"),
            source = Source("The Realm of Beginnings", f"https://genshin-impact.fandom.com/wiki/{quote("The_Realm_of_Beginnings")}")
        )
