# 🔐 Website Security Checker

A Python tool that scans any website and generates a professional PDF security report.

---

## 📋 What It Checks

| Check | Description |
|-------|-------------|
| ✅ Status | Is the website online? |
| ⚡ Speed | How fast does it respond? |
| 🔒 SSL | Is the connection secure? |
| 🛡️ Security Headers | Protection against XSS, Clickjacking, etc. |
| 🔗 Broken Links | Any dead links on the page? |

---

## 📄 Sample Report

The tool generates a clean PDF report like this:
Website Security Report
━━━━━━━━━━━━━━━━━━━━━
Target: https://example.com
Status: 200 - UP
Speed: 0.38 seconds
SSL: Secure
Security Headers: 2/4
Broken Links: None found

---

## 🚀 How To Run

```bash
git clone https://github.com/hsec-dev-max/website-checker
cd website-checker
pip install requests fpdf2 beautifulsoup4
python3 checker.py
```

---

## 🛠️ Built With

- Python 3.13
- requests
- fpdf2
- BeautifulSoup4

---

*Built by [hsec-dev-max](https://github.com/hsec-dev-max)*