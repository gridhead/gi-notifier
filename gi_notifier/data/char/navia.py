from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.equity import Equity


class Navia(CharacterBase):
    @property
    def name(self) -> str:
        return "Navia"

    @property
    def talent_book(self):
        return Equity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Artificed Spare Clockwork Component — Coppelius", f"https://genshin-impact.fandom.com/wiki/{quote("Artificed_Spare_Clockwork_Component_—_Coppelius")}"),
            source = Source("Icewind Suite: Nemesis of Coppelius", f"https://genshin-impact.fandom.com/wiki/{quote("Icewind_Suite:_Nemesis_of_Coppelius")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Lightless Silk String", f"https://genshin-impact.fandom.com/wiki/{quote("Lightless_Silk_String")}"),
            source = Source("All-Devouring Narwhal", f"https://genshin-impact.fandom.com/wiki/{quote("All-Devouring_Narwhal")}")
        )
