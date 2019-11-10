from app.models.spec.suggester import SuggesterCreator


class SpecPredictor:
    def __init__(self) -> None:
        self._creator = SuggesterCreator()

    def get_spec(self, current_string: str, vacancies_names: list) -> dict:
        self._creator.current_string = current_string
        self._creator.vacancies_names = vacancies_names
        suggestions = self._creator.create_suggestions()
        return {
            'spec': suggestions,
        }
