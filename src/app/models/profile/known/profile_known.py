from app.helpers import get_unique_list
from app.models.profile.known.known_from_db import KnownFromDb


class GetKnown:
    def __init__(self) -> None:
        self._known_from_db = KnownFromDb()

    async def get_known(self, email: str) -> dict:
        known_list = await self._known_from_db.select_known(email)
        users_list = await self._known_from_db.select_users(email)
        try:
            fresh_users_time = users_list[0]['save_time']
            known_list = [row for row in known_list if row['save_time'] >= fresh_users_time]
            skills = get_unique_list([row['known'] for row in known_list])
        except IndexError:
            skills = []
        return {
            'known': skills,
        }
