---
title: AI Deception OpenEnv
emoji: 🛡️
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
---
# AI Cyber Deception OpenEnv

## Overview

This project implements a real-world AI Cyber Deception environment where an AI agent learns to detect and mitigate cyber attacks such as brute force, port scanning, and credential stuffing.

The environment follows the OpenEnv specification and supports step(), reset(), and state() APIs.

---

## Real-world Task

Simulate cybersecurity defense in a production-like environment:

- Detect brute force attacks
- Detect port scanning
- Deploy deception mechanisms
- Block malicious IPs

---

## Action Space

The agent can perform:

- detect_attack
- deploy_honeypot
- fake_database
- block_ip

---

## Observation Space

Environment returns:

- failed_logins
- port_scans
- suspicious_ips
- request logs

---

## Tasks

### Easy Task
Detect brute force attack

### Medium Task
Deploy honeypot after detecting attack

### Hard Task
Block malicious attacker

---

## Reward Function

| Action | Reward |
|--------|--------|
| detect_attack | 0.4 |
| deploy_honeypot | 0.2 |
| block_ip | 0.3 |

---

## APIs

- `/reset`
- `/step`
- `/state`
- `/logs`
- `/status`

---

## Setup

### Run locally

```bash
pip install -r requirements.txt
python inference.py

Docker
docker build -t ai-deception .
docker run ai-deception

Hugging Face Deployment
https://bytecore1-ai-deception-openenv.hf.space/
https://bytecore1-ai-deception-openenv.hf.space/state
https://bytecore1-ai-deception-openenv.hf.space/status
https://bytecore1-ai-deception-openenv.hf.space/logs

Baseline Results

Example:

[START]
[STEP]
[STEP]
[STEP]
[END]
Architecture

Attacker → Fake Server → AI Agent → Defense Actions → Reward
