from tests.constants import skills_request


def test_set_email_known_unknown(request_parser):
    request_parser.set_email_known_unknown(skills_request)
    assert request_parser.known == ['android']
    assert request_parser.unknown == ['git']
