from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.gold import Gold


class Baizhu(CharacterBase):
    @property
    def name(self) -> str:
        return "Baizhu"

    @property
    def talent_book(self):
        return Gold().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Evergloom Ring", f"https://genshin-impact.fandom.com/wiki/{quote("Evergloom_Ring")}"),
            source = Source("Iniquitous Baptist", f"https://genshin-impact.fandom.com/wiki/{quote("Iniquitous_Baptist")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Worldspan Fern", f"https://genshin-impact.fandom.com/wiki/{quote("Worldspan_Fern")}"),
            source = Source("The Realm of Beginnings", f"https://genshin-impact.fandom.com/wiki/{quote("The_Realm_of_Beginnings")}")
        )
