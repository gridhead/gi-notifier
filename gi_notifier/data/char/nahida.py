from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ingenuity import Ingenuity


class Nahida(CharacterBase):
    @property
    def name(self) -> str:
        return "Nahida"

    @property
    def talent_book(self):
        return Ingenuity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Quelled Creeper",
                f"https://genshin-impact.fandom.com/wiki/{quote("Quelled_Creeper")}",
            ),
            source=Source(
                "Dendro Hypostasis",
                f"https://genshin-impact.fandom.com/wiki/{quote("Dendro_Hypostasis")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Puppet Strings",
                f"https://genshin-impact.fandom.com/wiki/{quote("Puppet_Strings")}",
            ),
            source=Source(
                "Joururi Workshop",
                f"https://genshin-impact.fandom.com/wiki/{quote("Joururi_Workshop")}",
            ),
        )
