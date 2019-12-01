from app.external.db import Db
from app.models.profile.unknown.profile_unknown import GetUnknown


class RoadmapFromDb(Db):
    def __init__(self) -> None:
        super().__init__()

    async def select_skills_from_roadmap(self, email):
        return await GetUnknown().get_unknown(email)
