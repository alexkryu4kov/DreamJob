# TODO: написать докстринги
# TODO: заиспользовать проперти вместо функций set
# TODO: проверять наличие текущего специализации (добавить поле validation)
# TODO: вынести обработку списка текущих вакансий в отдельный модуль (схлопывание)
# TODO: возможно использовать более интеллектуальный алгоритм поиска
# TODO: ранжировать по популярности названия вакансий и отдавать в отдельном порядке

from app.models.spec.suggester import SuggesterCreator


class SpecPredictor:
    def __init__(self):
        self._creator = SuggesterCreator()

    def get_spec(self, current_string: str, vacancies_names: list) -> dict:
        suggestions = self._creator.create_suggestions(current_string, vacancies_names)
        return {
            'spec': suggestions,
        }
