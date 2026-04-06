from env.env import DeceptionEnv
from env.attacker import brute_force

def run():

    brute_force()

    env = DeceptionEnv()
    env.reset()

    total_reward = 0

    _, r, _, _ = env.step("detect_attack")
    total_reward += r

    _, r, _, _ = env.step("deploy_honeypot")
    total_reward += r

    return total_reward
