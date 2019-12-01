from app.external.db import Db


class KnownFromDb(Db):
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

    async def select_known(self, email: str) -> list:
        await self._make_connection()
        known = await self._connection.fetch(
            '''SELECT known, save_time FROM email_known WHERE email=$1 ORDER BY save_time desc''',
            email,
        )
        await self._close_connection()
        return known
