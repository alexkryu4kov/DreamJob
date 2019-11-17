from tests.constants import complete_request


def test_parse(complete_parser):
    complete_parser.parse(complete_request)
    assert complete_parser.email == 'aaa@aaa.aaa'
    assert complete_parser.skill == 'python'
