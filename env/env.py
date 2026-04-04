import requests
from env.deception import deploy_honeypot, fake_database, block_attacker

SERVER = "http://127.0.0.1:5000"

class DeceptionEnv:

    def __init__(self):
        self.state = {}
        self.done = False

    def reset(self):

        self.done = False

        logs = requests.get(f"{SERVER}/logs").json()

        self.state = logs

        return self.state


    def step(self, action):

        reward = 0

        logs = requests.get(f"{SERVER}/logs").json()

        failed_logins = logs["failed_logins"]

        if action == "detect_attack":
            if failed_logins > 3:
                reward += 0.5

        if action == "deploy_honeypot":
            deploy_honeypot()
            reward += 0.3

        if action == "fake_database":
            fake_database()
            reward += 0.2

        if action == "block_ip":
            if logs["suspicious_ips"]:
                ip = logs["suspicious_ips"][0]
                block_attacker(ip)
                reward += 0.2
                self.done = True

        self.state = logs

        return self.state, reward, self.done, {}
