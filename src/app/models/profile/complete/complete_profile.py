from .complete_db import CompleteDb


class CompleteProfile:

    def __init__(self) -> None:
        self._complete = CompleteDb()

    async def complete_profile(self, request: dict) -> dict:
        await self._complete.complete(request)
        return {
            'status': 'OK',
        }
