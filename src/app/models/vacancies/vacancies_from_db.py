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
        self._name = name.lower()

    @property
    def level(self) -> str:
        return self._level

    @level.setter
    def level(self, level: str) -> None:
        self._level = level.lower()

    async def _get_row_data(self):
        await self._make_connection()
        row_data = await self._connection.fetch(
            '''SELECT vacancy_id, name, level, company_name, city, salary, url, real_name, skill
            FROM vacancies_skills WHERE name=$1 AND level=$2''',
            self.name, self.level,
        )
        await self._close_connection()
        return row_data


class VacanciesList(VacanciesFromDb):
    def __init__(self) -> None:
        super().__init__()

    def get_unique_ids(self, rows):
        return list(set([row['vacancy_id'] for row in rows]))

    def get_skills_by_id(self, rows):
        return {id: [row['skill'] for row in rows if id == row['vacancy_id']] for id in self.get_unique_ids(rows)}

    def create_vacancy(self, id, rows):
        for row in rows:
            if row['vacancy_id'] == id:
                return row

    async def create_list_of_vacancies(self) -> list:
        await self._make_connection()
        row_data = await self._get_row_data()
        skills_dict = self.get_skills_by_id(row_data)
        vacancies_row = [self.create_vacancy(id, row_data) for id in self.get_unique_ids(row_data)]
        vacancies = [Row(**row).create_dict_from_row(skills_dict) for row in vacancies_row]
        await self._close_connection()
        return vacancies
