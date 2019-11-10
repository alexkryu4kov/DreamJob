import pytest
from yarl import URL


@pytest.fixture
def url():
    return URL('http://206.81.5.208:8080')
