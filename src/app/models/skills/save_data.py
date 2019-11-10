import asyncio

from app.external.db import Db
from app.models.skills.parse_request import ParseRequest


class Saver(Db):

    def __init__(self, request):
        super().__init__()
        self._connection_known = None
        self._connection_unknown = None
        self._request = ParseRequest()
        self._request.set_email_known_unknown(request)

    async def db_execute_known(self, elem):
        await self._connection_known.execute('''INSERT INTO email_known (email, known) VALUES ($1, $2)''',
                                             self._request.email, elem)

    async def db_execute_unknown(self, elem):
        await self._connection_unknown.execute('''INSERT INTO email_unknown (email, unknown) VALUES ($1, $2)''',
                                               self._request.email, elem)

    async def save_known_data(self):
        self._connection_known = await self.db.acquire()
        [await self.db_execute_known(elem) for elem in self._request.known]
        await self.db.release(self._connection_known)

    async def save_unknown_data(self):
        self._connection_unknown = await self.db.acquire()
        [await self.db_execute_unknown(elem) for elem in self._request.unknown]
        await self.db.release(self._connection_unknown)
