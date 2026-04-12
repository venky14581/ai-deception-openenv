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
        self.detected = False
        self.deployed = False

    def reset(self):

        requests.post(f"{SERVER}/reset")

        self.done = False
        self.current_step = 0
        self.detected = False
        self.deployed = False

        logs = requests.get(f"{SERVER}/logs").json()
        self._state = logs

        return Observation(**self._state)

    def step(self, action):

        reward = 0.0
        self.current_step += 1

        logs = requests.get(f"{SERVER}/logs").json()

        failed_logins = logs.get("failed_logins", 0)
        requests_log = logs.get("requests", [])

        # ---------------- Detect Attack ----------------
        if action == "detect_attack":

            detected_any = False

            if failed_logins > 3:
                reward += 0.15
                detected_any = True

            for r in requests_log:
                if isinstance(r, dict) and r.get("type") == "port_scan":
                    reward += 0.15
                    detected_any = True
                    break

            for r in requests_log:
                if isinstance(r, dict) and r.get("type") == "sql_injection":
                    reward += 0.15
                    detected_any = True
                    break

            for r in requests_log:
                if isinstance(r, dict) and r.get("type") == "directory_traversal":
                    reward += 0.15
                    detected_any = True
                    break

            if detected_any:
                self.detected = True
            else:
                reward -= 0.10

        # ---------------- Deploy Honeypot ----------------
        elif action == "deploy_honeypot":

            deploy_honeypot()
            reward += 0.30
            self.deployed = True

        # ---------------- Fake Database ----------------
        elif action == "fake_database":

            fake_database()
            reward += 0.20
            self.deployed = True

        # ---------------- Block Attacker ----------------
        elif action == "block_ip":

            if (
                logs.get("suspicious_ips")
                and self.detected
                and self.deployed
                and self.current_step >= 3
            ):

                ip = logs["suspicious_ips"][-1]
                block_attacker(ip)

                reward += 0.70
                self.done = True

            else:
                reward -= 0.10

        # ---------------- Episode Boundary ----------------
        if self.current_step >= self.max_steps:
            self.done = True

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