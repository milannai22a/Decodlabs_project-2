# 📘 Documentation — Encryption & Decryption Tool

> **Author:** [milannai22a](https://github.com/milannai22a)
> **Repository:** [Decodlabs_project-2](https://github.com/milannai22a/Decodlabs_project-2)
> **Type:** Command-Line Application
> **Language:** Python 3.x (built-in libraries only)
> **Submission:** DecodLabs — Project 2

---

## 📋 Table of Contents

1. [Project Overview](#1-project-overview)
2. [Objectives](#2-objectives)
3. [Technology Used](#3-technology-used)
4. [Project Structure](#4-project-structure)
5. [How to Run](#5-how-to-run)
6. [Program Flow](#6-program-flow)
7. [Encryption & Decryption Logic](#7-encryption--decryption-logic)
8. [Built-in Libraries Used](#8-built-in-libraries-used)
9. [Sample Terminal Output](#9-sample-terminal-output)
10. [Test Cases](#10-test-cases)
11. [Known Limitations](#11-known-limitations)
12. [Future Improvements](#12-future-improvements)

---

## 1. Project Overview

The **Encryption & Decryption Tool** is a terminal-based Python application that allows users to encrypt a plaintext message into an unreadable cipher and decrypt it back to the original text using a key. Everything runs in the terminal — no browser, no UI, no external libraries.

The user selects whether they want to encrypt or decrypt, enters their message and a key, and the result is printed directly in the terminal. This project uses **only Python's built-in standard library** — no pip installs required.

---

## 2. Objectives

- Accept user input (message and key) from the terminal
- Encrypt a plaintext message into cipher text using a key
- Decrypt a cipher text back to the original message using the same key
- Demonstrate Python string manipulation, `ord()`, `chr()`, and loop logic
- Use only built-in Python — no external packages needed

---

## 3. Technology Used

| Item | Detail |
|---|---|
| Language | Python 3.x |
| Interface | Terminal / Command Line |
| Libraries | Built-in only (`ord`, `chr`, string operations) |
| Dependencies | None — no `pip install` needed |
| Platform | Windows, macOS, Linux |

---

## 4. Project Structure

```
Decodlabs_project-2/
│
├── encryption_tool.py      # Main script — all logic lives here
└── README.md               # Project readme
```

All the logic — menu, input handling, encryption, decryption, and output — is contained in the single file `encryption_tool.py`.

---

## 5. How to Run

### Step 1 — Make sure Python is installed
```bash
python --version
# Should show Python 3.x
```

### Step 2 — Clone the repository
```bash
git clone https://github.com/milannai22a/Decodlabs_project-2.git
cd Decodlabs_project-2
```

### Step 3 — Run the script
```bash
python encryption_tool.py
```

### Step 4 — Follow the prompts in the terminal
```
1. Encrypt
2. Decrypt
Enter choice: ___
```

No virtual environment or package installation needed.

---

## 6. Program Flow

```
START
  │
  ▼
Show menu:
  1. Encrypt
  2. Decrypt
  │
  ▼
User selects option
  │
  ├── Option 1: ENCRYPT
  │     │
  │     ▼
  │   Prompt: "Enter message to encrypt:"
  │   Prompt: "Enter key:"
  │     │
  │     ▼
  │   Run encryption function(message, key)
  │     │
  │     ▼
  │   Print cipher text to terminal
  │
  └── Option 2: DECRYPT
        │
        ▼
      Prompt: "Enter cipher to decrypt:"
      Prompt: "Enter key:"
        │
        ▼
      Run decryption function(cipher, key)
        │
        ▼
      Print original message to terminal
  │
  ▼
END
```

---

## 7. Encryption & Decryption Logic

The tool uses a **symmetric cipher** — the same key is used to encrypt and decrypt. Below are the two common approaches achievable with pure Python built-ins:

---

### Method: XOR Cipher

Each character in the message is XOR-ed with the corresponding character in the key. The key is cycled (repeated) if it's shorter than the message.

**Why XOR?**
- Applying XOR twice with the same key returns the original value
- So the **same function handles both encrypt and decrypt**
- Works entirely with `ord()` and `chr()` — no imports needed

**Logic:**

```python
def xor_cipher(text, key):
    result = ""
    for i, char in enumerate(text):
        result += chr(ord(char) ^ ord(key[i % len(key)]))
    return result

# Encrypt and Decrypt use the SAME function
encrypted = xor_cipher("Hello", "key")
decrypted = xor_cipher(encrypted, "key")  # Returns "Hello"
```

**Why it works:**
```
A XOR B = C
C XOR B = A   ← same key reverses the operation
```

---

### Method: Caesar Cipher (Shift Cipher)

Each alphabetic character is shifted forward by a numeric key during encryption, and shifted back during decryption. Non-alphabetic characters are kept as-is.

```python
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(cipher, shift):
    return caesar_encrypt(cipher, -shift)
```

**Example:**
```
Text  : Hello
Shift : 3
Output: Khoor

Khoor → shift back 3 → Hello
```

---

### Full Program Structure

```python
def encrypt(message, key):
    # cipher logic here
    pass

def decrypt(cipher, key):
    # reverse cipher logic here
    pass

# Main menu
print("1. Encrypt")
print("2. Decrypt")
choice = input("Enter choice: ")

if choice == "1":
    msg = input("Enter message to encrypt: ")
    key = input("Enter key: ")
    print("Encrypted:", encrypt(msg, key))

elif choice == "2":
    cipher = input("Enter cipher to decrypt: ")
    key = input("Enter key: ")
    print("Decrypted:", decrypt(cipher, key))

else:
    print("Invalid choice.")
```

---

## 8. Built-in Libraries Used

This project uses **no external libraries**. All functionality is achieved with Python's built-in tools:

| Feature | How It's Done |
|---|---|
| User input | `input()` |
| Character to ASCII | `ord(char)` |
| ASCII to character | `chr(value)` |
| XOR operation | `^` operator |
| Key cycling | `i % len(key)` |
| String building | String concatenation or `join()` |
| Output | `print()`, f-strings |

---

## 9. Sample Terminal Output

**Encrypting a message:**
```
1. Encrypt
2. Decrypt
Enter choice: 1

Enter message to encrypt : Hello, DecodLabs!
Enter key                : mykey

Encrypted: (cipher string output)
```

**Decrypting back:**
```
1. Encrypt
2. Decrypt
Enter choice: 2

Enter cipher to decrypt  : (cipher string from above)
Enter key                : mykey

Decrypted: Hello, DecodLabs!
```

**Wrong key used:**
```
Enter cipher to decrypt  : (cipher string)
Enter key                : wrongkey

Decrypted: (garbled output — incorrect key)
```

---

## 10. Test Cases

| Message | Key | Encrypt → Decrypt | Expected Result |
|---|---|---|---|
| `Hello` | `abc` | encrypt then decrypt | `Hello` |
| `Python123` | `key` | encrypt then decrypt | `Python123` |
| `Hello` | `abc` | decrypt with wrong key `xyz` | Garbled output |
| `Hello World` | `a` | encrypt then decrypt | `Hello World` |
| `` (empty) | `key` | encrypt | Empty output |

> ✅ A correct implementation always returns the original message when the same key is used.

---

## 11. Known Limitations

- XOR and Caesar ciphers are **not cryptographically secure** — intended for learning only
- No protection against wrong key — produces garbled output silently
- No input validation — empty message or key may cause errors
- Single-run program — exits after one operation
- Cipher text from XOR may contain non-printable characters depending on inputs

---

## 12. Future Improvements

- Add a loop so the user can encrypt/decrypt multiple messages without restarting
- Add input validation (empty message or key check)
- Support encrypting entire text files
- Add a stronger cipher using Python's built-in `hashlib` for key hashing
- Display cipher text in Base64 format for readability (using built-in `base64` module)
- Allow the user to choose between multiple cipher methods (XOR, Caesar, etc.)

---

*Documentation last updated: May 2026*
