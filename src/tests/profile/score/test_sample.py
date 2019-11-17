from app.models.profile.score.count_score import count_score


def test_count_score():
    assert count_score(['python'], ['android']) == 0.5
