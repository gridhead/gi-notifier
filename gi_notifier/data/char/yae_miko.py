from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.light import Light


class YaeMiko(CharacterBase):
    @property
    def name(self) -> str:
        return "Yae Miko"

    @property
    def talent_book(self):
        return Light().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Dragonheir's False Fin",
                f"https://genshin-impact.fandom.com/wiki/{quote("Dragonheir's_False_Fin")}",
            ),
            source=Source(
                "Coral Defenders",
                f"https://genshin-impact.fandom.com/wiki/{quote("Coral_Defenders")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "The Meaning of Aeons",
                f"https://genshin-impact.fandom.com/wiki/{quote("The_Meaning_of_Aeons")}",
            ),
            source=Source(
                "End of the Oneiric Euthymia",
                f"https://genshin-impact.fandom.com/wiki/{quote("End_of_the_Oneiric_Euthymia")}",
            ),
        )
