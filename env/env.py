import requests
from env.deception import deploy_honeypot, fake_database, block_attacker

SERVER = "http://127.0.0.1:7860"


class DeceptionEnv:

    def __init__(self):
        self._state = {}
        self.done = False
        self.max_steps = 5
        self.current_step = 0

    def reset(self):
        self.done = False
        self.current_step = 0

        logs = requests.get(f"{SERVER}/logs").json()
        self._state = logs

        return self._state

    def step(self, action):

        reward = 0.0
        self.current_step += 1

        logs = requests.get(f"{SERVER}/logs").json()

        failed_logins = logs.get("failed_logins", 0)
        requests_log = logs.get("requests", [])

        # Detect brute force
        if action == "detect_attack":
            if failed_logins > 3:
                reward += 0.2
            else:
                reward -= 0.05

        # Detect port scan
        if action == "detect_attack":
            for r in requests_log:
                if isinstance(r, dict) and r.get("type") == "port_scan":
                    reward += 0.2
                    break

        # Deploy honeypot
        elif action == "deploy_honeypot":
            deploy_honeypot()
            reward += 0.3

        # Fake database
        elif action == "fake_database":
            fake_database()
            reward += 0.2

        # Block attacker
        elif action == "block_ip":
            if logs.get("suspicious_ips"):
                ip = logs["suspicious_ips"][0]
                block_attacker(ip)
                reward += 0.5
                self.done = True

        # Episode boundary
        if self.current_step >= self.max_steps:
            self.done = True

        self._state = logs

        return self._state, reward, self.done, {}

    def state(self):
        return self._state

    def action_space(self):
        return [
            "detect_attack",
            "deploy_honeypot",
            "fake_database",
            "block_ip"
        ]
