from app.models.profile.known.known_from_db import KnownFromDb
from app.models.profile.score.count_score import count_score
from app.models.profile.unknown.unknown_from_db import UnknownFromDb


class ProfileScore:

    def __init__(self) -> None:
        self._known_from_db = KnownFromDb()
        self._unknown_from_db = UnknownFromDb()

    async def get_score(self, email: str) -> dict:
        known_data = await self._known_from_db.select_known(email)
        unknown_data = await self._unknown_from_db.select_unknown(email)
        users_list = await self._unknown_from_db.select_users(email)
        try:
            fresh_users_time = users_list[0]['save_time']
            known_data = [row for row in known_data if row['save_time'] >= fresh_users_time]
            unknown_data = [row for row in unknown_data if row['save_time'] >= fresh_users_time]
            return {
                'score': count_score(known_data, unknown_data),
            }
        except IndexError:
            return {
                'score': 0.0
            }
