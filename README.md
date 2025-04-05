
# 🧮 VLAN & Subnet Calculator (CLI Tool)

A Python CLI tool to help network engineers and QA testers quickly calculate subnet allocations based on host requirements and generate VLAN assignments.

This tool is ideal for lab planning, network segmentation, or as a base for automation projects in networking-focused QA roles.

---

## ✨ Features

- 🧠 Automatically calculates optimal subnet sizes based on required hosts
- 🔐 Assigns unique VLAN IDs
- 🗺️ Supports custom base network inputs (e.g., `192.168.0.0/16`)
- ⚙️ Avoids overlapping subnets
- 🖥️ CLI interface – lightweight, clean, and beginner-friendly

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.6 or higher
- No external libraries needed (uses built-in `ipaddress` and `math` modules)

---

### 📦 Installation

Clone the repository:

```bash
git clone git@github-shan:Susmitha2511/vlan-subnet-calculator.git
cd vlan-subnet-calculator
```

---

## 🛠️ Usage

Run the script from your terminal:

```bash
python vlan_subnet_calculator.py
```

Follow the prompts:

```
Enter base network (e.g., 192.168.0.0/16): 192.168.0.0/16
Enter number of VLANs you need: 3
Enter required hosts for VLAN 1: 50
Enter required hosts for VLAN 2: 200
Enter required hosts for VLAN 3: 30
```

---

## 📊 Sample Output

```
📊 VLAN & Subnet Allocation
========================================
VLAN 20: Needs 200 hosts → Assigned subnet: 192.168.0.0/24 (Usable: 254)
VLAN 10: Needs 50 hosts  → Assigned subnet: 192.168.1.0/26 (Usable: 62)
VLAN 30: Needs 30 hosts  → Assigned subnet: 192.168.1.64/27 (Usable: 30)
========================================
```

Subnets are assigned from the base network and sorted by host size to minimize fragmentation. All allocations avoid overlap.

---

## 📁 File Structure

```
vlan-subnet-calculator/
├── vlan_subnet_calculator.py   # Main CLI script
└── README.md                   # Project documentation
```

---

## 💡 Future Improvements

Here are some planned features and enhancements:

- [ ] Add a web interface using Flask or Streamlit
- [ ] Export output to CSV or JSON
- [ ] Add error handling for overlapping IP ranges
- [ ] Add visualization of subnet blocks on a chart
- [ ] Integrate unit tests and CI with GitHub Actions
- [ ] Auto-generate network diagrams (via Graphviz)

Contributions are welcome! Feel free to fork and open a pull request.

---

## 🧑‍💻 Author

**Susmitha**

- GitHub: [@Susmitha2511](https://github.com/Susmitha2511)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contributing

If you find this project useful or have suggestions for improvement, feel free to:

- ⭐ Star the repo
- 🐛 Open issues
- 🚀 Submit PRs

Thanks for checking out this project!

