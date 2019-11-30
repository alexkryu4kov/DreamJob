from app.models.profile.known.profile_known import GetKnown
from app.models.profile.unknown.profile_unknown import GetUnknown
from app.models.profile.score.profile_score import ProfileScore
from app.models.profile.complete.complete_profile import CompleteProfile
from app.models.profile.courses.profile_courses import ProfileCourses


class ProfilePredictor:

    def __init__(self) -> None:
        self._known = GetKnown()
        self._unknown = GetUnknown()
        self._score = ProfileScore()
        self._complete = CompleteProfile()
        self._courses = ProfileCourses()

    async def get_known(self, email: str):
        return await self._known.get_known(email)

    async def get_unknown(self, email: str):
        return await self._unknown.get_unknown(email)

    async def get_score(self, email: str):
        return await self._score.get_score(email)

    async def complete_profile(self, request: dict):
        return await self._complete.complete_profile(request)

    async def get_courses(self, skill: str):
        return await self._courses.get_courses(skill)
