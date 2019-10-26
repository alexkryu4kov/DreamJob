from aiohttp import web


async def spec_handler(request):
    name = request.rel_url.query['name']
    response_data = request.app['spec_predictor'].get_spec(name, request.app['vacancies_names'])

    return web.json_response(response_data)


async def vacancies_handler(request):
    name = request.rel_url.query['name']
    level = request.rel_url.query['lvl']
    response_data = request.app['vacancies_predictor'].get_vacancies(name, level)

    return web.json_response(response_data)


async def skills_handler(request):
    request_data = await request.json()
    response_data = request.app['skills_predictor'].post_skills(request_data)

    return web.json_response(response_data)


async def profile_known_handler(request):
    email = request.rel_url.query['email']
    response_data = request.app['profile_predictor'].get_profile(email)
    known_response_data = {key: response_data[key] for key in ['known']}

    return web.json_response(known_response_data)


async def profile_unknown_handler(request):
    email = request.rel_url.query['email']
    response_data = request.app['profile_predictor'].get_profile(email)
    unknown_response_data = {key: response_data[key] for key in ['unknown']}

    return web.json_response(unknown_response_data)


async def profile_courses_handler(request):
    email = request.rel_url.query['email']
    response_data = request.app['profile_predictor'].get_profile(email)
    courses_response_data = {key: response_data[key] for key in ['courses']}

    return web.json_response(courses_response_data)
