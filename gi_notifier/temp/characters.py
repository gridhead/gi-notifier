from ..models import Base, Drop, Item, Source

skirk_base = Base(
    title = """<strong>For Skirk</strong>""",
    normal_boss_drop = Drop(
        item = Item("Ensnaring Gaze", "https://genshin-impact.fandom.com/wiki/Ensnaring_Gaze"),
        source = Source("Tenebrous Papilla", "https://genshin-impact.fandom.com/wiki/Tenebrous_Papilla")
    ),
    weekly_boss_drop = Drop(
        item = Item("Ascended Sample: Knight", "https://genshin-impact.fandom.com/wiki/Ascended_Sample:_Knight"),
        source = Source("Unresolved Chess Game", "https://genshin-impact.fandom.com/wiki/Unresolved_Chess_Game")
    ),
    talent_book = Drop(
        item = Item("Contention Books", "https://genshin-impact.fandom.com/wiki/Contention_Book"),
        source = Source("Blazing Ruins", "https://genshin-impact.fandom.com/wiki/Blazing_Ruins")
    )
)

escoffier_base = Base(
    title = """<strong>For Escoffier</strong>""",
    normal_boss_drop = Drop(
        item = Item("Secret Source Airflow Accumulator", "https://genshin-impact.fandom.com/wiki/Secret_Source_Airflow_Accumulator"),
        source = Source("Secret Source Automaton: Overseer Device", "https://genshin-impact.fandom.com/wiki/Secret_Source_Automaton:_Overseer_Device")
    ),
    weekly_boss_drop = Drop(
        item = Item("Eroded Horn", "https://genshin-impact.fandom.com/wiki/Eroded_Horn"),
        source = Source("Stone Stele Records", "https://genshin-impact.fandom.com/wiki/Stone_Stele_Records")
    ),
    talent_book = Drop(
        item = Item("Justice Books", "https://genshin-impact.fandom.com/wiki/Justice_Book"),
        source = Source("Pale Forgotten Glory", "https://genshin-impact.fandom.com/wiki/Pale_Forgotten_Glory")
    )
)
