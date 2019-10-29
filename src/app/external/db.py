import asyncpg


async def init_database(pg_config):
    return await asyncpg.connect(**pg_config)
