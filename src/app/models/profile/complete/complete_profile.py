from app.models.profile.complete.complete_db import CompleteDb
from app.models.profile.complete.request_parser import RequestParser


class CompleteProfile:

    def __init__(self) -> None:
        self._complete = CompleteDb()
        self._request = RequestParser()

    async def complete_profile(self, request: dict) -> dict:
        self._request.parse(request)
        await self._complete.complete(self._request)
        return {
            'status': 'OK',
        }
