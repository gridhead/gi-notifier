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
class FixedMaterials:
    """
    Dataclass for the fixed materials.
    """
    experience: str = """Obtaining <a href="https://genshin-impact.fandom.com/wiki/Experience">Experience</a> from <a href="https://genshin-impact.fandom.com/wiki/Ley_Line_Outcrop">Ley Line Outcrop - Blossom of Revelation</a>"""
    mora: str = """Obtaining <a href="https://genshin-impact.fandom.com/wiki/Mora">Mora</a> from <a href="https://genshin-impact.fandom.com/wiki/Ley_Line_Outcrop">Ley Line Outcrop - Blossom of Wealth</a>"""
    resin: Resin = field(default_factory=Resin)


@dataclass
class Characters:
    """
    Data class for characters.
    """
    title: str
    normal_boss_drop: str
    weekly_boss_drop: str
    talent_book: str
    fixed_materials: FixedMaterials = field(default_factory=FixedMaterials)
