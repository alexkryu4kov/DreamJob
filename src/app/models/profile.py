class ProfilePredictor:
    def get_known(self, email, db):
        db.cur.execute(f"SELECT * FROM email_known WHERE email='{email}'")
        data = db.cur.fetchall()
        skills = [row.known for row in data]
        return {
            'known': skills,
        }

    def get_unknown(self, email, db):
        db.cur.execute(f"SELECT * FROM email_unknown WHERE email='{email}'")
        data = db.cur.fetchall()
        skills = [row.unknown for row in data]
        return [
            {
                'name': skill,
                'courses': [{
                    'url': 'http://https://www.udemy.com/course/java-tutorial/',
                    'name': 'How to be Java developer',
                }
                ]
            }
            for skill in skills
        ]

    def post_profile(self, data):
        return {
            'status': 'OK',
        }
