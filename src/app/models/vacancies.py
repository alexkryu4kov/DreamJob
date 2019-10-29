class VacanciesPredictor:
    def create_list_of_vacancies(self, db, data):
        return [
            {
                'name': row.name,
                'level': row.level,
                'company_name': row.company_name,
                'city': row.city,
                'salary': row.salary,
                'skills': self.get_list_of_skills(db, row.url)
            } for row in data
        ]

    def get_list_of_skills(self, db, url):
        db.cur.execute(f"SELECT * FROM skills WHERE vacancy_url='{url}'")
        data = db.cur.fetchall()
        return list(set([row.skill for row in data]))

    def get_vacancies(self, name, level, db):
        email = 'Leha@idi.na'
        db.cur.execute(f"SELECT * FROM email_known WHERE email={email}")
        data = db.cur.fetchall()
        print('data', data)
        email = 'Leha@idi.na'
        db.cur.execute(f"SELECT * FROM email_known WHERE email='{email}'")
        test_data = db.cur.fetchall()
        print('test_data', test_data)
        db.cur.execute(f"SELECT * FROM vacancies WHERE name='{name}' AND level='{level}';")
        row_data = db.cur.fetchall()
        return self.create_list_of_vacancies(db, row_data)
