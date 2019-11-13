import asyncio

from app.external.db import Db
from app.models.vacancies.row import Row


class VacanciesFromDb(Db):
    def __init__(self) -> None:
        super().__init__()
        self._name: str = ''
        self._level: str = ''

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name.capitalize()

    @property
    def level(self) -> str:
        return self._level

    @level.setter
    def level(self, level: str) -> None:
        self._level = level

    async def _get_row_data(self):
        return await self._connection.fetch(
            '''SELECT * FROM vacancies WHERE name=$1 AND level=$2''',
            self.name, self.level,
        )


class VacanciesList(VacanciesFromDb):
    def __init__(self) -> None:
        super().__init__()

    async def create_list_of_vacancies(self) -> list:
        await self._make_connection()
        row_data = await self._get_row_data()
        tasks = [asyncio.create_task(Row(**row).create_dict_from_row()) for row in row_data]
        await asyncio.gather(*tasks)
        await self._close_connection()
        return [task.result() for task in tasks]
