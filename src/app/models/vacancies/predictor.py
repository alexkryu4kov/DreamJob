# TODO: написать докстринги
# TODO: использовать проперти
# TODO: инкапсулировать взаимодействие с бд
# TODO: работать с классами, а не со словарями
# TODO: сделать интеллектуальный парсер скиллов из вакансий


from app.models.vacancies.vacancies_from_db import VacanciesList


class VacanciesPredictor:
    def __init__(self):
        self._vacancies_list = VacanciesList()

    async def get_vacancies(self, name, level):
        self._vacancies_list.name = name
        self._vacancies_list.level = level
        return await self._vacancies_list.create_list_of_vacancies()
