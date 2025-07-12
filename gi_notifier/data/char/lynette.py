from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.order import Order


class Lynette(CharacterBase):
    @property
    def name(self) -> str:
        return "Lynette"

    @property
    def talent_book(self):
        return Order().as_material_group()

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
                "Everamber",
                f"https://genshin-impact.fandom.com/wiki/{quote("Everamber")}",
            ),
            source=Source(
                "The Realm of Beginnings",
                f"https://genshin-impact.fandom.com/wiki/{quote("The_Realm_of_Beginnings")}",
            ),
        )
