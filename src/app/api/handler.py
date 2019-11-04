import logging
import time

from aiohttp import web


async def spec_handler(request):
    start_time = time.time()
    try:
        name = request.query['name']
        response_data = request.app['spec_predictor'].get_spec(name, request.app['vacancies_names'])
        logging.info(
            {
                'time': round(time.time() - start_time, 3),
                'method': request.method,
                'request': str(request.rel_url),
                'response': response_data,
            }
        )
        return web.json_response(response_data)

    except Exception as e:
        logging.error(
            {
                'time': round(time.time() - start_time, 3),
                'method': request.method,
                'request': str(request.rel_url),
                'error': str(e),
            }
        )


async def vacancies_handler(request):
    start_time = time.time()
    try:
        name = request.query['name']
        level = request.query['lvl']
        response_data = await request.app['vacancies_predictor'].get_vacancies(name, level, request.app['db'])
        logging.info(
            {
                'time': round(time.time() - start_time, 3),
                'method': request.method,
                'request': str(request.rel_url),
                'response': response_data,
            }
        )
        return web.json_response(response_data)

    except Exception as e:
        logging.error(
            {
                'time': round(time.time() - start_time, 3),
                'method': request.method,
                'request': str(request.rel_url),
                'error': str(e),
            }
        )


async def skills_handler(request):
    start_time = time.time()
    try:
        request_data = await request.json()
        response_data = await request.app['skills_predictor'].post_skills(request_data, request.app['db'])
        logging.info(
            {
                'time': round(time.time() - start_time, 3),
                'method': request.method,
                'request': str(request.rel_url),
                'response': response_data,
            }
        )
        return web.json_response(response_data)

    except Exception as e:
        logging.error(
            {
                'time': time.time() - start_time,
                'method': request.method,
                'request': str(request.rel_url),
                'error': str(e),
            }
        )


async def profile_known_handler(request):
    start_time = time.time()
    try:
        email = request.query['email']
        response_data = await request.app['profile_predictor'].get_known(email, request.app['db'])
        logging.info(
            {
                'time': round(time.time() - start_time, 3),
                'method': request.method,
                'request': str(request.rel_url),
                'response': response_data,
            }
        )
        return web.json_response(response_data)

    except Exception as e:
        logging.error(
            {
                'time': round(time.time() - start_time, 3),
                'method': request.method,
                'request': str(request.rel_url),
                'error': str(e),
            }
        )


async def profile_unknown_handler(request):
    start_time = time.time()
    try:
        email = request.query['email']
        response_data = await request.app['profile_predictor'].get_unknown(email, request.app['db'])
        logging.info(
            {
                'time': round(time.time() - start_time, 3),
                'method': request.method,
                'request': str(request.rel_url),
                'response': response_data,
            }
        )
        return web.json_response(response_data)

    except Exception as e:
        logging.error(
            {
                'time': round(time.time() - start_time, 3),
                'method': request.method,
                'request': str(request.rel_url),
                'error': str(e),
            }
        )


async def profile_score_handler(request):
    start_time = time.time()
    try:
        email = request.query['email']
        response_data = await request.app['profile_predictor'].get_score(email, request.app['db'])
        logging.info(
            {
                'time': round(time.time() - start_time, 3),
                'method': request.method,
                'request': str(request.rel_url),
                'response': response_data,
            }
        )
        return web.json_response(response_data)

    except Exception as e:
        logging.error(
            {
                'time': round(time.time() - start_time, 3),
                'method': request.method,
                'request': str(request.rel_url),
                'error': str(e),
            }
        )


async def profile_complete_handler(request):
    start_time = time.time()
    try:
        request_data = await request.json()
        response_data = await request.app['profile_predictor'].complete_profile(request_data, request.app['db'])
        logging.info(
            {
                'time': round(time.time() - start_time, 3),
                'method': request.method,
                'request': str(request.rel_url),
                'response': response_data,
            }
        )
        return web.json_response(response_data)

    except Exception as e:
        logging.error(
            {
                'time': round(time.time() - start_time, 3),
                'method': request.method,
                'request': str(request.rel_url),
                'error': str(e),
            }
        )
