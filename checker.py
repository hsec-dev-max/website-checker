import requests
import time
from bs4 import BeautifulSoup

def check_website(url):
    print(f"\n🔍 Checking: {url}")
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
        check_ssl(url)
        check_headers(url)
        check_broken_links(url)

    except requests.exceptions.ConnectionError:
        print("❌ ERROR: Cannot reach the website")
    except requests.exceptions.Timeout:
        print("❌ ERROR: Website took too long to respond")

def check_ssl(url):
    if url.startswith("https://"):
        print("🔒 SSL     : Secure ✅")
    else:
        print("⚠️  SSL     : Not Secure ❌")

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

    except:
        pass

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

    except:
        print("❌ Could not check links")

# --- Main ---
while True:
    url = input("\nEnter website URL (or 'quit' to exit): ")
    if url == "quit":
        break
    if not url.startswith("http"):
        url = "https://" + url
    check_website(url)