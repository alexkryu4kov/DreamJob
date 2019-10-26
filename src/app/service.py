from aiohttp.web import Application
from aiohttp import web

from app.settings import setup_profile_predictor, setup_skills_predictor, setup_spec_predictor, setup_vacancies_predictor

from app.routes import setup_routes


async def init_app():
    """Иницализация приложения."""
    app = Application()
    setup_routes(app)
    app.on_startup.append(setup_spec_predictor)
    app.on_startup.append(setup_vacancies_predictor)
    app.on_startup.append(setup_skills_predictor)
    app.on_startup.append(setup_profile_predictor)
    return app


def start():
    """Точка входа."""
    app = init_app()
    web.run_app(
        app,
        port=8080,
        access_log=None,
    )


if __name__ == '__main__':
    start()