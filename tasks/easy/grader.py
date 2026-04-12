def grade(rewards):
    if not rewards:
        return 0.0
    score = sum(rewards) / len(rewards)
    return min(max(score, 0.0), 1.0)