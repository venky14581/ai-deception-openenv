from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Global logs
logs = {
    "failed_logins": 0,
    "suspicious_ips": [],
    "requests": []
}


@app.route("/login", methods=["POST"])
def login():

    ip = request.remote_addr
    username = request.form.get("username")
    password = request.form.get("password")

    logs["requests"].append({
        "ip": ip,
        "username": username,
        "time": time.time()
    })

    # Fake login check
    if password == "admin123":
        return jsonify({"status": "success"})

    else:
        logs["failed_logins"] += 1

        if ip not in logs["suspicious_ips"]:
            logs["suspicious_ips"].append(ip)

        return jsonify({"status": "failed"})


@app.route("/logs", methods=["GET"])
def get_logs():
    return jsonify(logs)


def run_server():
    app.run(port=5000)

@app.route("/")
def home():
    return "AI Cyber Deception Server Running"

@app.route("/admin")
def admin():
    logs["requests"].append({
        "type": "port_scan",
        "endpoint": "/admin",
        "time": time.time()
    })
    return "Forbidden", 403


@app.route("/config")
def config():
    logs["requests"].append({
        "type": "port_scan",
        "endpoint": "/config",
        "time": time.time()
    })
    return "Forbidden", 403


@app.route("/backup")
def backup():
    logs["requests"].append({
        "type": "port_scan",
        "endpoint": "/backup",
        "time": time.time()
    })
    return "Forbidden", 403
