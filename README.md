# Networks_Final_Project_AlanUrquieta
This project is a mini distributed computing system over a network using 3 Azure VMS.

# Distributed Computing with Python Sockets on Azure Virtual Machines

This project demonstrates a lightweight distributed computing system using three Azure Virtual Machines connected inside the same virtual network. One VM acts as the **head node**, and two VMs act as **worker nodes**. The head node sends tasks to workers over TCP sockets, workers compute results, and the head aggregates the results.

---

# 📡 1. Azure Setup

## 1.1 Create a Resource Group
- Azure Portal → Resource groups → Create
- Name: `cluster-rg`
- Region: (e.g., Central US)

## 1.2 Create a Virtual Network (VNet)
- Name: `cluster-vnet`
- Address space: `10.0.0.0/16`
- Subnet:
  - Name: `cluster-subnet`
  - Range: `10.0.0.0/24`

## 1.3 Create the Virtual Machines
Create **three VMs**:

| VM Name       | Role        | Private IP   | Public IP |
|---------------|-------------|--------------|-----------|
| project-head  | Head Node   | 10.0.0.10    | Yes       |
| worker-1      | Worker Node | 10.0.0.11    | No        |
| worker-2      | Worker Node | 10.0.0.12    | No        |

### VM Settings:
- Image: Ubuntu Server 22.04 LTS
- Size: Free/cheap tier OK (B1s/B1ms)
- Authentication: SSH key
- VNet: `cluster-vnet`
- Subnet: `cluster-subnet`

### Set Private IP (after VM creation)
Azure → VM → **Networking** → NIC → IP configurations → Set to **Static** and assign the correct private IP.

---

# 🧰 2. Connect to VMs via VS Code

1. Install VS Code extension: **Remote - SSH**
2. Add this to your SSH config:
Host project-head
HostName <HEAD_PUBLIC_IP>
User alan
IdentityFile ~/.ssh/<your-key>.pem
3. Connect using:SSH from the head node to workers:
   - ssh alan@10.0.0.11
   - ssh alan@10.0.0.12

---

# 🐍 3. Install Python on Each VM

Run on *all three* VMs:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

---

# 4. Worker Server Setup

1. Create the server script:
```bash
mkdir ~/cluster_project
cd ~/cluster_project
nano worker_server.py
```
2. Paste worker_server.py
3. Create Controller Script
```bash
mkdir ~/cluster_project
cd ~/cluster_project
nano head_controller.py
```
4. Paste head_controller.py

---

# 5. Running the Distributed System

1. On worker-1 and worker-2:
```bash
python3 worker_server.py
```
2. On the head node:
```bash
python3 head_controller.py
```
Expected output:

- Serial time: ~10 seconds

- Distributed time: ~5 seconds

- Workers process tasks in parallel
