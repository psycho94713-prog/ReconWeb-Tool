# 🚀 Advanced Website OSINT Framework

A production-ready Website OSINT (Open Source Intelligence) Framework developed using **FastAPI**, **Python**, and **Bootstrap**.

This tool helps security researchers, penetration testers, bug bounty hunters, students, and developers collect intelligence about a target domain from a single dashboard.

---

## ✨ Features

- 🌐 WHOIS Lookup
- 🌍 DNS Lookup
- 🔒 SSL Certificate Analysis
- 📡 HTTP Headers Analysis
- 💻 Technology Detection
- 🧩 CMS Detection
- 🛡️ WAF Detection
- 🌎 GeoIP Lookup
- 🛰️ ASN Lookup
- 📧 Email Extraction
- 🔐 Security Headers Analysis
- 📜 JavaScript Analysis
- 📂 Directory Enumeration
- 📬 Email Security Check
- 🕒 Wayback Machine Lookup
- 📊 Risk Score Calculation
- 📁 Scan History
- 🚀 REST API
- 💾 SQLite Database
- 🐳 Docker Support

---

# 🛠️ Tech Stack

## Backend

- Python 3.12+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- SQLite

## Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap 5

## Networking & Security

- Requests
- HTTPX
- Socket
- SSL
- DNS

## Development Tools

- Git
- GitHub
- Docker
- VS Code

---

# 📂 Project Structure

```text
ReconWeb-Tool/
│
├── app/
│   ├── api/
│   ├── crud/
│   ├── database/
│   ├── models/
│   ├── modules/
│   ├── schemas/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   ├── main.py
│   └── config.py
│
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🪟 Windows Installation

## 1. Clone the Repository

```bash
git clone https://github.com/psycho94713-prog/ReconWeb-Tool.git
```

## 2. Open the Project

```bash
cd ReconWeb-Tool
```

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

## 4. Activate the Virtual Environment

```bash
venv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Run the Project

```bash
uvicorn app.main:app --reload
```

## 7. Open in Browser

```
http://127.0.0.1:8000
```

## 8. Open API Documentation

```
http://127.0.0.1:8000/docs
```

---

# 🐉 Kali Linux Installation

## 1. Update the System

```bash
sudo apt update && sudo apt upgrade -y
```

## 2. Install Required Packages

```bash
sudo apt install python3 python3-pip python3-venv git -y
```

## 3. Clone the Repository

```bash
git clone https://github.com/psycho94713-prog/ReconWeb-Tool.git
```

## 4. Open the Project Folder

```bash
cd ReconWeb-Tool
```

## 5. Create a Virtual Environment

```bash
python3 -m venv venv
```

## 6. Activate the Virtual Environment

```bash
source venv/bin/activate
```

## 7. Install Project Dependencies

```bash
pip install -r requirements.txt
```

## 8. Run the Project

```bash
uvicorn app.main:app --reload
```

## 9. Open in Browser

```
http://127.0.0.1:8000
```

## 10. Open Swagger API Documentation

```
http://127.0.0.1:8000/docs
```

---

# 📄 License

This project is licensed under the **MIT License**.

