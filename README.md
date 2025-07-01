# HTTPxRay

🔎 HTTPxRay
HTTPxRay is a Python-based utility designed to inspect and audit HTTP headers and test all major HTTP methods against a target website. It helps in web reconnaissance and security assessments by giving insights into request/response headers, supported HTTP methods, and general server behavior.

📌 Features
📤 Display request headers sent to the server.

📥 Display response headers received from the server.

🧾 Extract server details such as:

Status Code
Content Type
Server info
Content Length
Encoding

🔎 Check supported HTTP methods using the OPTIONS method.

🚀 Test all major HTTP methods:

GET, POST, PUT, DELETE, OPTIONS, HEAD, TRACE, CONNECT

🛠️ Installation
This tool works best on Linux-based systems and requires Python 3.x.

✅ Requirements
Install Python dependencies (only requests module is needed):

bash
Copy
Edit
pip install requests

🚀 Usage

1. Clone the repository:
bash
Copy
Edit
git clone https://github.com/saini01sandeep/HTTPxRay.git
cd HTTPxRay
2. Run the tool:
bash
Copy
Edit
python3 httpxray.py
You will be prompted to enter a URL or domain:

less
Copy
Edit
Enter website URL or domain (e.g. example.com or https://example.com):
The tool will handle adding http:// if the scheme is missing.

🧪 Sample Output
shell
Copy
Edit
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
...

🔎 Allowed HTTP Methods (via OPTIONS):
Allow header  : GET, POST, OPTIONS

🚀 Testing Common HTTP Methods:
[GET]     → Status: 200 | Reason: OK
[POST]    → Status: 405 | Reason: Method Not Allowed
[TRACE]   → Status: 501 | Reason: Not Implemented
...

👨‍💻 Author
Sandeep Saini
GitHub: saini01sandeep
Built with ❤️ for ethical hackers, bug bounty hunters, and developers.

📣 Contribution
Feel free to contribute or suggest improvements via pull requests or issues!
