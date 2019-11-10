from app.helpers import get_unique_list
from .courses import CourseSelector
from .unknown_from_db import UnknownFromDb


class GetUnknown:
    def __init__(self) -> None:
        self._course_selector = CourseSelector()
        self._unknown_from_db = UnknownFromDb()

    async def get_unknown(self, email: str) -> list:
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

