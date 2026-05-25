[README_project2_encryption_decryption_tool.md](https://github.com/user-attachments/files/28209867/README_project2_encryption_decryption_tool.md)
# 🔒 Encryption & Decryption Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Terminal](https://img.shields.io/badge/Runs_In-Terminal-black?style=for-the-badge&logo=gnometerminal)
![No Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen?style=for-the-badge)
![DecodLabs](https://img.shields.io/badge/DecodLabs-Project_2-purple?style=for-the-badge)

A terminal-based **Encryption & Decryption Tool** built entirely with Python's built-in libraries. Encrypt any text message and decrypt it back — no pip installs required.

---

## 📌 Table of Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [How It Works](#how-it-works)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [License](#license)

---

## 📖 About

This is a **command-line tool** that lets users encrypt a plaintext message into an unreadable cipher and decrypt it back to the original text. The user provides a message and a key directly in the terminal. Built as a DecodLabs submission using only Python's standard library — no external packages needed.

---

## ✨ Features

- ✅ Runs entirely in the terminal — no browser or UI needed
- ✅ Zero external dependencies — only built-in Python
- ✅ Encrypt any text message using a key
- ✅ Decrypt any cipher text back to the original message
- ✅ Symmetric — same key used for both operations
- ✅ Handles letters, numbers, and special characters

---

## ⚙️ Requirements

- Python 3.x (no additional packages needed)

Check your Python version:
```bash
python --version
```

---

## ▶️ How to Run

1. **Clone or download the repository:**
   ```bash
   git clone https://github.com/milannai22a/Decodlabs_project-2.git
   cd Decodlabs_project-2
   ```

2. **Run the script:**
   ```bash
   python encryption_tool.py
   ```

3. **Follow the prompts** in the terminal — choose to encrypt or decrypt, then enter your text and key.

---

## ⚙️ How It Works

The tool uses a **symmetric cipher** — the same key is used to both encrypt and decrypt. When encrypting, each character in the message is transformed using the key. When decrypting, the same key reverses the transformation to recover the original message.

- **Encrypt:** `plaintext + key → cipher text`
- **Decrypt:** `cipher text + key → plaintext`

> ⚠️ The key must be the same for both operations. Using a different key during decryption will not return the original message.

---

## 🖥️ Sample Output

**Encryption:**
```
Choose operation:
1. Encrypt
2. Decrypt
Enter choice: 1

Enter message : Hello, DecodLabs!
Enter key     : mykey

Encrypted: (cipher output)
```

**Decryption:**
```
Choose operation:
1. Encrypt
2. Decrypt
Enter choice: 2

Enter cipher  : (cipher output from above)
Enter key     : mykey

Decrypted: Hello, DecodLabs!
```

---

## 📁 Project Structure

```
Decodlabs_project-2/
│
├── encryption_tool.py      # Main Python script
└── README.md               # Project documentation
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> Made with ❤️ by [milannai22a](https://github.com/milannai22a) | DecodLabs Submission
