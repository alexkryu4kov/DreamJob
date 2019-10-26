import requests

levels = ['стажер', 'intern', 'стажёр', 'junior', 'младший', 'senior', 'старший']


class VacancyParser:
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies?text='
        self.items = None

    def get_items(self, keyword):
        data = requests.get(f'{self.url}{keyword}')
        self.items = data.json()['items'][5:10]

    def get_name(self, item):
        try:
            return ' '.join([name.lower() for name in item['name'].split(' ') if name.lower() not in levels])
        except KeyError:
            return ''

    def get_salary(self, item):
        try:
            if item['salary']['currency'] == 'RUR':
                try:
                    return (item['salary']['from'] + item['salary']['to'])/2
                except TypeError:
                    return item['salary']['from']
        except TypeError:
            return 0

    def get_level(self, item):
        name = self.get_name(item)
        if 'intern' in name or 'стажер' in name or 'стажёр' in name:
            return 'Intern'
        if 'junior' in name or 'младший' in name:
            return 'Junior'
        if 'senior' in name or 'старший' in name:
            return 'Senior'
        return 'Middle'

    def get_url(self, item):
        try:
            return item['employer']['vacancies_url']
        except KeyError:
            return ''

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
        try:
            return item['snippet']['requirement']
        except KeyError:
            return ''

    def get_list_of_vacancies(self):
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
                    'description': self.get_description(item),
                }
            )
        return vacancies


parser = VacancyParser()
parser.get_items('Python')
print(parser.items)
print(parser.get_list_of_vacancies())
