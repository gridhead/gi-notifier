from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.freedom import Freedom


class Diona(CharacterBase):
    @property
    def name(self) -> str:
        return "Diona"

    @property
    def talent_book(self):
        return Freedom().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Hoarfrost Core",
                f"https://genshin-impact.fandom.com/wiki/{quote("Hoarfrost_Core")}",
            ),
            source=Source(
                "Cryo Regisvine",
                f"https://genshin-impact.fandom.com/wiki/{quote("Cryo_Regisvine")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Shard of a Foul Legacy",
                f"https://genshin-impact.fandom.com/wiki/{quote("Shard_of_a_Foul_Legacy")}",
            ),
            source=Source(
                "Enter the Golden House",
                f"https://genshin-impact.fandom.com/wiki/{quote("Enter_the_Golden_House")}",
            ),
        )
