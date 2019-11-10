from app.helpers import get_unique_list
from app.models.profile.known.known_from_db import KnownFromDb


class GetKnown:
    def __init__(self) -> None:
        self._known_from_db = KnownFromDb()

    async def get_known(self, email: str) -> dict:
        known_list = await self._known_from_db.select_known(email)
        skills = get_unique_list([row['known'] for row in known_list])
        return {
            'known': skills,
        }
