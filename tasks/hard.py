from env.env import DeceptionEnv
from env.attacker import brute_force, port_scan, credential_stuffing

def run():

    brute_force()
    port_scan()
    credential_stuffing()

    env = DeceptionEnv()

    env.reset()

    total_reward = 0

    _, r, _, _ = env.step("detect_attack")
    total_reward += r

    _, r, _, _ = env.step("deploy_honeypot")
    total_reward += r

    _, r, _, _ = env.step("block_ip")
    total_reward += r

    return total_reward
