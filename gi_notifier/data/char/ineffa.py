from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.conflict import Conflict


class Ineffa(CharacterBase):
    @property
    def name(self) -> str:
        return "Ineffa"

    @property
    def talent_book(self):
        return Conflict().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Secret Source Airflow Accumulator",
                f"https://genshin-impact.fandom.com/wiki/{quote("Secret_Source_Airflow_Accumulator")}",
            ),
            source=Source(
                "Secret Source Automaton: Overseer Device",
                f"https://genshin-impact.fandom.com/wiki/{quote("Secret_Source_Automaton:_Overseer_Device")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Eroded Sunfire",
                f"https://genshin-impact.fandom.com/wiki/{quote("Eroded_Sunfire")}",
            ),
            source=Source(
                "Stone Stele Records",
                f"https://genshin-impact.fandom.com/wiki/{quote("Stone_Stele_Records")}",
            ),
        )
