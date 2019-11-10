class SuggesterCreator:

    def create_suggestions(self, vacancies_names, current_string) -> list:
        return [name for name in vacancies_names if name.startswith(current_string)]
