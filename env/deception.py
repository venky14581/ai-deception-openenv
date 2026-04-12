import requests

SERVER = "http://127.0.0.1:7860"


def deploy_honeypot():

    try:
        requests.post(f"{SERVER}/deploy_honeypot")
    except Exception:
        pass

    return {
        "action": "honeypot",
        "status": "deployed"
    }


def fake_database():

    try:
        requests.post(f"{SERVER}/fake_database")
    except Exception:
        pass

    return {
        "action": "fake_db",
        "status": "active"
    }


def block_attacker(ip):

    try:
        requests.post(
            f"{SERVER}/block",
            json={"ip": ip}
        )
    except Exception:
        pass

    return {
        "action": "block",
        "ip": ip
    }