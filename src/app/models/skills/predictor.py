# TODO: исправть асинхрон в save_data

import asyncio


class SkillsPredictor:
    def __init__(self):
        self._known = []
        self._unknown = []
        self._skills = []
        self._db = None
        self._email = None

    def _set_db(self, db):
        self._db = db

    def _set_email(self, data):
        self._email = data['email'].lower()

    def _set_skills(self, data):
        for elem in data['skillsItemUiModel']:
            self._skills.append({'name': elem['name'],
                                 'selected': elem['selected']['mValue'],
                                 })

    def _set_known_unknown(self):
        for skill in self._skills:
            if skill['selected']:
                self._known.append(skill['name'])
            else:
                self._unknown.append(skill['name'])

    def _parse_response(self, data):
        self._set_email(data)
        self._set_skills(data)
        self._set_known_unknown()

    async def post_skills(self, data, db):
        self._set_db(db)
        self._parse_response(data)
        await self.save_data()
        return {
            'status': 'OK',
        }

    async def db_execute_known(self, elem):
        con = await self._db.acquire()
        await con.execute('''INSERT INTO email_known (email, known) VALUES ($1, $2)''', self._email, elem)
        await self._db.release(con)

    async def db_execute_unknown(self, elem):
        con = await self._db.acquire()
        await con.execute('''INSERT INTO email_unknown (email, unknown) VALUES ($1, $2)''', self._email, elem)
        await self._db.release(con)

    async def save_data(self):
        tasks_known = [asyncio.create_task(self.db_execute_known(elem)) for elem in self._known]
        tasks_unknown = [asyncio.create_task(self.db_execute_unknown(elem)) for elem in self._unknown]
        tasks = tasks_known + tasks_unknown
        await asyncio.gather(*tasks)
