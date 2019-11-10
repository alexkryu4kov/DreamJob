from .known.profile_known import GetKnown
from .unknown.profile_unknown import GetUnknown
from .score.profile_score import ProfileScore
from .complete.complete_profile import CompleteProfile


class ProfilePredictor:

    def __init__(self) -> None:
        self._known = GetKnown()
        self._unknown = GetUnknown()
        self._score = ProfileScore()
        self._complete = CompleteProfile()

    async def get_known(self, email: str):
        return await self._known.get_known(email)

    async def get_unknown(self, email: str):
        return await self._unknown.get_unknown(email)

    async def get_score(self, email: str):
        return await self._score.get_score(email)

    async def complete_profile(self, request: dict):
        return await self._complete.complete_profile(request)
