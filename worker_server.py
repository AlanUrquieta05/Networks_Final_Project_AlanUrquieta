import socket
import json
import time

HOST = "0.0.0.0"  # listen on all interfaces
PORT = 5000       # you can change this if needed

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"[WORKER] Listening on {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()
            with conn:
                print(f"[WORKER] Connection from {addr}")
                data = conn.recv(1024)
                if not data:
                    continue

                try:
                    request = json.loads(data.decode("utf-8"))
                    n = request["n"]
                    # Simulate some work
                    time.sleep(1)
                    result = n * n
                    response = {
                        "n": n,
                        "result": result,
                    }
                    conn.sendall(json.dumps(response).encode("utf-8"))
                except Exception as e:
                    print(f"[WORKER] Error: {e}")

if __name__ == "__main__":
    main()