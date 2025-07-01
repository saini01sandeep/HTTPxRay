# 🔎 HTTPxRay

**HTTPxRay** is a Linux-based Python tool designed for **HTTP header analysis** and **method testing**. It fetches request and response headers, reveals server metadata, checks supported HTTP methods, and tests commonly used HTTP verbs like `GET`, `POST`, `PUT`, `DELETE`, and more.

> 📌 Created with ❤️ by [saini01sandeep](https://github.com/saini01sandeep) for security researchers, ethical hackers, and penetration testers.

---

## 📂 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Sample Output](#-sample-output)
- [Author](#-author)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Features:

- 🌐 Takes a domain or URL and automatically resolves it
- 📤 Displays **Request Headers** sent
- 📥 Displays **Response Headers** received
- 📊 Shows **Server Details**:
  - Status Code
  - Content-Type
  - Server
  - Content-Length
  - Encoding
- 📡 Performs `OPTIONS` request to identify allowed HTTP methods
- ⚔️ Tests common HTTP methods:
  - `GET`, `POST`, `PUT`, `DELETE`, `OPTIONS`, `HEAD`, `TRACE`, `CONNECT`
- 💨 Built for **Linux-based systems**

---

## 🛠️ Installation:

> ✅ Requires Python 3.6 or higher  
> 🧰 Dependency: `requests`

### 1. Clone the repository

```
git clone https://github.com/saini01sandeep/HTTPxRay.git
cd HTTPxRay
```
2. Install dependencies
```
pip install requests
```
3. Run
```
python3 httpxray.py
```

💻 Usage:

Run the tool using Python:
```
python3 httpxray.py
When prompted:
Enter website URL or domain (e.g. example.com or https://example.com):
Provide the full or partial URL — the tool will normalize it for you.
```
📤 Sample Output
```
🌐 HTTP Header & Method Tester Tool
🔧============================================================
🔧        DEVELOPED BY: SAINI01SANDEEP
🔧============================================================

Enter website URL or domain (e.g. example.com or https://example.com): example.com

🔍 Target URL: http://example.com

📤 Request Headers Sent:
User-Agent: Mozilla/5.0 ...
Accept: */*
...

📥 Response Headers Received:
Content-Type: text/html; charset=UTF-8
Server: ECS (nyb/1D1D)
...

🧾 General Information:
Status Code   : 200
Content Type  : text/html
Server        : ECS (nyb/1D1D)
Content Length: 1256
Encoding      : UTF-8

🔎 Allowed HTTP Methods (via OPTIONS):
Allow header  : GET, POST, OPTIONS

🚀 Testing Common HTTP Methods:
[GET]     → Status: 200 | Reason: OK
[POST]    → Status: 405 | Reason: Method Not Allowed
[PUT]     → Status: 405 | Reason: Method Not Allowed
```
👨‍💻 Author:
```
Sandeep Saini
GitHub: saini01sandeep
```
🤝 Contributing:
Contributions, suggestions, and pull requests are welcome!

🔐 Disclaimer:
```
This tool is intended for educational and authorized security testing only. Unauthorized use is strictly prohibited.
```
🪪 License:
This project is licensed under the MIT License.
