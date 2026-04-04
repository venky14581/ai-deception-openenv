def deploy_honeypot():

    print("Honeypot deployed")

    return {
        "action": "honeypot",
        "status": "deployed"
    }


def fake_database():

    print("Fake database exposed")

    return {
        "action": "fake_db",
        "status": "active"
    }


def block_attacker(ip):

    print(f"Blocked attacker: {ip}")

    return {
        "action": "block",
        "ip": ip
    }
