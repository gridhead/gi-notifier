from urllib.parse import quote
from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.justice import Justice


class Freminet(CharacterBase):
    @property
    def name(self) -> str:
        return "Freminet"

    @property
    def talent_book(self):
        return Justice().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Artificed Spare Clockwork Component — Coppelius", f"https://genshin-impact.fandom.com/wiki/{quote("Artificed_Spare_Clockwork_Component_—_Coppelius")}"),
            source = Source("Icewind Suite: Nemesis of Coppelius", f"https://genshin-impact.fandom.com/wiki/{quote("Icewind_Suite:_Nemesis_of_Coppelius")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Worldspan Fern", f"https://genshin-impact.fandom.com/wiki/{quote("Worldspan_Fern")}"),
            source = Source("The Realm of Beginnings", f"https://genshin-impact.fandom.com/wiki/{quote("The_Realm_of_Beginnings")}")
        )
