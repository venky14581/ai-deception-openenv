import requests
from env.deception import deploy_honeypot, fake_database, block_attacker

SERVER = "http://127.0.0.1:7860"


class DeceptionEnv:

    def _init_(self):
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
        requests_log = logs["requests"]

        # Detect brute force
        if action == "detect_attack":
            if failed_logins > 3:
                reward += 0.2
            else:
                reward -= 0.1

        # Detect port scan
        if action == "detect_attack":
            for r in requests_log:
                if isinstance(r, dict) and r.get("type") == "port_scan":
                    reward += 0.2
                    break

        # Deploy honeypot
        if action == "deploy_honeypot":
            deploy_honeypot()
            reward += 0.3

        # Fake database
        if action == "fake_database":
            fake_database()
            reward += 0.2

        # Block attacker
        if action == "block_ip":
            if logs["suspicious_ips"]:
                ip = logs["suspicious_ips"][0]
                block_attacker(ip)
                reward += 0.5
                self.done = True

        self.state = logs

        return self.state, reward, self.done, {}

    def state(self):
        return self.state

    def action_space(self):
        return [
            "detect_attack",
            "deploy_honeypot",
            "fake_database",
            "block_ip"
        ]
