# TODO: сделать класс ProfilePredictor фасадом


from app.helpers import get_unique_list


class ProfilePredictor:

    def __init__(self):
        self._connection = None

    async def _set_connection(self, db):
        self._connection = await db.acquire()

    async def _close_connection(self, db):
        await db.release(self._connection)

    async def get_known(self, email, db):
        await self._set_connection(db)
        data = await self._connection.fetch(f"SELECT * FROM email_known WHERE email='{email}'")
        skills = get_unique_list([row['known'] for row in data])
        await self._close_connection(db)
        return {
            'known': skills,
        }

    async def get_courses(self):
        return await self._connection.fetch("SELECT * FROM courses;")

    def find_course(self, courses, skill):
        for course in courses:
            if course['skill'] == skill:
                return {
                    'url': course['url'],
                    'name': course['name'],
                }

    async def get_unknown(self, email, db):
        await self._set_connection(db)
        data = await self._connection.fetch(f"SELECT * FROM email_unknown WHERE email='{email}'")
        skills = get_unique_list([row['unknown'] for row in data])
        courses = await self.get_courses()
        await self._close_connection(db)
        return [
            {
                'name': skill,
                'courses': self.find_course(courses, skill)
            }
            for skill in skills
        ]

    def count_score(self, known, unknown):
        return round(len(known)/(len(known)+len(unknown)), 2)

    async def get_score(self, email, db):
        await self._set_connection(db)
        known_data = await self._connection.fetch(f"SELECT * FROM email_known WHERE email='{email}'")
        unknown_data = await self._connection.fetch(f"SELECT * FROM email_unknown WHERE email='{email}'")
        await self._close_connection(db)
        try:
            return {
                'score': self.count_score(known_data, unknown_data),
            }
        except ZeroDivisionError:
            return {
                'score': 0,
            }

    async def complete_profile(self, data, db):
        await self._set_connection(db)
        skill = data['skill']
        email = data['email']
        await self._connection.execute(f"INSERT INTO email_known (email, known) VALUES ('{email}', '{skill}')")
        await self._connection.execute(f"DELETE FROM email_unknown WHERE email='{email}' AND unknown='{skill}'")
        await self._close_connection(db)
        return {
            'status': 'OK',
        }
