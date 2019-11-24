from app.models.roadmaps.select.roadmap_from_db import RoadmapFromDb


class ProfileCourses:
    def __init__(self) -> None:
        self._roadmap_from_db = RoadmapFromDb()

    async def get_roadmap(self, name) -> dict:
        raw_roadmap = await self._roadmap_from_db.select_roadmaps(name)
        roadmap = raw_roadmap['roadmap_name']
        course_1 = raw_roadmap['course_1']
        course_2 = raw_roadmap['course_2']
        course_3 = raw_roadmap['course_3']
        return {
            'name': roadmap,
            'course_1': course_1,
            'course_2': course_2,
            'course_3': course_3,
        }
