class Suggester:
    def __init__(self) -> None:
        self._current_string = None
        self._vacancies_names = None

    @property
    def vacancies_names(self):
        return self._vacancies_names

    @vacancies_names.setter
    def vacancies_names(self, vacancies_names: list) -> None:
        self._vacancies_names = vacancies_names

    @property
    def current_string(self):
        return self._current_string

    @current_string.setter
    def current_string(self, current_string: str):
        self._current_string = current_string.lower()


class SuggesterCreator(Suggester):
    def __init__(self):
        super().__init__()

    def create_suggestions(self) -> list:
        return [name for name in self.vacancies_names if name.startswith(self.current_string)]
