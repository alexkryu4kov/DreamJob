from app.external.db import Db
from .request_parser import RequestParser


class CompleteDb(Db):
    def __init__(self) -> None:
        super().__init__()
        self._request = RequestParser()

    async def insert_known(self) -> None:
        await self._make_connection()
        await self._connection.execute('''INSERT INTO email_known (email, known) VALUES ($1, $2)''',
                                       self._request.email, self._request.skill)
        await self._close_connection()

    async def delete_unknown(self) -> None:
        await self._make_connection()
        await self._connection.execute('''DELETE FROM email_unknown WHERE email=$1 AND unknown=$2''',
                                       self._request.email, self._request.skill)
        await self._close_connection()

    async def complete(self, request: dict) -> None:
        self._request.parse(request)
        await self.insert_known()
        await self.delete_unknown()
