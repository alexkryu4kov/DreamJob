def test_create_suggestions(suggester):
    assert suggester.create_suggestions() == ['python developer']
