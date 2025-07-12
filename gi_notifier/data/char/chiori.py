from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.light import Light


class Chiori(CharacterBase):
    @property
    def name(self) -> str:
        return "Chiori"

    @property
    def talent_book(self):
        return Light().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Artificed Spare Clockwork Component — Coppelia",
                f"https://genshin-impact.fandom.com/wiki/{quote("Artificed_Spare_Clockwork_Component_—_Coppelia")}",
            ),
            source=Source(
                "Icewind Suite: Dirge of Coppelia",
                f"https://genshin-impact.fandom.com/wiki/{quote("Icewind_Suite:_Dirge_of_Coppelia")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Lightless Silk String",
                f"https://genshin-impact.fandom.com/wiki/{quote("Lightless_Silk_String")}",
            ),
            source=Source(
                "All-Devouring Narwhal",
                f"https://genshin-impact.fandom.com/wiki/{quote("All-Devouring_Narwhal")}",
            ),
        )
