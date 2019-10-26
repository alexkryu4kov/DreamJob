class VacanciesPredictor:
    def get_vacancies(self, name, level):
        return {
            'vacancies_list': [
                {
                    'name': f'{name} developer',
                    'level': level,
                    'company_name': 'CFT',
                    'city': 'Moscow',
                    'salary': 31000,
                    'skills': ['Python', 'Web', 'Java']
                },
                {
                    'name': f'{name} developer',
                    'level': level,
                    'company_name': 'CFT',
                    'city': 'Moscow',
                    'salary': 60000,
                    'skills': ['Python', 'Web', 'Java']
                },
                {
                    'name': f'{name} developer',
                    'level': level,
                    'company_name': 'CFT',
                    'city': 'Moscow',
                    'salary': 80000,
                    'skills': ['Python', 'Web', 'Java']
                },
            ]
        }
