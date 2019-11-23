from app.models.profile.courses.courses_from_db import CoursesFromDb


class ProfileCourses:
    def __init__(self) -> None:
        self._courses_from_db = CoursesFromDb()

    async def get_courses(self, skill) -> list:
        raw_courses = await self._courses_from_db.select_courses(skill)
        courses = [{
            'url': course['url'],
            'name': course['name'],
        }
            for course in raw_courses]
        return courses
