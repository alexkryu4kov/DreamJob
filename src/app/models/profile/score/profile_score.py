from app.models.profile.known.known_from_db import KnownFromDb
from app.models.profile.unknown.unknown_from_db import UnknownFromDb


class ProfileScore:

    def __init__(self):
        self._known_from_db = KnownFromDb()
        self._unknown_from_db = UnknownFromDb()

    async def get_score(self, email):
        known_data = await self._known_from_db.select_known(email)
        unknown_data = await self._unknown_from_db.select_unknown(email)
        return {
                'score': self.count_score(known_data, unknown_data),
            }

    def count_score(self, known, unknown):
        try:
            return round(len(known) / (len(known) + len(unknown)), 2)

        except ZeroDivisionError:
            return 0
