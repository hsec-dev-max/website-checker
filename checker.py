import requests
import time

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
        
    except requests.exceptions.ConnectionError:
        print("❌ ERROR: Cannot reach the website")
    except requests.exceptions.Timeout:
        print("❌ ERROR: Website took too long to respond")

# --- Main ---
while True:
    url = input("\nEnter website URL (or 'quit' to exit): ")
    if url == "quit":
        break
    if not url.startswith("http"):
        url = "https://" + url
    check_website(url)