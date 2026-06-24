import requests

print("=" * 60)
print("        PYTHON WEB TECHNOLOGY DETECTOR")
print("=" * 60)

# Website input
url = input("Enter website URL: ")

# Add HTTPS if missing
if not url.startswith("http"):
    url = "https://" + url

try:
    # Send request
    response = requests.get(url, timeout=10)

    # Get headers
    headers = response.headers

    print("\n[+] Website Information")
    print("-" * 60)

    print(f"URL             : {url}")
    print(f"Status Code     : {response.status_code}")

    # Detect Server
    server = headers.get("Server", "Not Detected")
    print(f"Server          : {server}")

    # Detect Powered By
    powered_by = headers.get("X-Powered-By", "Not Detected")
    print(f"Powered By      : {powered_by}")

    # CDN / WAF Detection
    print("\n[+] CDN / WAF Detection")
    print("-" * 60)

    server_lower = server.lower()

    if "cloudflare" in server_lower:
        print("CDN/WAF         : Cloudflare")

    elif "akamai" in server_lower:
        print("CDN/WAF         : Akamai")

    elif "sucuri" in server_lower:
        print("CDN/WAF         : Sucuri")

    else:
        print("CDN/WAF         : Not Detected")

    # Framework Detection
    print("\n[+] Framework Detection")
    print("-" * 60)

    cookies = headers.get("Set-Cookie", "")

    if "PHPSESSID" in cookies:
        print("Framework       : PHP")

    elif "JSESSIONID" in cookies:
        print("Framework       : Java")

    elif "ASP.NET" in cookies:
        print("Framework       : ASP.NET")

    else:
        print("Framework       : Unknown")

    # Important Headers
    print("\n[+] Important Headers")
    print("-" * 60)

    important_headers = [
        "Content-Type",
        "Content-Length",
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "Set-Cookie"
    ]

    for header in important_headers:
        value = headers.get(header)

        if value:
            print(f"{header}: {value}")

    # Security Headers
    print("\n[+] Security Headers")
    print("-" * 60)

    security_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "Referrer-Policy"
    ]

    for sec_header in security_headers:

        if sec_header in headers:
            print(f"[FOUND]   {sec_header}")

        else:
            print(f"[MISSING] {sec_header}")

except requests.exceptions.RequestException as e:
    print("\n[!] Connection Error")
    print(f"Error: {e}")