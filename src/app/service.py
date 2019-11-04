import logging

from aiohttp.web import Application
from aiohttp import web

from app import settings
from app.routes import setup_routes


async def init_app():
    """Иницализация приложения."""
    app = Application()
    logging.basicConfig(level=logging.INFO, filename='logs/sample.log')
    setup_routes(app)
    app.on_startup.append(settings.setup_spec_predictor)
    app.on_startup.append(settings.setup_vacancies_predictor)
    app.on_startup.append(settings.setup_skills_predictor)
    app.on_startup.append(settings.setup_profile_predictor)
    app.on_startup.append(settings.setup_db)
    app.on_startup.append(settings.create_vacancies_names)
    app.on_shutdown.append(settings.on_shutdown)
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
