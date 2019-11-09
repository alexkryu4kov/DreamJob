# TODO: написать докстринги
# TODO: заиспользовать проперти вместо функций set
# TODO: вынести обработку списка текущих вакансий в отдельный модуль (схлопывание)
# TODO: возможно использовать более интеллектуальный алгоритм поиска
# TODO: ранжировать по популярности названия вакансий и отдавать в отдельном порядке


class SpecPredictor:

    def __init__(self) -> None:
        self._current_string = None
        self._vacancies_names = None

    def _set_vacancies_names(self, vacancies_names: list) -> None:
        self._vacancies_names = vacancies_names

    def _set_current_string(self, current_string: str):
        self._current_string = current_string.lower()

    def _create_suggestions(self) -> list:
        return [name for name in self._vacancies_names if name.startswith(self._current_string)]

    def get_spec(self, current_string: str, vacancies_names: list) -> dict:
        self._set_current_string(current_string)
        self._set_vacancies_names(vacancies_names)
        suggestions = self._create_suggestions()
        return {
            'spec': suggestions,
        }


