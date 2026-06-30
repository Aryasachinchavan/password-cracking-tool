# 🔐 Password Cracking Tool (Beginner Cybersecurity Project)

A simple password-cracking simulation tool built to demonstrate core ethical hacking concepts, including brute-force and dictionary-based attacks. This project is intended as a learning resource for those getting started with cybersecurity fundamentals.

> ⚠️ **Disclaimer:** This tool is built strictly for **educational purposes**. Do not use it against any system, account, or network without explicit, authorized permission. Unauthorized use may be illegal.

---

## 📌 Overview

Password cracking is a foundational topic in cybersecurity used to understand password strength, attack methodology, and defensive best practices. This project implements two common techniques in a simplified, beginner-friendly way:

- **Brute Force Attack** — systematically tries every possible character combination until the correct password is found.
- **Dictionary Attack** — tests passwords against a predefined wordlist of common or leaked passwords.

---

## ⚙️ Features

- 🔁 Brute force simulation with configurable character sets and length
- 📖 Dictionary attack support using a custom wordlist
- ⚡ Fast and lightweight password testing logic
- 🧑‍🎓 Clean, beginner-friendly Python code with comments
- 📊 Basic output showing attempts and time taken

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Dependencies:** None (standard library only) — *update this if your project uses external packages*

---

## 📂 Project Structure

```
password-cracking-tool/
├── Images/             # Screenshots/diagrams used in documentation
├── cracker.py          # Main script (brute force + dictionary attack logic)
├── hashes.txt          # Sample password hashes used for testing
├── wordlist.txt         # Wordlist used for dictionary attacks
├── requirements.txt     # Python dependencies
├── report.txt            # Output/results report generated after running the tool
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Installation
```bash
git clone https://github.com/<your-username>/password-cracking-tool.git
cd password-cracking-tool
pip install -r requirements.txt
```

### Usage
Run the tool:
```bash
python3 cracker.py
```

The script reads target hashes from `hashes.txt`, attempts to crack them using `wordlist.txt` (and/or brute force, depending on configuration), and writes results to `report.txt`.

> 📝 Add specifics here once finalized — for example, whether the script prompts for input, accepts command-line arguments (e.g. `--mode dictionary` or `--hash-file hashes.txt`), and what a sample run/output looks like.

---

## 🎯 Learning Objectives

This project is designed to help beginners understand:

- How brute force and dictionary attacks work conceptually
- Why password length and complexity matter
- The importance of strong, unique passwords and rate-limiting/lockout defenses
- Basic Python scripting for security-related tasks

---

## ⚠️ Disclaimer

This tool is provided **strictly for educational and ethical learning purposes**. The author does not condone or support any unauthorized or illegal use of this software. Always obtain explicit permission before testing any system's security.

---

## 👨‍💻 Author

**Arya Sachin Chavan**
Cybersecurity Enthusiast

---

## 📜 License

This project is licensed under the MIT License — feel free to use it for learning and modify it as needed. *(Add a LICENSE file if you'd like to formalize this.)*
