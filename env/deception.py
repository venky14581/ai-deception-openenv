def deploy_honeypot():

    return {
        "action": "honeypot",
        "status": "deployed"
    }


def fake_database():

    return {
        "action": "fake_db",
        "status": "active"
    }


def block_attacker(ip):

    return {
        "action": "block",
        "ip": ip
    }
