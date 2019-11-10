# TODO: исправть асинхрон в save_data

from app.external.db import Db
from app.models.skills.save_data import Saver


class SkillsPredictor:
    def __init__(self):
        self._saver = None

    @property
    def saver(self):
        return self._saver

    @saver.setter
    def saver(self, saver):
        self._saver = saver

    async def post_skills(self, request, db):
        Db.db = db
        self.saver = Saver(request)
        await self.saver.save_known_data()
        await self.saver.save_unknown_data()
        return {
            'status': 'OK',
        }

