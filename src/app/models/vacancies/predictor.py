from .vacancies_from_db import VacanciesList


class VacanciesPredictor:
    def __init__(self) -> None:
        self._vacancies_list = VacanciesList()

    async def get_vacancies(self, name: str, level: str):
        self._vacancies_list.name = name
        self._vacancies_list.level = level
        return await self._vacancies_list.create_list_of_vacancies()
