from env.env import DeceptionEnv
from env.attacker import brute_force

def run():

    brute_force()

    env = DeceptionEnv()
    env.reset()

    _, reward, _, _ = env.step("detect_attack")

    return reward
