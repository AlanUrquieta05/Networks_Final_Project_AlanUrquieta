import socket
import json
import time
import threading

# Worker private IPs
WORKERS = [
    ("10.0.0.11", 5000),  # worker-1
    ("10.0.0.12", 5000),  # worker-2
]

def send_task(worker_host, worker_port, n, results):
    """Send a single task (n) to a worker and save its reply in results."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((worker_host, worker_port))
            payload = json.dumps({"n": n}).encode("utf-8")
            s.sendall(payload)
            data = s.recv(1024)
        response = json.loads(data.decode("utf-8"))
        results.append(response)
        print(f"[HEAD] Got result from {worker_host}: {response}")
    except Exception as e:
        print(f"[HEAD] Error talking to {worker_host}: {e}")

def distributed_run(numbers):
    """Send numbers out to workers in parallel using threads."""
    threads = []
    results = []

    start = time.time()

    for i, n in enumerate(numbers):
        worker_host, worker_port = WORKERS[i % len(WORKERS)]
        t = threading.Thread(target=send_task,
                             args=(worker_host, worker_port, n, results))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.time()

    # Sort results by input n for nicer printing
    results.sort(key=lambda r: r["n"])

    print("\n[HEAD] Distributed results:")
    for r in results:
        print(f"  n={r['n']} -> {r['result']}")

    print(f"[HEAD] Distributed time: {end - start:.2f} seconds")

def serial_run(numbers):
    """Do the same computation on a single machine, no network."""
    start = time.time()
    results = []
    for n in numbers:
        time.sleep(1)  # simulate same work
        results.append({"n": n, "result": n * n})
    end = time.time()

    print("\n[HEAD] Serial results:")
    for r in results:
        print(f"  n={r['n']} -> {r['result']}")
    print(f"[HEAD] Serial time: {end - start:.2f} seconds")

def main():
    numbers = list(range(10))  # 10 tasks

    print("== Serial run (single machine) ==")
    serial_run(numbers)

    print("\n== Distributed run (2 workers over network) ==")
    distributed_run(numbers)

if __name__ == "__main__":
    main()
