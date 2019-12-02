from app.helpers import get_unique_list
from app.models.profile.unknown.unknown_from_db import UnknownFromDb


class GetUnknown:
    def __init__(self) -> None:
        self._unknown_from_db = UnknownFromDb()

    async def get_unknown(self, email: str) -> dict:
        unknown_list = await self._unknown_from_db.select_unknown(email)
        users_list = await self._unknown_from_db.select_users(email)
        try:
            fresh_users_time = users_list[0]['save_time']
            unknown_list = [row for row in unknown_list if row['save_time'] >= fresh_users_time]
            skills = get_unique_list([row['unknown'] for row in unknown_list])
            return {
                'unknown': skills
            }
        except IndexError:
            return {
                'unknown': []
            }
