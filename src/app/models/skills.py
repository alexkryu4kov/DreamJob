class SkillsPredictor:
    async def post_skills(self, data, db):
        print(data)
        known = []
        unknown = []
        skills = []
        email = data['email'].lower()
        for elem in data['skillsItemUiModel']:
            skills.append({'name': elem['name'],
                           'selected': elem['selected']['mValue'],
                           })
        for skill in skills:
            if skill['selected']:
                known.append(skill['name'])
            else:
                unknown.append(skill['name'])
        print('known', known)
        print('unknown', unknown)
        await self.save_data(db, email, known, unknown)
        return {
            'status': 'OK',
        }

    async def db_execute_known(self, db, email, elem):
        await db.execute('''INSERT INTO email_known (email, known) VALUES ($1, $2)''', email, elem)

    async def db_execute_unknown(self, db, email, elem):
        return await db.execute('''INSERT INTO email_unknown (email, unknown) VALUES ($1, $2)''', email, elem)

    async def save_data(self, db, email, known, unknown):
        [await self.db_execute_known(db, email, elem) for elem in known]
        [await self.db_execute_unknown(db, email, elem) for elem in unknown]
