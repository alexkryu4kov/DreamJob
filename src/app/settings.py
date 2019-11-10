from aiohttp.web_app import Application

from app.external.config import db_config
from app.external.db import Db
from app.external.init_db import init_database
from app.helpers import create_list_of_names
from app.models.profile.predictor import ProfilePredictor
from app.models.skills.predictor import SkillsPredictor
from app.models.spec.predictor import SpecPredictor
from app.models.vacancies.predictor import VacanciesPredictor


async def setup_spec_predictor(aioapp: Application):
    aioapp['spec_predictor'] = SpecPredictor()


async def setup_skills_predictor(aioapp: Application):
    aioapp['skills_predictor'] = SkillsPredictor()


async def setup_vacancies_predictor(aioapp: Application):
    aioapp['vacancies_predictor'] = VacanciesPredictor()


async def setup_profile_predictor(aioapp: Application):
    aioapp['profile_predictor'] = ProfilePredictor()


async def setup_db(aioapp: Application):
    aioapp['db'] = await init_database(db_config)
    Db.db = aioapp['db']


async def on_shutdown(app):
    await app['db'].close()


async def create_vacancies_names(app):
    connection = await app['db'].acquire()
    row_data = await connection.fetch('''SELECT * FROM vacancies''')
    app['vacancies_names'] = create_list_of_names(row_data)
    await app['db'].release(connection)
