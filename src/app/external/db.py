class Db:
    def __init__(self):
        self._db = None
        self._connection = None

    @property
    def db(self):
        return self._db

    @db.setter
    def db(self, db):
        self._db = db

    async def _make_connection(self):
        self._connection = await self.db.acquire()

    async def _close_connection(self):
        await self.db.release(self._connection)
