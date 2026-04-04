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


if __name__ == "__main__":
    brute_force()
