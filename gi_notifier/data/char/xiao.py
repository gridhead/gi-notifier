from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.prosperity import Prosperity


class Xiao(CharacterBase):
    @property
    def name(self) -> str:
        return "Xiao"

    @property
    def talent_book(self):
        return Prosperity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Juvenile Jade", f"https://genshin-impact.fandom.com/wiki/{quote("Juvenile_Jade")}"),
            source = Source("Primo Geovishap", f"https://genshin-impact.fandom.com/wiki/{quote("Primo_Geovishap")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Shadow of the Warrior", f"https://genshin-impact.fandom.com/wiki/{quote("Shadow_of_the_Warrior")}"),
            source = Source("Enter the Golden House", f"https://genshin-impact.fandom.com/wiki/{quote("Enter_the_Golden_House")}")
        )
