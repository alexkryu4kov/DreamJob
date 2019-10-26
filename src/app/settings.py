from aiohttp.web_app import Application

from app.external.config import db_config
from app.external.db import DbWorker
from app.models.spec import SpecPredictor
from app.models.skills import SkillsPredictor
from app.models.vacancies import VacanciesPredictor
from app.models.profile import ProfilePredictor


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
    db = DbWorker(db_config)
    aioapp['db'] = db


def create_list_of_names(data: list) -> list:
    return [row.name.lower() for row in data]


async def create_vacancies_names(app):
    app['db'].cur.execute("SELECT * FROM vacancies;")
    row_data = app['db'].cur.fetchall()
    app['vacancies_names'] = create_list_of_names(row_data)


async def on_shutdown(app):
    await app['db'].close()
