from env.env import DeceptionEnv
from env.attacker import brute_force

def run():

    brute_force()

    env = DeceptionEnv()

    env.reset()

    state, reward, done, _ = env.step("detect_attack")

    return reward
