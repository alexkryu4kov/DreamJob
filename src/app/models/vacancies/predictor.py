class VacanciesPredictor:
    async def create_list_of_vacancies(self, db, data):
        return [
            {
                'name': row['name'],
                'level': row['level'],
                'company_name': row['company_name'],
                'city': row['city'],
                'salary': row['salary'],
                'skills': await self.get_list_of_skills(db, row['url'])
            } for row in data
        ]

    async def get_list_of_skills(self, db, url):
        data = await db.fetch(f"SELECT * FROM skills WHERE vacancy_url='{url}'")
        return list(set([row['skill'] for row in data]))

    async def get_vacancies(self, name, level, db):
        row_data = await db.fetch(f"SELECT * FROM vacancies WHERE name='{name}' AND level='{level}';")
        return await self.create_list_of_vacancies(db, row_data)
