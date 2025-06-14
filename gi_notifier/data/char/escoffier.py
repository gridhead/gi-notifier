from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.justice import Justice


class Escoffier(CharacterBase):
    @property
    def name(self) -> str:
        return "Escoffier"

    @property
    def talent_book(self):
        return Justice().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Secret Source Airflow Accumulator", f"https://genshin-impact.fandom.com/wiki/{quote("Secret_Source_Airflow_Accumulator")}"),
            source = Source("Secret Source Automaton: Overseer Device", f"https://genshin-impact.fandom.com/wiki/{quote("Secret_Source_Automaton:_Overseer_Device")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Eroded Horn", f"https://genshin-impact.fandom.com/wiki/{quote("Eroded_Horn")}"),
            source = Source("Stone Stele Records", f"https://genshin-impact.fandom.com/wiki/{quote("Stone_Stele_Records")}")
        )
