from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.justice import Justice


class Charlotte(CharacterBase):
    @property
    def name(self) -> str:
        return "Charlotte"

    @property
    def talent_book(self):
        return Justice().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item('"Tourbillon Device"', f"https://genshin-impact.fandom.com/wiki/{quote("\"Tourbillon Device\"")}"),
            source = Source("Experimental Field Generator", f"https://genshin-impact.fandom.com/wiki/{quote("Experimental_Field_Generator")}")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Lightless Silk String", f"https://genshin-impact.fandom.com/wiki/{quote("Lightless_Silk_String")}"),
            source = Source("All-Devouring Narwhal", f"https://genshin-impact.fandom.com/wiki/{quote("All-Devouring_Narwhal")}")
        )
