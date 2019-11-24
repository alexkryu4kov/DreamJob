from asyncpg import Record

from app.external.db import Db


class RoadmapFromDb(Db):
    def __init__(self) -> None:
        super().__init__()

    async def select_roadmap_names(self, email):
        await self._make_connection()
        roadmaps_names = await self._connection.fetch(
            '''SELECT * FROM email_roadmaps WHERE email=$1''',
            email,
        )
        await self._close_connection()
        return roadmaps_names

    async def select_roadmaps(self, roadmap_name: str) -> Record:
        await self._make_connection()
        roadmaps = await self._connection.fetch(
            '''SELECT * FROM roadmaps WHERE roadmap_name=$1''',
            roadmap_name,
        )
        await self._close_connection()
        return roadmaps
