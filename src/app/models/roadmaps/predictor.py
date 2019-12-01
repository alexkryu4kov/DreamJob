from app.models.roadmaps.roadmap_from_db import RoadmapFromDb
from app.models.roadmaps.roadmap import Roadmap


class RoadmapsPredictor:
    def __init__(self) -> None:
        self._roadmap_from_db = RoadmapFromDb()

    async def get_roadmap(self, email) -> list:
        skills_for_roadmap = await self._roadmap_from_db.select_skills_from_roadmap(email)
        return [
            Roadmap(courses=skills_for_roadmap[0]['courses']).get()
        ]
