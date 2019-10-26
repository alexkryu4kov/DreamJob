class SpecPredictor:
    def get_spec(self, current_string, vacancies_names):
        suggestions = [name for name in vacancies_names if name.startswith(current_string.lower())]
        return {
            'spec': suggestions,
        }
