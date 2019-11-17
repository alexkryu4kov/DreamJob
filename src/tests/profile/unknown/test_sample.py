from app.models.profile.unknown.find_course import find_course


def test_find_course():
    assert find_course([{
        'url': 'url',
        'name': 'name',
        'skill': 'git'}], 'git') == [{'url': 'url', 'name': 'name'}]
