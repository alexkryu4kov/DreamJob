from app.helpers import get_unique_list
from app.models.profile.unknown.find_course import find_course
from app.models.profile.unknown.unknown_from_db import UnknownFromDb


class GetUnknown:
    def __init__(self) -> None:
        self._unknown_from_db = UnknownFromDb()

    async def get_unknown(self, email: str) -> list:
        unknown_list = await self._unknown_from_db.select_unknown(email)
        users_list = await self._unknown_from_db.select_users(email)
        try:
            fresh_time = unknown_list[0]['save_time']
            fresh_users_time = users_list[0]['save_time']
            if fresh_time >= fresh_users_time:
                unknown_list = [row for row in unknown_list if row['save_time'] == fresh_time]
                skills = get_unique_list([row['unknown'] for row in unknown_list])
                courses = await self._unknown_from_db.select_courses()
                return [
                    {
                        'name': skill,
                        'courses': find_course(courses, skill),
                    }
                    for skill in skills
                ]
            return []
        except IndexError:
            return []

