import aiohttp_cors

from app.api import handler


def setup_routes(app):
    """Добавлена точка входа для приложения."""
    cors = aiohttp_cors.setup(app, defaults={
        '*': aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers='*',
            allow_headers='*',
        ),
    })

    cors.add(app.router.add_get('/spec', handler.spec_handler))
    cors.add(app.router.add_get('/vacancies', handler.vacancies_handler))
    cors.add(app.router.add_post('/skills', handler.skills_handler))
    cors.add(app.router.add_get('/profile', handler.profile_handler))
