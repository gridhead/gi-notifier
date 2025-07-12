from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.contention import Contention


class Mualani(CharacterBase):
    @property
    def name(self) -> str:
        return "Mualani"

    @property
    def talent_book(self):
        return Contention().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Mark of the Binding Blessing",
                f"https://genshin-impact.fandom.com/wiki/{quote("Mark_of_the_Binding_Blessing")}",
            ),
            source=Source(
                "Goldflame Qucusaur Tyrant",
                f"https://genshin-impact.fandom.com/wiki/{quote("Goldflame_Qucusaur_Tyrant")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Lightless Mass",
                f"https://genshin-impact.fandom.com/wiki/{quote("Lightless_Mass")}",
            ),
            source=Source(
                "All-Devouring Narwhal",
                f"https://genshin-impact.fandom.com/wiki/{quote("All-Devouring_Narwhal")}",
            ),
        )
