import requests
import time
from bs4 import BeautifulSoup

def check_website(url):
    print(f"\n🌐 Checking: {url}")
    print("-" * 40)

    try:
        start = time.time()
        response = requests.get(url, timeout=10)
        end = time.time()

        speed = round(end - start, 2)
        status = response.status_code

        if status == 200:
            print(f"✅ Status  : {status} — Website is UP")
        else:
            print(f"⚠️  Status  : {status} — Something is wrong")

        print(f"⚡ Speed   : {speed} seconds")
        
        ssl_secure = check_ssl(url)
        headers_score = check_headers(url)
        broken_count = check_broken_links(url)

        save_pdf_report(url, status, speed, ssl_secure, headers_score, broken_count)

    except requests.exceptions.ConnectionError:
        print("❌ ERROR: Cannot reach the website")
    except requests.exceptions.Timeout:
        print("❌ ERROR: Website took too long to respond")

def check_ssl(url):
    if url.startswith("https://"):
        print("🔒 SSL     : Secure ✅")
        return True
    else:
        print("⚠️  SSL     : Not Secure ❌")
        return False

def check_headers(url):
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers

        print("\n🛡️  Security Headers:")

        checks = {
            "X-Frame-Options": "Clickjacking Protection",
            "X-XSS-Protection": "XSS Protection",
            "Strict-Transport-Security": "HTTPS Enforced",
            "Content-Security-Policy": "Content Security"
        }

        score = 0
        for header, description in checks.items():
            if header in headers:
                print(f"   ✅ {description}")
                score += 1
            else:
                print(f"   ❌ {description} — Missing!")

        print(f"\n   Score: {score}/4")
        return score

    except:
        return 0

def check_broken_links(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a")

        print(f"\n🔗 Broken Links Check:")
        broken = 0

        for link in links:
            href = link.get("href")
            if href and href.startswith("http"):
                try:
                    r = requests.get(href, timeout=5)
                    if r.status_code == 404:
                        print(f"  ❌ BROKEN: {href}")
                        broken += 1
                except:
                    print(f"  ⚠️  UNREACHABLE: {href}")
                    broken += 1

        if broken == 0:
            print("  ✅ No broken links found!")
        else:
            print(f"\n  Total broken: {broken}")

            return broken

    except:
        print("❌ Could not check links")
        
        return 0 

def save_pdf_report(url, status, speed, ssl_secure, headers_score, broken_count):
    from fpdf import FPDF
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Website Security Report", ln=True)
    
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 10, f"URL: {url}", ln=True)
    pdf.cell(0, 10, f"Status: {status}", ln=True)
    pdf.cell(0, 10, f"Speed: {speed} seconds", ln=True)
    pdf.cell(0, 10, f"SSL: {'Secure' if ssl_secure else 'Not Secure'}", ln=True)
    pdf.cell(0, 10, f"Security Headers Score: {headers_score}/4", ln=True)
    pdf.cell(0, 10, f"Broken Links: {broken_count}", ln=True)
    
    filename = "report.pdf"
    pdf.output(filename)
    print(f"\n📄 Report saved: {filename}")

# --- Main ---
while True:
    url = input("\nEnter website URL (or 'quit' to exit): ")
    if url == "quit":
        break
    if not url.startswith("http"):
        url = "https://" + url
    check_website(url)