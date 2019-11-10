from app.external.db import Db


class UnknownFromDb(Db):
    def __init__(self):
        super().__init__()

    async def select_unknown(self, email):
        await self._make_connection()
        data = await self._connection.fetch('''SELECT * FROM email_unknown WHERE email=$1''', email)
        await self._close_connection()
        return data

    async def select_courses(self):
        await self._make_connection()
        data = await self._connection.fetch('''SELECT * FROM courses''')
        await self._close_connection()
        return data
