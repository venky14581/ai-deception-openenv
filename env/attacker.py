import requests
import requests
import time

TARGET = "http://127.0.0.1:5000"


def brute_force():

    print("Starting brute force attack...")

    for i in range(5):
        response = requests.post(
            f"{TARGET}/login",
            data={
                "username": "admin",
                "password": "wrong"
            }
        )

        print("Attempt:", i+1, response.json())

        time.sleep(1)


def port_scan():

    print("Starting port scan...")

    endpoints = ["/admin", "/config", "/backup"]

    for ep in endpoints:
        response = requests.get(f"{TARGET}{ep}")
        print("Scan:", ep, response.status_code)


def credential_stuffing():

    print("Starting credential stuffing...")

    passwords = ["admin", "password", "123456"]

    for p in passwords:
        response = requests.post(
            f"{TARGET}/login",
            data={"username": "admin", "password": p}
        )

        print("Attempt:", p, response.json())


if __name__ == "__main__":
    brute_force()
    port_scan()
    credential_stuffing()
