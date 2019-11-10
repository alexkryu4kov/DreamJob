from app.external.db import Db


class KnownFromDb(Db):
    def __init__(self) -> None:
        super().__init__()

    async def select_known(self, email: str) -> list:
        await self._make_connection()
        known = await self._connection.fetch(
            '''SELECT * FROM email_known WHERE email=$1''',
            email,
        )
        await self._close_connection()
        return known
