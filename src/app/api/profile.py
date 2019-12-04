import logging
import time

from aiohttp import web


async def known_handler(request):
    start_time = time.time()
    try:
        email = request.query['email']
        response_data = await request.app['profile_predictor'].get_known(email)
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
        time_log = round(time.time() - start_time, 3)
        method_log = request.method
        request_log = str(request.rel_url)
        error_log = str(e)
        logging.error(
            {
                'time': time_log,
                'method': method_log,
                'request': request_log,
                'error': error_log,
            }
        )
        await request.app['db'].execute('''INSERT INTO logs (time, method, request, error) VALUES ($1, $2, $3, $4)''',
                                        time_log, method_log, request_log, error_log)


async def unknown_handler(request):
    start_time = time.time()
    try:
        email = request.query['email']
        response_data = await request.app['profile_predictor'].get_unknown(email)
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
        time_log = round(time.time() - start_time, 3)
        method_log = request.method
        request_log = str(request.rel_url)
        error_log = str(e)
        logging.error(
            {
                'time': time_log,
                'method': method_log,
                'request': request_log,
                'error': error_log,
            }
        )
        await request.app['db'].execute('''INSERT INTO logs (time, method, request, error) VALUES ($1, $2, $3, $4)''',
                                        time_log, method_log, request_log, error_log)


async def score_handler(request):
    start_time = time.time()
    try:
        email = request.query['email']
        response_data = await request.app['profile_predictor'].get_score(email)
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
        time_log = round(time.time() - start_time, 3)
        method_log = request.method
        request_log = str(request.rel_url)
        error_log = str(e)
        logging.error(
            {
                'time': time_log,
                'method': method_log,
                'request': request_log,
                'error': error_log,
            }
        )
        await request.app['db'].execute('''INSERT INTO logs (time, method, request, error) VALUES ($1, $2, $3, $4)''',
                                        time_log, method_log, request_log, error_log)


async def complete_handler(request):
    start_time = time.time()
    try:
        request_data = await request.json()
        response_data = await request.app['profile_predictor'].complete_profile(request_data)
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
        time_log = round(time.time() - start_time, 3)
        method_log = request.method
        request_log = str(request.rel_url)
        error_log = str(e)
        logging.error(
            {
                'time': time_log,
                'method': method_log,
                'request': request_log,
                'error': error_log,
            }
        )
        await request.app['db'].execute('''INSERT INTO logs (time, method, request, error) VALUES ($1, $2, $3, $4)''',
                                        time_log, method_log, request_log, error_log)


async def courses_handler(request):
    start_time = time.time()
    try:
        skill = request.query['skill']
        response_data = await request.app['profile_predictor'].get_courses(skill)
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
        time_log = round(time.time() - start_time, 3)
        method_log = request.method
        request_log = str(request.rel_url)
        error_log = str(e)
        logging.error(
            {
                'time': time_log,
                'method': method_log,
                'request': request_log,
                'error': error_log,
            }
        )
        await request.app['db'].execute('''INSERT INTO logs (time, method, request, error) VALUES ($1, $2, $3, $4)''',
                                        time_log, method_log, request_log, error_log)
