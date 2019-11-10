import aiohttp
import pytest


@pytest.mark.asyncio
async def test_spec(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url / 'spec?name=p') as resp:
            print(resp)
            print(resp.status)


@pytest.mark.asyncio
async def test_vacancies(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url / 'vacancies?name=python developer&lvl=Middle') as resp:
            print(resp)
            print(resp.status)


@pytest.mark.asyncio
async def test_skills(url):
    async with aiohttp.ClientSession() as session:
        async with session.post(url / 'skills', json={
            'email': 'lll@lll.lll', 'skillsItemUiModel': [
                {'layoutId': 2, 'name': 'android', 'selected': {'mValue': 'True'}},
                {'layoutId': 2, 'name': 'git', 'selected': {'mValue': 'False'}}]
        }) as resp:
            print(resp)
            print(resp.status)


@pytest.mark.asyncio
async def test_profile_known(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url / 'profile/known?email=aaa@aaa.aaa') as resp:
            print(resp)
            print(resp.status)


@pytest.mark.asyncio
async def test_profile_unknown(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url / 'profile/unknown?email=aaa@aaa.aaa') as resp:
            print(resp)
            print(resp.status)


@pytest.mark.asyncio
async def test_profile_score(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url / 'profile/score?email=aaa@aaa.aaa') as resp:
            print(resp)
            print(resp.status)


@pytest.mark.asyncio
async def test_profile_complete(url):
    async with aiohttp.ClientSession() as session:
        async with session.post(url / 'profile/complete', json={
            'email': 'lll@lll.lll', 'skill': 'git'
        }) as resp:
            print(resp)
            print(resp.status)
