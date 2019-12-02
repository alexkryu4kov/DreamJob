from app.external.db import Db


class UnknownFromDb(Db):
    def __init__(self) -> None:
        super().__init__()

    async def select_users(self, email):
        await self._make_connection()
        users = await self._connection.fetch(
            '''SELECT save_time FROM users WHERE email=$1 ORDER BY save_time desc''',
            email,
        )
        await self._close_connection()
        return users

    async def select_unknown(self, email: str) -> list:
        await self._make_connection()
        unknown = await self._connection.fetch(
            '''SELECT unknown, save_time FROM email_unknown WHERE email=$1 ORDER BY save_time desc''',
            email,
        )
        await self._close_connection()
        return unknown
