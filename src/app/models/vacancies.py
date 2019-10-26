class VacanciesPredictor:
    def get_vacancies(self, name, level):
        return {
            'name': f'{name} developer',
            'level': level,
            'company_name': 'CFT',
            'salary': 31000,
            'skills': ['Python', 'Web', 'Java'],
        }
