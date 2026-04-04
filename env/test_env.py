from env import DeceptionEnv

env = DeceptionEnv()

state = env.reset()

print("Initial State:", state)

state, reward, done, _ = env.step("deploy_honeypot")

print("After step:", state)
print("Reward:", reward)
