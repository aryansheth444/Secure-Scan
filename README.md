# 🛡️ Secure-Scan

Secure-Scan is a lightweight web-based security scanner built with Flask that helps users quickly inspect a website's security headers and basic server information.

## 🚀 Features

* Website URL Analysis
* HTTP Status Code Detection
* Server Information Lookup
* Content-Type Detection
* HSTS (HTTP Strict Transport Security) Check
* Content Security Policy (CSP) Check
* X-Frame-Options Check
* User-Friendly Dashboard
* Fast and Lightweight

## 📸 Preview<img width="1918" height="911" alt="Screenshot 2026-06-12 150113" src="https://github.com/user-attachments/assets/8dbdff50-357f-4f7c-997a-67d0bdb23258" />
<img width="1536" height="1024" alt="54" src="https://github.com/user-attachments/assets/2ef37ca9-a69d-4fd9-861e-849b61015f39" />


Secure-Scan allows users to enter a website URL and instantly receive a security report containing important HTTP header information.

## 🛠️ Technologies Used

* Python
* Flask
* Requests
* HTML5
* CSS3
* Bootstrap 5

## 📂 Project Structure

```bash
Secure-Scan/
│
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
```

## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Secure-Scan.git
cd Secure-Scan
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```bash
http://127.0.0.1:5000
```

## 🌐 Deployment

This project can be deployed on:

* Render
* Railway
* PythonAnywhere
* VPS Servers

## 🔒 Security Headers Checked

| Header          | Description                    |
| --------------- | ------------------------------ |
| HSTS            | Enforces HTTPS connections     |
| CSP             | Prevents XSS attacks           |
| X-Frame-Options | Protects against Clickjacking  |
| Content-Type    | Displays response content type |
| Server          | Shows server information       |

## 🎯 Future Enhancements

* SSL Certificate Analysis
* Port Scanning
* Vulnerability Detection
* WHOIS Lookup
* DNS Enumeration
* Security Score Calculation
* Export Reports (PDF)

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## 📜 License

This project is open-source and available under the MIT License.

---

### Developed with ❤️ using Flask & Cybersecurity Concepts
