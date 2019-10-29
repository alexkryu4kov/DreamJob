class SkillsPredictor:
    def post_skills(self, data, db):
        print(data)
        known = []
        unknown = []
        skills = []
        email = data['email']
        for elem in data['skillsItemUiModel']:
            skills.append({'name': elem['name'],
                           'selected': elem['selected']['mValue'],
                           })
        for skill in skills:
            if skill['selected']:
                known.append(skill['name'])
            else:
                unknown.append(skill['name'])
        self.save_data(db, email, known, unknown)
        return {
            'status': 'OK',
        }

    def save_data(self, db, email, known, unknown):
        [db.cur.execute(f"INSERT INTO email_known (email, known) VALUES ('{email}', '{elem}');") for elem in known]
        [db.cur.execute(f"INSERT INTO email_unknown (email, unknown) VALUES ('{email}', '{elem}');") for elem in unknown]
        db.conn.commit()
