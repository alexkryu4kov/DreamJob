from app.helpers import get_unique_list
from app.external.db import Db


class SkillsFromDb(Db):
    def __init__(self):
        super().__init__()

    async def get_list_of_skills(self, url):
        await self._make_connection()
        data = await self._connection.fetch('''SELECT * FROM skills WHERE vacancy_url=$1''', url)
        await self._close_connection()
        return get_unique_list([row['skill'] for row in data])
