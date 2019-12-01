from app.external.db import Db


class CoursesFromDb(Db):
    def __init__(self):
        super().__init__()

    async def select_courses(self, skill):
        await self._make_connection()
        courses = await self._connection.fetch(
            '''SELECT url, name FROM courses WHERE skill=$1''',
            skill,
        )
        await self._close_connection()
        return courses
