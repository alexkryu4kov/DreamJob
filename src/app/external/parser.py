import requests


class VacancyParser:
    def __init__(self):
        self.levels = ['стажер', 'intern', 'стажёр', 'junior', 'младший', 'senior', 'старший']
        self.url = 'https://api.hh.ru/vacancies?text='
        self.items = None

    def get_items(self, keyword):
        data = requests.get(f'{self.url}{keyword}')
        self.items = data.json()['items']

    def get_name(self, item):
        try:
            return ' '.join([name.lower() for name in item['name'].split(' ') if name.lower() not in self.levels])
        except KeyError:
            return ''

    def get_salary(self, item):
        try:
            if item['salary']['currency'] == 'RUR':
                try:
                    if item['salary']['from'] is not None:
                        return (item['salary']['from'] + item['salary']['to']) / 2
                    return 0
                except TypeError:
                    return 0
            else:
                return 0
        except TypeError:
            return 0

    def get_level(self, item):
        name = [name.lower() for name in item['name'].split(' ')]
        if 'intern' in name or 'стажер' in name or 'стажёр' in name:
            return 'Intern'
        if 'junior' in name or 'младший' in name:
            return 'Junior'
        if 'senior' in name or 'старший' in name:
            return 'Senior'
        return 'Middle'

    def get_id(self, item):
        try:
            return item['url'].split('vacancies/')[1].split('?')[0]
        except KeyError:
            return ''

    def get_url(self, item):
        return f'https://hh.ru/vacancy/{self.get_id(item)}'

    def get_city(self, item):
        try:
            return item['area']['name']
        except KeyError:
            return ''

    def get_company_name(self, item):
        try:
            return item['employer']['name']
        except KeyError:
            return ''

    def get_description(self, item):
        req = requests.get(f"https://api.hh.ru/vacancies/{self.get_id(item)}")
        try:
            return req.json()['description']
        except KeyError:
            return ''

    def get_vacancies(self):
        vacancies = []
        for item in self.items:
            vacancies.append(
                {
                    'name': self.get_name(item),
                    'salary': self.get_salary(item),
                    'level': self.get_level(item),
                    'url': self.get_url(item),
                    'city': self.get_city(item),
                    'company_name': self.get_company_name(item),
                }
            )
        return vacancies

    def get_skills(self):
        skills = []
        for item in self.items:
            skills.append(
                {
                    'vacancy_url': self.get_url(item),
                    'skill': self.get_description(item),
                }
            )
        return skills
