import aiohttp
import pytest


@pytest.mark.asyncio
async def test_spec(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}/spec?name=p') as resp:
            print(resp)
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
            'email': 'aaa@aaa.aaa', 'skillsItemUiModel': [
                {'layoutId': 2, 'name': 'android', 'selected': {'mValue': True}},
                {'layoutId': 2, 'name': 'git', 'selected': {'mValue': False}}]
        }) as resp:
            assert resp.status == 200


@pytest.mark.asyncio
async def test_profile_known(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}/profile/known?email=aaa@aaa.aaa') as resp:
            assert resp.status == 200


@pytest.mark.asyncio
async def test_profile_unknown(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}/profile/unknown?email=aaa@aaa.aaa') as resp:
            assert resp.status == 200


@pytest.mark.asyncio
async def test_profile_score(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}/profile/score?email=aaa@aaa.aaa') as resp:
            assert resp.status == 200


@pytest.mark.asyncio
async def test_profile_complete(url):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{url}/profile/complete', json={
            'email': 'aaa@aaa.aaa', 'skill': 'git'
        }) as resp:
            assert resp.status == 200
