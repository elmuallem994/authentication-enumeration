# User Enumeration via Verbose Errors

This project demonstrates how verbose error messages in authentication mechanisms
can be abused to enumerate valid users during the login process.

---

## 🧠 Concept

When a login page returns different error messages such as:

- **"Email does not exist"**
- **"Invalid password"**

An attacker can determine whether a specific user exists in the system.

This vulnerability is known as **Authentication Enumeration** and often occurs
due to improperly handled error messages.

---

## ⚙️ How It Works

The script automates the enumeration process by:

- Sending login requests with a **fixed (incorrect) password**
- Iterating over a list of email addresses
- Analyzing server responses
- Distinguishing between:
  - **Non-existing users**
  - **Existing users with incorrect passwords**

---

## 📋 Prerequisites

- Python 3.8+
- Internet connection
- Permission to test the target application

---

## 🛠️ Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/elmuallem994/authentication-enumeration.git
cd authentication-enumeration
pip install -r requirements.txt
```


## 🚀 Usage

```bash
python3 script.py <email_list_file> <login_url>
```

## 📌 Example Output


```text
[INVALID] test1@gmail.com
[INVALID] admin@gmail.com
[VALID] canderson@gmail.com

Valid emails found:
canderson@gmail.com
```
