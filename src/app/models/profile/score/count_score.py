def count_score(known: list, unknown: list) -> float:
    try:
        score = len(known) / (len(known) + len(unknown))
        return round(score, 2)
    except ZeroDivisionError:
        return 0.0
