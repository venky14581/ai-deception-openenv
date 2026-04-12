def grade(rewards):
    if not rewards:
        return 0.0

    score = sum(rewards) / len(rewards)
    score = score * 0.8
    return min(max(score, 0.0), 1.0)