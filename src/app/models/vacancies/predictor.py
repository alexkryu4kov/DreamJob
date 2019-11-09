# TODO: написать докстринги
# TODO: использовать проперти
# TODO: инкапсулировать взаимодействие с бд
# TODO: работать с классами, а не со словарями
# TODO: сделать интеллектуальный парсер скиллов из вакансий

import asyncio

from app.helpers import get_unique_skills


class VacanciesPredictor:

    def __init__(self):
        self._name = None
        self._level = None
        self._db = None

    def _set_db(self, db):
        self._db = db

    def _set_name(self, name):
        self._name = name

    def _set_level(self, level):
        self._level = level

    async def get_vacancies(self, name, level, db):
        self._set_db(db)
        self._set_name(name)
        self._set_level(level)
        row_data = await self._db.fetch(f"SELECT * FROM vacancies WHERE name='{self._name}' AND level='{self._level}';")
        return await self.create_list_of_vacancies(row_data)

    async def _create_dict_from_row(self, row):
        return {
            'name': row['name'],
            'level': row['level'],
            'company_name': row['company_name'],
            'city': row['city'],
            'salary': row['salary'],
            'skills': await self._get_list_of_skills(row['url'])
        }

    async def create_list_of_vacancies(self, data):
        tasks = [asyncio.create_task(self._create_dict_from_row(row)) for row in data]
        await asyncio.gather(*tasks)
        return [task.result() for task in tasks]

    async def _get_list_of_skills(self, url):
        con = await self._db.acquire()
        data = await con.fetch(f"SELECT * FROM skills WHERE vacancy_url='{url}'")
        return get_unique_skills([row['skill'] for row in data])

