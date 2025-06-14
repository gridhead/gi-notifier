from dataclasses import dataclass, field


@dataclass
class Resin:
    """
    Data class for resins.
    """
    original_resin: str = """Use your <a href="https://genshin-impact.fandom.com/wiki/Original_Resin">Original Resin</a> for"""
    transient_resin: str = """Do not forget to claim your <a href="https://genshin-impact.fandom.com/wiki/Transient_Resin">Transient Resin</a> from <a href="https://genshin-impact.fandom.com/wiki/Serenitea_Pot/Realm_Depot">Realm Depot</a>"""
    condensed_resin: str = """Making <a href="https://genshin-impact.fandom.com/wiki/Condensed_Resin">Condensed Resin</a> for future usage"""


@dataclass
class Item:
    """
    Data class for ontainable items.
    """
    name: str
    link: str


@dataclass
class Source:
    """
    Data class for the source of the obtainable item.
    """
    name: str
    link: str


@dataclass
class Drop:
    """
    Data class for the genrating the message for an obtainable item.
    """
    item: Item
    source: Source

    def to_html(self) -> str:
        return (
            f"""Obtaining <a href="{self.item.link}">{self.item.name}</a> """
            f"""from <a href="{self.source.link}">{self.source.name}</a>"""
        )


@dataclass
class ConstantResource:
    """
    Dataclass for the constanct resource.
    """
    experience: Drop = field(
        default_factory = lambda: Drop(
            item = Item("Experience", "https://genshin-impact.fandom.com/wiki/Experience"),
            source = Source("Ley Line Outcrop - Blossom of Revelation", "https://genshin-impact.fandom.com/wiki/Ley_Line_Outcrop")
        )
    )
    mora: Drop = field(
        default_factory = lambda: Drop(
            item = Item("Mora", "https://genshin-impact.fandom.com/wiki/Mora"),
            source = Source("Ley Line Outcrop - Blossom of Wealth", "https://genshin-impact.fandom.com/wiki/Ley_Line_Outcrop")
        )
    )
    resin: Resin = field(default_factory=Resin)


@dataclass
class Base:
    """
    Data class for characters.
    """
    title: str
    normal_boss_drop: Drop
    weekly_boss_drop: Drop
    talent_book: Drop
    constant_resource: ConstantResource = field(default_factory=ConstantResource)


@dataclass
class Week:
    """
    Data class for weeks
    """
    monday: str
    tuesday: str
    wednesday: str
    thursday: str
    friday: str
    saturday: str
    sunday: str


@dataclass
class Character:
    """
    Data class for characters.
    """
    base: Base
    week: Week
