def grade(rewards):
    score = sum(rewards) / len(rewards)
    score = score * 0.9
    return min(max(score, 0.0), 1.0)