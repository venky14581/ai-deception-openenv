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

AI Cyber Deception OpenEnv is a real-world cybersecurity simulation environment where an AI agent learns to detect attackers and deploy deception strategies such as honeypots.

## Features

- Fake server simulation
- Attacker simulation
- AI deception environment
- Reward-based learning
- Multiple difficulty tasks

## Tasks

### Easy
Detect brute force attack

### Medium
Deploy honeypot

### Hard
Full incident response (detect, deceive, block)

## Actions

- detect_attack
- deploy_honeypot
- block_ip

## Reward System

- Detect attack → +0.5
- Deploy honeypot → +0.3
- Block attacker → +0.2

## Project Structure
ai_deception_env/
├── env/
├── tasks/
├── inference.py
├── openenv.yaml
├── Dockerfile


## Run

### Local


python inference.py


### Docker


docker build -t ai-deception-env .
docker run ai-deception-env


## Example Output


[START]
[STEP]
[STEP]
[STEP]
[END]


## Requirements

- Python 3.10
- Flask
- Requests

## Author

Bytecore team
