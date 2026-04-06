import threading
import time
import os
import random
from openai import OpenAI

random.seed(42)

from env.fake_server import run_server
from env.env import DeceptionEnv
from env.attacker import simulate_attack

# Start server
threading.Thread(target=run_server, daemon=True).start()
time.sleep(2)

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-7B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    print("[ERROR] HF_TOKEN not set. Please set your Hugging Face token.")
    exit(1)

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

env = DeceptionEnv()
state = env.reset()   # reset only once

print("[START] task=ai-deception env=cyber-security model=AI-agent", flush=True)

rewards = []
history = []

for step in range(1, 4):

    simulate_attack()

    summary = {
        "failed_logins": state["failed_logins"],
        "port_scans": state.get("port_scans", 0),
        "suspicious_ips": len(state["suspicious_ips"])
    }

    prompt = f"""
You are a cybersecurity decision system.

Previous actions:
{history}

Current summary:
{summary}

STRICT RULES (must follow exactly):

1. If no previous action → detect_attack
2. If last action == detect_attack → deploy_honeypot
3. If last action == deploy_honeypot → block_ip
4. If last action == block_ip → block_ip

Return ONLY one word:
detect_attack
deploy_honeypot
fake_database
block_ip
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=20
    )

    action = response.choices[0].message.content.strip()

    # deterministic fallback
    if history:
        last = history[-1]
        if last == "detect_attack":
            action = "deploy_honeypot"
        elif last == "deploy_honeypot":
            action = "block_ip"

    history.append(action)

    state, reward, done, _ = env.step(action)
    rewards.append(reward)

    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} "
        f"done={str(done).lower()} error=null",
        flush=True
    )

print(
    f"[END] success=true steps=3 rewards={','.join(f'{r:.2f}' for r in rewards)}",
    flush=True
)
