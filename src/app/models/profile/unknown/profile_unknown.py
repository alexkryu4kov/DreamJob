from app.helpers import get_unique_list
from app.models.profile.unknown.courses import CourseSelector
from app.models.profile.unknown.unknown_from_db import UnknownFromDb


class GetUnknown:
    def __init__(self):
        self._course_selector = CourseSelector()
        self._unknown_from_db = UnknownFromDb()

    async def get_unknown(self, email):
        unknown_list = await self._unknown_from_db.select_unknown(email)
        skills = get_unique_list([row['unknown'] for row in unknown_list])
        courses = await self._unknown_from_db.select_courses()
        return [
            {
                'name': skill,
                'courses': self._course_selector.find_course(courses, skill)
            }
            for skill in skills
        ]

