from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.order import Order


class Emilie(CharacterBase):
    @property
    def name(self) -> str:
        return "Emilie"

    @property
    def talent_book(self):
        return Order().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Fragment of a Golden Melody", f"https://genshin-impact.fandom.com/wiki/{quote("Fragment_of_a_Golden_Melody")}"),
            source = Source("Statue of Marble and Brass", f"https://genshin-impact.fandom.com/wiki/{quote("\"Statue_of_Marble_and_Brass\"")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Silken Feather", f"https://genshin-impact.fandom.com/wiki/{quote("Silken_Feather")}"),
            source = Source("The Knave", f"https://genshin-impact.fandom.com/wiki/{quote("The_Knave")}")
        )
