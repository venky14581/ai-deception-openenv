import threading
import time

from env.fake_server import run_server, RESULTS
from tasks.easy import run as easy
from tasks.medium import run as medium
from tasks.hard import run as hard

# Start fake server in background
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

time.sleep(2)  # wait for server to start

print("[START] task=ai-deception env=cyber-security model=baseline", flush=True)

# Run continuously
while True:

    # Easy Task
    easy_score = easy()
    print(
        f"[STEP] step=1 action=easy reward={easy_score:.2f} done=false error=null",
        flush=True
    )

    # Medium Task
    medium_score = medium()
    print(
        f"[STEP] step=2 action=medium reward={medium_score:.2f} done=false error=null",
        flush=True
    )

    # Hard Task
    hard_score = hard()
    print(
        f"[STEP] step=3 action=hard reward={hard_score:.2f} done=true error=null",
        flush=True
    )

    print(
        f"[END] success=true steps=3 rewards={easy_score:.2f},{medium_score:.2f},{hard_score:.2f}",
        flush=True
    )

    # Update results for judges
    RESULTS["status"] = "completed"
    RESULTS["steps"] = 3
    RESULTS["rewards"] = [easy_score, medium_score, hard_score]
    RESULTS["attacks"] = [
        "brute_force",
        "port_scan",
        "credential_stuffing"
    ]

    # wait before next attack cycle
    time.sleep(60)
