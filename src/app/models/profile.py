class ProfilePredictor:
    def get_known(self, email, db):
        print('email', email)
        db.cur.execute(f"SELECT * FROM email_known")
        test_data = db.cur.fetchall()
        print('test_data', test_data)
        db.cur.execute("SELECT * FROM email_known WHERE email=%s", (email,))
        data = db.cur.fetchall()
        print('data', data)
        skills = list(set([row.known for row in data]))
        print('skills', skills)
        return {
            'known': skills,
        }

    def get_courses(self, skill, db):
        db.cur.execute(f"SELECT * FROM courses WHERE skill='{skill}'")
        data = db.cur.fetchall()
        return {
            'url': data[0].url,
            'name': data[0].name
            }

    def get_unknown(self, email, db):
        db.cur.execute(f"SELECT * FROM email_unknown WHERE email='{email}'")
        data = db.cur.fetchall()
        skills = list(set([row.unknown for row in data]))
        return [
            {
                'name': skill,
                'courses': [self.get_courses(skill, db)]
            }
            for skill in skills
        ]

    def get_score(self, email, db):
        db.cur.execute(f"SELECT * FROM email_known WHERE email='{email}'")
        known_data = db.cur.fetchall()
        db.cur.execute(f"SELECT * FROM email_unknown WHERE email='{email}'")
        unknown_data = db.cur.fetchall()
        try:
            return {
                'score': round(len(known_data)/(len(known_data)+len(unknown_data)), 2),
            }
        except ZeroDivisionError:
            return {
                'score': 0,
            }

    def post_profile(self, data, db):
        skill = data['skill']
        email = data['email']
        db.cur.execute(f"INSERT INTO email_known (email, known) VALUES ('{email}', '{skill}')")
        db.cur.execute(f"DELETE FROM email_unknown WHERE email='{email}' AND unknown='{skill}'")
        return {
            'status': 'OK',
        }
