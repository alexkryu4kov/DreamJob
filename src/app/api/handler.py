from aiohttp import web


async def spec_handler(request):
    print('spec', request)
    name = request.rel_url.query['name']
    response_data = request.app['spec_predictor'].get_spec(name, request.app['vacancies_names'])

    return web.json_response(response_data)


async def vacancies_handler(request):
    print('vacancy', request)
    name = request.rel_url.query['name']
    level = request.rel_url.query['lvl']
    print(name, level)
    response_data = request.app['vacancies_predictor'].get_vacancies(name, level, request.app['db'])

    return web.json_response(response_data)


async def skills_handler(request):
    print('skills', request)
    request_data = await request.json()
    print(request_data)
    response_data = request.app['skills_predictor'].post_skills(request_data, request.app['db'])

    return web.json_response(response_data)


async def profile_known_handler(request):
    print('known', request)
    email = request.rel_url.query['email']
    response_data = request.app['profile_predictor'].get_known(email, request.app['db'])

    return web.json_response(response_data)


async def profile_unknown_handler(request):
    print('unknown', request)
    email = request.rel_url.query['email']
    response_data = request.app['profile_predictor'].get_unknown(email, request.app['db'])

    return web.json_response(response_data)


async def profile_score_handler(request):
    print('score', request)
    email = request.rel_url.query['email']
    response_data = request.app['profile_predictor'].get_score(email, request.app['db'])

    return web.json_response(response_data)


async def profile_complete_handler(request):
    print('complete', request)
    request_data = await request.json()
    response_data = request.app['profile_predictor'].post_profile(request_data, request.app['db'])

    return web.json_response(response_data)
