class ProfilePredictor:
    async def get_known(self, email, db):
        data = await db.fetch(f"SELECT * FROM email_known WHERE email='{email}'")
        skills = list(set([row['known'] for row in data]))
        return {
            'known': skills,
        }

    async def get_courses(self, skill, db):
        data = await db.fetch(f"SELECT * FROM courses WHERE skill='{skill}'")
        return {
            'url': data[0]['url'],
            'name': data[0]['name'],
            }

    async def get_unknown(self, email, db):
        data = await db.fetch(f"SELECT * FROM email_unknown WHERE email='{email}'")
        skills = list(set([row['unknown'] for row in data]))
        return [
            {
                'name': skill,
                'courses': [await self.get_courses(skill, db)]
            }
            for skill in skills
        ]

    async def get_score(self, email, db):
        known_data = await db.fetch(f"SELECT * FROM email_known WHERE email='{email}'")
        unknown_data = await db.fetch(f"SELECT * FROM email_unknown WHERE email='{email}'")
        try:
            return {
                'score': round(len(known_data)/(len(known_data)+len(unknown_data)), 2),
            }
        except ZeroDivisionError:
            return {
                'score': 0,
            }

    async def post_profile(self, data, db):
        skill = data['skill']
        email = data['email']
        await db.execute(f"INSERT INTO email_known (email, known) VALUES ('{email}', '{skill}')")
        await db.execute(f"DELETE FROM email_unknown WHERE email='{email}' AND unknown='{skill}'")
        return {
            'status': 'OK',
        }
