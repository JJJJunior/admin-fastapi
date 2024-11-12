import os

from tortoise import Tortoise, run_async


async def init_db():
    await Tortoise.init(
        db_url=f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}",
        modules={"models": ["models"]}
    )
    await Tortoise.generate_schemas()


run_async(init_db())
