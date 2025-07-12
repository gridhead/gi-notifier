from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.diligence import Diligence


class Ganyu(CharacterBase):
    @property
    def name(self) -> str:
        return "Ganyu"

    @property
    def talent_book(self):
        return Diligence().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Hoarfrost Core", f"https://genshin-impact.fandom.com/wiki/{quote("Hoarfrost_Core")}"),
            source = Source("Cryo Regisvine", f"https://genshin-impact.fandom.com/wiki/{quote("Cryo_Regisvine")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Shadow of the Warrior", f"https://genshin-impact.fandom.com/wiki/{quote("Shadow_of_the_Warrior")}"),
            source = Source("Enter the Golden House", f"https://genshin-impact.fandom.com/wiki/{quote("Enter_the_Golden_House")}")
        )
