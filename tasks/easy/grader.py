def grade(rewards):
    score = sum(rewards) / len(rewards)
    return min(max(score, 0.0), 1.0)