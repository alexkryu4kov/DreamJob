from aiohttp.web_app import Application

from app.external.config import db_config
from app.external.db import Db
from app.external.init_db import init_database
from app.helpers import get_unique_list
from app.models.spec.predictor import SpecPredictor
from app.models.skills.predictor import SkillsPredictor
from app.models.vacancies.predictor import VacanciesPredictor
from app.models.profile.predictor import ProfilePredictor


async def setup_spec_predictor(aioapp: Application):
    predictor = SpecPredictor()
    aioapp['spec_predictor'] = predictor


async def setup_skills_predictor(aioapp: Application):
    predictor = SkillsPredictor()
    aioapp['skills_predictor'] = predictor


async def setup_vacancies_predictor(aioapp: Application):
    predictor = VacanciesPredictor()
    aioapp['vacancies_predictor'] = predictor


async def setup_profile_predictor(aioapp: Application):
    predictor = ProfilePredictor()
    aioapp['profile_predictor'] = predictor


async def setup_db(aioapp: Application):
    aioapp['db'] = await init_database(db_config)
    Db.db = aioapp['db']


async def on_shutdown(app):
    await app['db'].close()


def create_list_of_names(data: list) -> list:
    return get_unique_list([row['name'].lower() for row in data])


async def create_vacancies_names(app):
    row_data = await app['db'].fetch("SELECT * FROM vacancies;")
    app['vacancies_names'] = create_list_of_names(row_data)
