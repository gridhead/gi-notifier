from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.order import Order


class Chevreuse(CharacterBase):
    @property
    def name(self) -> str:
        return "Chevreuse"

    @property
    def talent_book(self):
        return Order().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Fontemer Unihorn",
                f"https://genshin-impact.fandom.com/wiki/{quote("Fontemer_Unihorn")}",
            ),
            source=Source(
                "Millennial Pearl Seahorse",
                f"https://genshin-impact.fandom.com/wiki/{quote("Millennial_Pearl_Seahorse")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Lightless Eye of the Maelstrom",
                f"https://genshin-impact.fandom.com/wiki/{quote("Lightless_Eye_of_the_Maelstrom")}",
            ),
            source=Source(
                "All-Devouring Narwhal",
                f"https://genshin-impact.fandom.com/wiki/{quote("All-Devouring_Narwhal")}",
            ),
        )
