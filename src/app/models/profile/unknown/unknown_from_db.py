from app.external.db import Db


class UnknownFromDb(Db):
    def __init__(self) -> None:
        super().__init__()

    async def select_unknown(self, email: str) -> list:
        await self._make_connection()
        unknown = await self._connection.fetch(
            '''SELECT * FROM email_unknown WHERE email=$1 ORDER BY save_time desc''',
            email,
        )
        await self._close_connection()
        return unknown

    async def select_courses(self) -> list:
        await self._make_connection()
        courses = await self._connection.fetch(
            '''SELECT * FROM courses'''
        )
        await self._close_connection()
        return courses
