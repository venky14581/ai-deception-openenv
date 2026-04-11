from env.env import DeceptionEnv
from env.attacker import brute_force, port_scan, credential_stuffing


def run():

    env = DeceptionEnv()
    env.reset()

    brute_force()
    port_scan()
    credential_stuffing()

    total_reward = 0

    _, r, _, _ = env.step("detect_attack")
    total_reward += r

    _, r, _, _ = env.step("deploy_honeypot")
    total_reward += r

    _, r, _, _ = env.step("fake_database")
    total_reward += r

    _, r, _, _ = env.step("block_ip")
    total_reward += r

    return total_reward
