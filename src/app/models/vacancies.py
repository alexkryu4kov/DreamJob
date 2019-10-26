class VacanciesPredictor:
    def create_list_of_vacancies(self, data):
        return [
            {
                'name': row.name,
                'level': row.level,
                'company_name': row.company_name,
                'city': row.city,
                'salary': row.salary,
                'skills': ['Python', 'Web', 'Java']
            } for row in data
        ]

    def get_vacancies(self, name, level, db):
        db.cur.execute(f"SELECT * FROM vacancies WHERE name='{name}' AND level='{level.capitalize()}';")
        row_data = db.cur.fetchall()
        return self.create_list_of_vacancies(row_data)
