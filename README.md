# 🧮 VLAN & Subnet Calculator (CLI Tool)

A Python CLI tool to help network engineers and QA testers quickly calculate subnet allocations based on host requirements and generate VLAN assignments.

Ideal for lab planning, network segmentation, or as a base for automation projects in networking roles.

---

## ✨ Features

- Automatically calculates optimal subnet sizes based on required hosts
- Assigns unique VLAN IDs
- Supports custom base network inputs (e.g., 192.168.0.0/16)
- Avoids overlapping subnets
- CLI interface – easy to use and expand

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.6+
- No external libraries needed (uses Python’s built-in `ipaddress` and `math` modules)

### 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/vlan-subnet-calculator.git
cd vlan-subnet-calculator

