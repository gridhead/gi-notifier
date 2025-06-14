from ..models import Week
from .characters import escoffier_base, skirk_base

week_skirk = Week(
    monday = f"""
{skirk_base.title}

{skirk_base.constant_resource.resin.original_resin}
1. {skirk_base.talent_book.to_html()}
2. {skirk_base.normal_boss_drop.to_html()}
3. {skirk_base.constant_resource.mora.to_html()}
4. {skirk_base.constant_resource.experience.to_html()}
5. {skirk_base.constant_resource.resin.condensed_resin}
""",
    tuesday = f"""
{skirk_base.title}

{skirk_base.constant_resource.resin.original_resin}
1. {skirk_base.weekly_boss_drop.to_html()}
2. {skirk_base.normal_boss_drop.to_html()}
3. {skirk_base.constant_resource.mora.to_html()}
4. {skirk_base.constant_resource.experience.to_html()}
5. {skirk_base.constant_resource.resin.condensed_resin}
""",
    wednesday = f"""
{skirk_base.title}

{skirk_base.constant_resource.resin.original_resin}
1. {skirk_base.normal_boss_drop.to_html()}
2. {skirk_base.constant_resource.mora.to_html()}
3. {skirk_base.constant_resource.experience.to_html()}
4. {skirk_base.constant_resource.resin.condensed_resin}
""",
    thursday = f"""
{skirk_base.title}

{skirk_base.constant_resource.resin.original_resin}
1. {skirk_base.talent_book.to_html()}
2. {skirk_base.normal_boss_drop.to_html()}
3. {skirk_base.constant_resource.mora.to_html()}
4. {skirk_base.constant_resource.experience.to_html()}
5. {skirk_base.constant_resource.resin.condensed_resin}
""",
    friday = f"""
{skirk_base.title}

{skirk_base.constant_resource.resin.original_resin}
1. {skirk_base.normal_boss_drop.to_html()}
2. {skirk_base.constant_resource.mora.to_html()}
3. {skirk_base.constant_resource.experience.to_html()}
4. {skirk_base.constant_resource.resin.condensed_resin}
""",
    saturday = f"""
{skirk_base.title}

{skirk_base.constant_resource.resin.original_resin}
1. {skirk_base.normal_boss_drop.to_html()}
2. {skirk_base.constant_resource.mora.to_html()}
3. {skirk_base.constant_resource.experience.to_html()}
4. {skirk_base.constant_resource.resin.condensed_resin}
""",
    sunday = f"""
{skirk_base.title}

{skirk_base.constant_resource.resin.original_resin}
1. {skirk_base.talent_book.to_html()}
2. {skirk_base.normal_boss_drop.to_html()}
3. {skirk_base.constant_resource.mora.to_html()}
4. {skirk_base.constant_resource.experience.to_html()}
5. {skirk_base.constant_resource.resin.condensed_resin}
"""
)

week_escoffier = Week(
    monday = f"""
{escoffier_base.title}

{escoffier_base.constant_resource.resin.original_resin}
1. {escoffier_base.weekly_boss_drop.to_html()}
2. {escoffier_base.normal_boss_drop.to_html()}
3. {escoffier_base.constant_resource.mora.to_html()}
4. {escoffier_base.constant_resource.experience.to_html()}
5. {escoffier_base.constant_resource.resin.condensed_resin}
""",
    tuesday = f"""
{escoffier_base.title}

{escoffier_base.constant_resource.resin.original_resin}
1. {escoffier_base.talent_book.to_html()}
2. {escoffier_base.normal_boss_drop.to_html()}
3. {escoffier_base.constant_resource.mora.to_html()}
4. {escoffier_base.constant_resource.experience.to_html()}
5. {escoffier_base.constant_resource.resin.condensed_resin}
""",
    wednesday = f"""
{escoffier_base.title}

{escoffier_base.constant_resource.resin.original_resin}
1. {escoffier_base.normal_boss_drop.to_html()}
2. {escoffier_base.constant_resource.mora.to_html()}
3. {escoffier_base.constant_resource.experience.to_html()}
4. {escoffier_base.constant_resource.resin.condensed_resin}
""",
    thursday = f"""
{escoffier_base.title}

{escoffier_base.constant_resource.resin.original_resin}
1. {escoffier_base.normal_boss_drop.to_html()}
2. {escoffier_base.constant_resource.mora.to_html()}
3. {escoffier_base.constant_resource.experience.to_html()}
4. {escoffier_base.constant_resource.resin.condensed_resin}
""",
    friday = f"""
{escoffier_base.title}

{escoffier_base.constant_resource.resin.original_resin}
1. {escoffier_base.talent_book.to_html()}
2. {escoffier_base.normal_boss_drop.to_html()}
3. {escoffier_base.constant_resource.mora.to_html()}
4. {escoffier_base.constant_resource.experience.to_html()}
5. {escoffier_base.constant_resource.resin.condensed_resin}
""",
    saturday = f"""
{escoffier_base.title}

{escoffier_base.constant_resource.resin.original_resin}
1. {escoffier_base.normal_boss_drop.to_html()}
2. {escoffier_base.constant_resource.mora.to_html()}
3. {escoffier_base.constant_resource.experience.to_html()}
4. {escoffier_base.constant_resource.resin.condensed_resin}
""",
    sunday = f"""
{escoffier_base.title}

{escoffier_base.constant_resource.resin.original_resin}
1. {escoffier_base.talent_book.to_html()}
2. {escoffier_base.normal_boss_drop.to_html()}
3. {escoffier_base.constant_resource.mora.to_html()}
4. {escoffier_base.constant_resource.experience.to_html()}
5. {escoffier_base.constant_resource.resin.condensed_resin}
"""
)
