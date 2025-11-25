from prp_core.modules.finance.services import seeder as finance_seeder
from prp_core.modules.assets.services import seeder as assets_seeder
from prp_core.modules.planning.services import seeder as planning_seeder

async def clear_data():
    """Wipes all data from the database."""
    await finance_seeder.clear_data()
    await assets_seeder.clear_data()
    await planning_seeder.clear_data()

async def seed_young_professional():
    """
    Scenario: Young Professional
    """
    await finance_seeder.seed("young_professional")
    await assets_seeder.seed("young_professional")
    await planning_seeder.seed("young_professional")

async def seed_family():
    """
    Scenario: Family
    """
    await finance_seeder.seed("family")
    await assets_seeder.seed("family")
    await planning_seeder.seed("family")

async def seed_small_business():
    """
    Scenario: Small Business Owner
    """
    await finance_seeder.seed("small_business")
    await assets_seeder.seed("small_business")
    await planning_seeder.seed("small_business")
