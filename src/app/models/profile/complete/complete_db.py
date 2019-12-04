from app.external.db import Db
from app.models.profile.complete.request_parser import RequestParser


class CompleteDb(Db):
    def __init__(self) -> None:
        super().__init__()
        self._request = None

    async def select_unknown_save_time(self) -> int:
        await self._make_connection()
        unknown = await self._connection.fetch(
            '''SELECT save_time FROM email_unknown WHERE email=$1 AND unknown=$2 ORDER BY save_time desc''',
            self._request.email, self._request.skill
        )
        await self._close_connection()
        return unknown[0]['save_time']

    async def insert_known(self, save_time) -> None:
        await self._make_connection()
        await self._connection.execute(
            '''INSERT INTO email_known (email, known, save_time) VALUES ($1, $2, $3)''',
            self._request.email, self._request.skill, save_time,
        )
        await self._close_connection()

    async def delete_unknown(self, save_time) -> None:
        await self._make_connection()
        await self._connection.execute(
            '''DELETE FROM email_unknown WHERE email=$1 AND unknown=$2 AND save_time=$3''',
            self._request.email, self._request.skill, save_time,
        )
        await self._close_connection()

    async def complete(self, request: RequestParser) -> None:
        self._request = request
        unknown_save_time = await self.select_unknown_save_time()
        await self.delete_unknown(unknown_save_time)
        await self.insert_known(unknown_save_time)
