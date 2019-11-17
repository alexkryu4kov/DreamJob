import pytest

from app.models.profile.complete.request_parser import RequestParser
from app.models.spec.suggester import SuggesterCreator
from app.models.skills.parse_request import ParseRequest


@pytest.fixture
def suggester():
    creator = SuggesterCreator()
    creator.current_string = 'pyt'
    creator.vacancies_names = ['python developer']
    return creator


@pytest.fixture
def request_parser():
    return ParseRequest()


@pytest.fixture
def complete_parser():
    return RequestParser()


