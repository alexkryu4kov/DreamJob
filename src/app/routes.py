import aiohttp_cors

from app.api import profile, roadmaps, skills, spec, vacancies


def setup_routes(app):
    """Добавлена точка входа для приложения."""
    cors = aiohttp_cors.setup(app, defaults={
        '*': aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers='*',
            allow_headers='*',
        ),
    })

    cors.add(app.router.add_get('/spec', spec.handler))
    cors.add(app.router.add_get('/vacancies', vacancies.handler))
    cors.add(app.router.add_post('/skills', skills.handler))
    cors.add(app.router.add_get('/profile/known', profile.known_handler))
    cors.add(app.router.add_get('/profile/unknown', profile.unknown_handler))
    cors.add(app.router.add_get('/profile/score', profile.score_handler))
    cors.add(app.router.add_post('/profile/complete', profile.complete_handler))
    cors.add(app.router.add_get('/profile/courses', profile.courses_handler))
    cors.add(app.router.add_get('/roadmaps', roadmaps.handler))
