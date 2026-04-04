from env.env import DeceptionEnv

def run():

    env = DeceptionEnv()

    env.reset()

    state, reward, done, _ = env.step("deploy_honeypot")

    return reward
