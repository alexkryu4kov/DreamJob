from app.external.abstract_db import AbstractDbWorker
from app.mock import vacancies, skills, adv_skills, courses, users, email_known, email_unknown, email_course

db_config = {
    'user': 'jcoqxhnbbdmhej',
    'password': '6634869b448b0e129b789480e55230d35087d0bca4760416e7ac3aae61654982',
    'host': 'ec2-174-129-231-116.compute-1.amazonaws.com',
    'port': 5432,
    'dbname': 'da7ht06l1b358e',
    'sslmode': 'require'
}


class DbWorker(AbstractDbWorker):
    def __init__(self, config):
        super().__init__(config)


db = DbWorker(db_config)
#db.cur.execute(f"INSERT INTO vacancies (name, level, company_name, city, salary, url) VALUES ('{vacancies['name']}','{vacancies['level']}','{vacancies['company_name']}','{vacancies['city']}','{vacancies['salary']}','{vacancies['url']}');")
#db.cur.execute(f"INSERT INTO skills (vacancy_url, skill) VALUES ('{skills['vacancy_url']}','{skills['skill']}');")
#db.cur.execute(f"INSERT INTO adv_skills (skill, adv_skill) VALUES ('{adv_skills['skill']}','{adv_skills['adv_skill']}');")
#db.cur.execute(f"INSERT INTO courses (name, url, skill) VALUES ('{courses['name']}','{courses['url']}','{courses['skill']}');")
#db.cur.execute(f"INSERT INTO users (email) VALUES ('{users['email']}');")
#db.cur.execute(f"INSERT INTO email_known (email, known) VALUES ('{email_known['email']}','{email_known['known']}');")
#db.cur.execute(f"INSERT INTO email_unknown (email, unknown) VALUES ('{email_unknown['email']}','{email_unknown['unknown']}');")
#db.cur.execute(f"INSERT INTO email_course (email, course) VALUES ('{email_course['email']}','{email_course['course']}');")
#db.conn.commit()
db.cur.execute("SELECT * FROM vacancies;")
data = db.cur.fetchall()
