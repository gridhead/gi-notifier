from ...models.base import MaterialGroupBase
from ...models.models import Drop, Item, Source, Weekday


class Freedom(MaterialGroupBase):
    @property
    def drop(self) -> Drop:
        return Drop(
            item=Item(
                "Freedom Books", "https://genshin-impact.fandom.com/wiki/Freedom_Book"
            ),
            source=Source(
                "Forsaken Rift", "https://genshin-impact.fandom.com/wiki/Forsaken_Rift"
            ),
        )

    @property
    def available_on(self) -> list[Weekday]:
        return [Weekday.MON, Weekday.THU, Weekday.SUN]
