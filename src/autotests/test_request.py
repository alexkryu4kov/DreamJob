import aiohttp
import pytest


@pytest.mark.asyncio
async def test_spec(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}/spec?name=p') as resp:
            assert resp.status == 200


@pytest.mark.asyncio
async def test_vacancies(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}/vacancies?name=python developer&lvl=Middle') as resp:
            assert resp.status == 200


@pytest.mark.asyncio
async def test_skills(url):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{url}/skills', json={
            'email': 'test@test.test', 'skillsItemUiModel': [
                {'layoutId': 2, 'name': 'android', 'selected': {'mValue': True}},
                {'layoutId': 2, 'name': 'git', 'selected': {'mValue': False}}]
        }) as resp:
            assert resp.status == 200


@pytest.mark.asyncio
async def test_roadmaps(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}/roadmaps?email=test@test.test') as resp:
            assert resp.status == 200


@pytest.mark.asyncio
async def test_profile_known(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}/profile/known?email=test@test.test') as resp:
            assert resp.status == 200


@pytest.mark.asyncio
async def test_profile_unknown(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}/profile/unknown?email=test@test.test') as resp:
            assert resp.status == 200


@pytest.mark.asyncio
async def test_profile_score(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}/profile/score?email=test@test.test') as resp:
            assert resp.status == 200


@pytest.mark.asyncio
async def test_profile_complete(url):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{url}/profile/complete', json={
            'email': 'test@test.test', 'skill': 'git'
        }) as resp:
            assert resp.status == 200


@pytest.mark.asyncio
async def test_profile_courses(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}/profile/courses?skill=python') as resp:
            assert resp.status == 200
