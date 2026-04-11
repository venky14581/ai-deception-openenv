import requests
from env.deception import deploy_honeypot, fake_database, block_attacker
from models import Observation, Reward

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

        return Observation(**self._state)

    def step(self, action):

        reward = 0.0
        self.current_step += 1

        logs = requests.get(f"{SERVER}/logs").json()

        failed_logins = logs.get("failed_logins", 0)
        requests_log = logs.get("requests", [])

        # Detect brute force
        if action == "detect_attack":
            if failed_logins > 3:
                reward += 0.15
            else:
                reward -= 0.05

        # Detect port scan
        if action == "detect_attack":
            for r in requests_log:
                if isinstance(r, dict) and r.get("type") == "port_scan":
                    reward += 0.15
                    break

        # Detect SQL injection
        if action == "detect_attack":
            for r in requests_log:
                if isinstance(r, dict) and r.get("type") == "sql_injection":
                    reward += 0.15
                    break

        # Detect directory traversal
        if action == "detect_attack":
            for r in requests_log:
                if isinstance(r, dict) and r.get("type") == "directory_traversal":
                    reward += 0.15
                    break

        # Deploy honeypot
        elif action == "deploy_honeypot":
            deploy_honeypot()
            reward += 0.30

        # Fake database
        elif action == "fake_database":
            fake_database()
            reward += 0.20

        # Block attacker (multi attacker support)
        elif action == "block_ip":
            if logs.get("suspicious_ips"):
                ip = logs["suspicious_ips"][-1]   # latest attacker
                block_attacker(ip)
                reward += 0.50
                self.done = True

        # Episode boundary
        if self.current_step >= self.max_steps:
            self.done = True

        # Clamp reward
        reward = min(max(reward, 0.0), 1.0)

        self._state = logs

        observation = Observation(**self._state)
        reward_obj = Reward(reward=reward, done=self.done)

        return observation, reward_obj.reward, reward_obj.done, {}

    def state(self):
        return Observation(**self._state)

    def action_space(self):
        return [
            "detect_attack",
            "deploy_honeypot",
            "fake_database",
            "block_ip"
        ]