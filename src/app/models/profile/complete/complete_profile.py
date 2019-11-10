from app.models.profile.complete.complete_db import CompleteDb


class CompleteProfile:

    def __init__(self):
        self._complete = CompleteDb()

    async def complete_profile(self, request):
        await self._complete.complete(request)
        return {
            'status': 'OK',
        }
