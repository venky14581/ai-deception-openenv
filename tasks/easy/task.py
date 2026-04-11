from env.env import DeceptionEnv
from env.attacker import brute_force


def run():

    env = DeceptionEnv()
    env.reset()

    brute_force()

    _, reward, _, _ = env.step("detect_attack")

    return reward
