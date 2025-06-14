from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.transience import Transience


class YumemizukiMizuki(CharacterBase):
    @property
    def name(self) -> str:
        return "Yumemizuki Mizuki"

    @property
    def talent_book(self):
        return Transience().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Talisman of the Enigmatic Land", f"https://genshin-impact.fandom.com/wiki/{quote("Talisman_of_the_Enigmatic_Land")}"),
            source = Source("Wayward Hermetic Spiritspeaker", f"https://genshin-impact.fandom.com/wiki/{quote("Wayward_Hermetic_Spiritspeaker")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Fading Candle", f"https://genshin-impact.fandom.com/wiki/{quote("Fading_Candle")}"),
            source = Source("The Knave", f"https://genshin-impact.fandom.com/wiki/{quote("The_Knave")}")
        )
