from aiohttp import web


async def spec_handler(request):
    name = request.rel_url.query['name']
    response_data = request.app['spec_predictor'].get_spec(name)

    return web.json_response(response_data)


async def vacancies_handler(request):
    name = request.rel_url.query['name']
    print(name)
    level = request.rel_url.query['lvl']
    response_data = request.app['vacancies_predictor'].get_vacancies(name, level)

    return web.json_response(response_data)


async def skills_handler(request):
    request_data = await request.json()
    response_data = request.app['skills_predictor'].post_skills(request_data)

    return web.json_response(response_data)


async def profile_handler(request):
    email = request.rel_url.query['email']
    response_data = request.app['profile_predictor'].get_profile(email)

    return web.json_response(response_data)