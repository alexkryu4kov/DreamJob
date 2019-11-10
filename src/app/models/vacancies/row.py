from dataclasses import asdict, dataclass

from app.models.vacancies.skills_from_db import SkillsFromDb


@dataclass
class Row:
    id: int
    name: str
    level: str
    company_name: str
    city: str
    salary: int
    url: str
    skills: list = None

    async def set_skills(self):
        skills_from_db = SkillsFromDb()
        self.skills = await skills_from_db.get_list_of_skills(self.url)

    async def create_dict_from_row(self):
        await self.set_skills()
        result = asdict(self)
        del result['id']
        return result

