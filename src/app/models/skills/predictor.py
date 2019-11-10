from .save_data import Saver


class SkillsPredictor:
    def __init__(self) -> None:
        self._saver = None

    @property
    def saver(self) -> Saver:
        return self._saver

    @saver.setter
    def saver(self, saver: Saver) -> None:
        self._saver = saver

    async def post_skills(self, request: dict) -> dict:
        self.saver = Saver(request)
        await self.saver.save_known_data()
        await self.saver.save_unknown_data()
        return {
            'status': 'OK',
        }
