import asyncpg


async def init_database(pg_config):
    return await asyncpg.create_pool(**pg_config)