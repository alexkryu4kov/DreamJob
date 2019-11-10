from app.external.db import Db


class KnownFromDb(Db):
    def __init__(self):
        super().__init__()

    async def select_known(self, email):
        await self._make_connection()
        data = await self._connection.fetch('''SELECT * FROM email_known WHERE email=$1''', email)
        await self._close_connection()
        return data
