from app.models.spec import SpecPredictor
from app.models.skills import SkillsPredictor
from app.models.vacancies import VacanciesPredictor
from app.models.profile import ProfilePredictor
from aiohttp.web_app import Application


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
