import asyncio

from app.external.db import Db
from app.models.vacancies.row import Row


class VacanciesFromDb(Db):
    def __init__(self):
        super().__init__()
        self._name = None
        self._level = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    async def _get_row_data(self):
        return await self._connection.fetch('''SELECT * FROM vacancies WHERE name=$1 AND level=$2''',
                                            self.name, self.level)


class VacanciesList(VacanciesFromDb):
    def __init__(self):
        super().__init__()

    async def create_list_of_vacancies(self):
        await self._make_connection()
        row_data = await self._get_row_data()
        tasks = [asyncio.create_task(Row(**row).create_dict_from_row()) for row in row_data]
        await asyncio.gather(*tasks)
        await self._close_connection()
        return [task.result() for task in tasks]
