from flask import Flask, request, jsonify
import time
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

logs = {
    "failed_logins": 0,
    "port_scans": 0,
    "suspicious_ips": [],
    "requests": []
}

# ---------------- Login Attack ----------------

@app.route("/login", methods=["POST"])
def login():
    ip = request.remote_addr
    username = request.form.get("username")
    password = request.form.get("password")

    logs["requests"].append({
        "ip": ip,
        "type": "login_attempt",
        "username": username,
        "time": time.time()
    })

    if password == "admin123":
        return jsonify({"status": "success"})
    else:
        logs["failed_logins"] += 1

        if ip not in logs["suspicious_ips"]:
            logs["suspicious_ips"].append(ip)

        return jsonify({"status": "failed"})


# ---------------- Port Scan ----------------

@app.route("/scan", methods=["GET"])
def scan():
    ip = request.remote_addr

    logs["port_scans"] += 1

    logs["requests"].append({
        "ip": ip,
        "type": "port_scan",
        "time": time.time()
    })

    if ip not in logs["suspicious_ips"]:
        logs["suspicious_ips"].append(ip)

    return jsonify({"status": "scan detected"})


# ---------------- SQL Injection Attack ----------------

@app.route("/sql")
def sql():
    ip = request.remote_addr

    logs["requests"].append({
        "ip": ip,
        "type": "sql_injection",
        "time": time.time()
    })

    if ip not in logs["suspicious_ips"]:
        logs["suspicious_ips"].append(ip)

    return jsonify({"status": "sql injection detected"})


# ---------------- Directory Traversal ----------------

@app.route("/download")
def download():
    ip = request.remote_addr

    logs["requests"].append({
        "ip": ip,
        "type": "directory_traversal",
        "time": time.time()
    })

    if ip not in logs["suspicious_ips"]:
        logs["suspicious_ips"].append(ip)

    return jsonify({"status": "directory traversal attempt"})


# Common scan endpoints

@app.route("/admin")
def admin():
    logs["port_scans"] += 1
    return "Forbidden", 403


@app.route("/config")
def config():
    logs["port_scans"] += 1
    return "Forbidden", 403


@app.route("/backup")
def backup():
    logs["port_scans"] += 1
    return "Forbidden", 403


# ---------------- Logs ----------------

@app.route("/logs", methods=["GET"])
def get_logs():
    return jsonify(logs)


# ---------------- State API ----------------

@app.route("/state")
def state():
    return jsonify({
        "failed_logins": logs["failed_logins"],
        "port_scans": logs["port_scans"],
        "suspicious_ips": logs["suspicious_ips"],
        "total_requests": len(logs["requests"]),
        "attack_types": [r["type"] for r in logs["requests"]]
    })


# ---------------- Reset API ----------------

@app.route("/reset", methods=["GET", "POST"])
def reset():
    global logs

    logs = {
        "failed_logins": 0,
        "port_scans": 0,
        "suspicious_ips": [],
        "requests": []
    }

    return jsonify({
        "status": "reset",
        "success": True
    }), 200


# ---------------- Step API ----------------

@app.route("/step", methods=["GET", "POST"])
def step():

    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        action = data.get("action", None)
    else:
        action = request.args.get("action")

    reward = 0.0
    done = False

    if action == "detect_bruteforce":
        if logs["failed_logins"] > 3:
            reward = 0.4

    elif action == "detect_portscan":
        if logs["port_scans"] > 0:
            reward = 0.3

    elif action == "mitigate_attack":
        if len(logs["suspicious_ips"]) > 0:
            reward = 1.0
            done = True

    return jsonify({
        "state": logs,
        "reward": reward,
        "done": done,
        "info": {}
    })


# ---------------- Health Check ----------------

@app.route("/health")
def health():
    return jsonify({"status": "ok"})


# ---------------- Status ----------------

@app.route("/status")
def status():
    return jsonify({
        "environment": "AI Cyber Deception",
        "attacks": [
            "brute_force",
            "port_scan",
            "credential_stuffing",
            "sql_injection",
            "directory_traversal"
        ],
        "status": "running"
    })


# ---------------- Home ----------------

@app.route("/")
def home():
    return "AI Cyber Deception Server Running"


# ---------------- Run Server ----------------

def run_server():
    app.run(
        host="0.0.0.0",
        port=7860,
        debug=False,
        use_reloader=False
    )
