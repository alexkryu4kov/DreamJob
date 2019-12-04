from copy import deepcopy
from dataclasses import asdict, dataclass


@dataclass
class Row:
    vacancy_id: int
    name: str
    real_name: str
    level: str
    company_name: str
    city: str
    salary: int
    url: str
    skill: str

    def search_by_url(self, skills):
        return [element['skill'] for element in skills if element['vacancy_url'] == self.url]

    def create_dict_from_row(self, skills) -> dict:
        row_dict = asdict(self)
        row_dict['name'] = deepcopy(row_dict['real_name'])
        row_dict['skills'] = skills[self.vacancy_id]
        del row_dict['url']
        del row_dict['real_name']
        del row_dict['skill']
        del row_dict['vacancy_id']
        return row_dict
