# Networks_Final_Project_AlanUrquieta
This project is a mini distributed computing system over a network using 3 Azure VMS.

📌 Project Overview

The system consists of:

1 Head Node

Runs head_controller.py

Sends tasks to workers

Collects results

Measures serial vs. distributed performance

2 Worker Nodes

Each runs worker_server.py

Listens on TCP port 5000

Receives tasks and returns computed results

The goal is to show how distributed computing can be implemented manually using sockets, demonstrating fundamental networking concepts such as TCP communication, message passing, IP addressing, and parallelization.

🖥 Network Setup

All VMs were deployed on Azure:

Role	Private IP	Port Used
Head Node	10.0.0.10	Connects to workers
Worker 1	10.0.0.11	TCP 5000
Worker 2	10.0.0.12	TCP 5000

Azure automatically handles routing inside the Virtual Network (VNet).

📂 File Structure
/cluster_project
│
├── head_controller.py   # Sends tasks, collects results
├── worker_server.py     # Worker server listening on TCP port 5000
└── README.md

⚙️ Requirements

Python 3.x (Ubuntu Server 22.04)

Azure Virtual Machines (free-tier acceptable)

All VMs must be in the same VNet + subnet

Recommended: port 5000 open internally in your VNet

No external libraries are required — only Python’s built-in socket, json, and threading.

🚀 How to Run the Workers

On worker-1 and worker-2, run:

python3 worker_server.py


You should see:

[WORKER] Listening on 0.0.0.0:5000


Leave these terminals running.

🚀 How to Run the Head Node

On the head node, run:

python3 head_controller.py


You will see two parts:

1. Serial run (single machine)

Processes tasks one-by-one → slow.

2. Distributed run

Sends tasks to workers in parallel using threading → significantly faster.

Sample output:

== Serial run (single machine) ==
Serial time: ~10 seconds

== Distributed run (2 workers) ==
Distributed time: ~5 seconds

📡 Communication Flow

Head node connects to workers via TCP (worker_ip:5000).

Sends JSON tasks such as:

{ "n": 6 }


Worker computes n^2 (with simulated delay).

Worker returns:

{ "n": 6, "result": 36 }


Head aggregates and prints results.

📈 Performance Comparison
Mode	Total Tasks	Time
Serial (1 machine)	10 tasks	~10 seconds
Distributed (2 workers)	10 tasks	~5 seconds

This demonstrates real performance gain due to parallel task execution across multiple VMs.
