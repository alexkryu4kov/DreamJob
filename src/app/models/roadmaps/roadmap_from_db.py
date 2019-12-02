from app.external.db import Db
from app.models.profile.unknown.unknown_from_db import UnknownFromDb
from app.helpers import get_unique_list
from app.models.roadmaps.find_course import find_course


class RoadmapFromDb(Db):
    def __init__(self) -> None:
        super().__init__()
        self._unknown_from_db = UnknownFromDb()

    async def select_courses(self) -> list:
        await self._make_connection()
        courses = await self._connection.fetch(
            '''SELECT url, name, skill FROM courses'''
        )
        await self._close_connection()
        return courses

    async def get_unknown(self, email: str) -> list:
        unknown_list = await self._unknown_from_db.select_unknown(email)
        users_list = await self._unknown_from_db.select_users(email)
        try:
            fresh_users_time = users_list[0]['save_time']
            unknown_list = [row for row in unknown_list if row['save_time'] >= fresh_users_time]
            skills = get_unique_list([row['unknown'] for row in unknown_list])
            courses = await self.select_courses()
            return [
                {
                    'courses': find_course(courses, skill),
                }
                for skill in skills
            ]
        except IndexError:
            return []

    async def select_skills_from_roadmap(self, email):
        return await self.get_unknown(email)
