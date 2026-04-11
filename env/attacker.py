import requests
import time

TARGET = "http://127.0.0.1:7860"


def brute_force():
    for i in range(5):
        requests.post(
            f"{TARGET}/login",
            data={
                "username": "admin",
                "password": "wrong"
            }
        )
        time.sleep(0.5)


def port_scan():
    endpoints = ["/admin", "/config", "/backup"]

    for ep in endpoints:
        requests.get(f"{TARGET}{ep}")


def credential_stuffing():
    passwords = ["admin", "password", "123456"]

    for p in passwords:
        requests.post(
            f"{TARGET}/login",
            data={"username": "admin", "password": p}
        )


# ---------------- SQL Injection ----------------

def sql_injection():
    requests.get(f"{TARGET}/sql")


# ---------------- Directory Traversal ----------------

def directory_traversal():
    requests.get(f"{TARGET}/download")


# ---------------- Full Attack Simulation ----------------

def simulate_attack():
    brute_force()
    port_scan()
    credential_stuffing()
    sql_injection()
    directory_traversal()
