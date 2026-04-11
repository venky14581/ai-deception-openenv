import threading
import time
import os
import random
import traceback
from openai import OpenAI

random.seed(42)
from env.fake_server import run_server
threading.Thread(target=run_server, daemon=True).start()
time.sleep(2)
from env.env import DeceptionEnv
from env.attacker import simulate_attack

# Import graders
from tasks.easy.grader import grade as easy_grade
from tasks.medium.grader import grade as medium_grade
from tasks.hard.grader import grade as hard_grade


API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-7B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN")


def choose_action(client, state):

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": """You are a cybersecurity deception agent.

Choose the best action based on the state:

- detect_attack → when attacks suspected
- deploy_honeypot → after attack detected
- fake_database → when attacker probing system
- block_ip → when attacker confirmed

Return only one action from:
detect_attack, deploy_honeypot, fake_database, block_ip"""
                },
                {
                    "role": "user",
                    "content": f"Current state: {state}"
                }
            ],
            max_tokens=10,
            temperature=0.4
        )

        action = response.choices[0].message.content.strip()

    except Exception:
        action = "detect_attack"

    return action


def run_task(task_name):

    try:

        client = OpenAI(
            base_url=API_BASE_URL,
            api_key=HF_TOKEN
        )

        env = DeceptionEnv()
        state = env.reset()

        print(
            f"[START] task={task_name} env=ai-deception-openenv model={MODEL_NAME}",
            flush=True
        )

        rewards = []
        done = False

        for step in range(1, 4):

            try:
                simulate_attack()
            except Exception:
                pass

            try:
                state = env.state()
            except Exception:
                pass

            # AI chooses action
            action = choose_action(client, state)

            # exploration (30%)
            if random.random() < 0.3:
                action = random.choice(env.action_space())

            # fallback
            if action not in env.action_space():
                action = "detect_attack"

            state, reward, done, _ = env.step(action)

            reward = min(max(reward, 0.05), 0.95)
            rewards.append(reward)

            print(
                f"[STEP] step={step} action={action} reward={reward:.2f} "
                f"done={str(done).lower()} error=null",
                flush=True
            )

            if done:
                break

        steps = len(rewards)

        # grading
        if task_name == "easy":
            score = easy_grade(rewards)
        elif task_name == "medium":
            score = medium_grade(rewards)
        else:
            score = hard_grade(rewards)

        success = score >= 0.5

        print(
            f"[END] success={str(success).lower()} steps={steps} "
            f"score={score:.2f} rewards={','.join(f'{r:.2f}' for r in rewards)}",
            flush=True
        )

    except Exception:
        traceback.print_exc()
        print(
            "[END] success=false steps=0 score=0.10 rewards=",
            flush=True
        )


run_task("easy")
run_task("medium")
run_task("hard")

# Keep alive briefly
time.sleep(180)
