Automated Routing Protocol Validation Framework is a Python-based automation platform designed to validate Layer 2 and Layer 3 routing behavior in virtualized Linux environments.

The framework simulates multi-node router topologies using Linux network namespaces and automates:

Route injection

Convergence validation

Routing table verification

It reflects real-world routing software validation workflows used in service provider and distributed network environments, enabling scalable, repeatable, and CI/CD-compatible regression testing.

🎯 Objectives

Simulate virtual router topologies in isolated Linux namespaces

Automate route injection and propagation validation

Verify routing table correctness and convergence behavior

Support regression testing of L2/L3 protocol workflows

Enable CI/CD integration for automated qualification

✨ Key Features

Multi-node virtual router simulation

Validation of routing behavior (OSPF, BGP, IS-IS, TCP/IP concepts)

Automated route injection and verification

Convergence validation using timeout-based checks

Failure scenario simulation (link down, route withdrawal)

Modular and extensible architecture

🏗 Architecture
Virtual Routers (Linux Namespaces)
        ↓
Interface Configuration
        ↓
Route Injection
        ↓
Routing Table Validation
        ↓
Structured Test Result Output


Each virtual router operates in an isolated namespace, enabling realistic simulation of distributed routing environments.

🛠 Tech Stack

Python

Linux Network Namespaces

IP Route Utilities

Bash Integration

CI/CD Compatible Execution

⚙ Installation
Prerequisites

Linux (Ubuntu recommended)

Python 3.8+

Root privileges (required for namespace creation)

Clone Repository
git clone https://github.com/kaustubh-5016/Automated-Routing-Protocol-Validation-Framework.git
cd Automated-Routing-Protocol-Validation-Framework

Install Dependencies
pip install -r requirements.txt

▶ Usage

Run the framework:

sudo python3 main.py

Example Output
Starting Routing Validation Framework...
Route validated successfully

🧪 Example Test Workflow

Create virtual routers

Configure interfaces

Inject route

Validate route presence

Log results

🔮 Future Enhancements

Integration with FRRouting for dynamic OSPF/BGP testing

Traffic generator integration

JSON/HTML test reporting

Jenkins pipeline automation

Scalability benchmarking

📚 Learning Outcomes

This project demonstrates:

Routing protocol fundamentals

Linux networking internals

Automation testing framework design

Distributed systems validation concepts

CI/CD-ready architecture

📄 License

This project is developed for educational and research purposes.
