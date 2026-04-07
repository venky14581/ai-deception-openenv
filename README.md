---
title: AI Deception OpenEnv
emoji: 🛡️
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
---

# 🛡️ AI Cyber Deception OpenEnv

## Overview

AI Cyber Deception OpenEnv is a real-world cybersecurity simulation environment where an AI agent learns to detect, deceive, and mitigate cyber attacks.

This environment simulates production-like cybersecurity defense scenarios including brute force attacks, port scanning, and credential stuffing.

The environment follows the **OpenEnv specification** and supports:

- `reset()`
- `step()`
- `state()`

---

## 🎯 Real-World Task

Simulate cybersecurity defense in a production-like environment:

- Detect brute force attacks
- Detect port scanning
- Deploy deception mechanisms
- Block malicious attackers

---

## ⚙️ Action Space

The AI agent can perform the following actions:

- `detect_attack`
- `deploy_honeypot`
- `fake_database`
- `block_ip`

---

## 👁️ Observation Space

Environment returns structured observation:

- `failed_logins`
- `port_scans`
- `suspicious_ips`
- `request_logs`

---

## 🧠 Tasks

### Easy Task
Detect brute force attack

### Medium Task
Detect attack and deploy honeypot

### Hard Task
Detect, deceive, and block attacker

---

## 🏆 Reward Function

| Action | Reward |
|--------|--------|
| detect_attack | 0.20 |
| deploy_honeypot | 0.30 |
| fake_database | 0.20 |
| block_ip | 0.50 |

Reward range normalized between **0.0 – 1.0**

---

## 🌐 API Endpoints

Available endpoints:

- `/reset`
- `/step`
- `/state`
- `/logs`
- `/status`

Example:


POST /reset
POST /step
GET /state


---

## 🚀 Run Locally

Install dependencies:

```bash
pip install -r requirements.txt

Run inference:

python inference.py

🐳 Docker

Build:

docker build -t ai-deception .

Run:

docker run -p 7860:7860 ai-deception

🤗 Hugging Face Deployment
Live Space:

https://bytecore1-ai-deception-openenv.hf.space/

Endpoints:

https://bytecore1-ai-deception-openenv.hf.space/reset
https://bytecore1-ai-deception-openenv.hf.space/state
https://bytecore1-ai-deception-openenv.hf.space/status
https://bytecore1-ai-deception-openenv.hf.space/logs

📊 Baseline Results
Example run:

[START] task=ai-deception env=cyber-security model=Qwen
[STEP] step=1 action=detect_attack reward=0.20 done=false error=null
[STEP] step=2 action=deploy_honeypot reward=0.30 done=false error=null
[STEP] step=3 action=block_ip reward=0.50 done=true error=null
[END] success=true steps=3 score=1.00 rewards=0.20,0.30,0.50


🏗️ Architecture
Attacker
   ↓
Fake Server
   ↓
AI Agent (Inference)
   ↓
Defense Actions
   ↓
Reward

📦 Project Structure

ai-deception-openenv/
│
├── env/
│   ├── __init__.py
│   ├── attacker.py
│   ├── deception.py
│   ├── env.py
│   ├── fake_server.py
│   ├── test_env.py
│   └── test_server.py
│
├── tasks/
│   ├── __init__.py
│   ├── easy.py
│   ├── medium.py
│   ├── hard.py
│   └── test_tasks.py
│
├── inference.py
├── app.py
├── models.py
├── openenv.yaml
├── Dockerfile
├── requirements.txt
├── README.md
├── .gitignore
└── .gitattributes


✅ OpenEnv Compliance
reset() implemented
step() implemented
state() implemented
Docker support
Structured logs
Multiple tasks
Reward normalization

👨‍💻 Use Case
This environment can be used for:

Cybersecurity research
Reinforcement learning
AI defense strategy training
Red team vs blue team simulations

🛡️ AI Cyber Deception
This project demonstrates how AI can:

Detect attackers
Deploy deception
Block malicious actors
Learn defensive strategies


License

MIT License
