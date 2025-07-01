import requests

METHODS_TO_TEST = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "TRACE", "CONNECT"]

def fetch_headers_and_test_methods(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    print(f"\n🔍 Target URL: {url}\n")

    spoofed_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Origin': url,
        'Referer': url
    }

    try:
        response = requests.get(url, headers=spoofed_headers, timeout=5)

        print("📤 Request Headers Sent:\n")
        for key, value in response.request.headers.items():
            print(f"{key}: {value}")

        print("\n📥 Response Headers Received:\n")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        print("\n🧾 General Information:\n")
        print(f"Status Code   : {response.status_code}")
        print(f"Content Type  : {response.headers.get('Content-Type', 'N/A')}")
        print(f"Server        : {response.headers.get('Server', 'N/A')}")
        print(f"Content Length: {response.headers.get('Content-Length', 'N/A')}")
        print(f"Encoding      : {response.encoding}")

        # Check allowed methods via OPTIONS
        print("\n🔎 Allowed HTTP Methods (via OPTIONS):\n")
        options_response = requests.options(url, headers=spoofed_headers, timeout=5)
        allow = options_response.headers.get('Allow')
        if allow:
            print(f"Allow header  : {allow}")
        else:
            print("Allow header not provided in OPTIONS response.")

        # Test all common HTTP methods
        print("\n🚀 Testing Common HTTP Methods:\n")
        for method in METHODS_TO_TEST:
            try:
                if method in ["POST", "PUT", "DELETE", "CONNECT"]:
                    test_response = requests.request(
                        method,
                        url,
                        headers={**spoofed_headers, 'Content-Type': 'application/x-www-form-urlencoded'},
                        data="test=data",
                        timeout=5
                    )
                else:
                    test_response = requests.request(method, url, headers=spoofed_headers, timeout=5)

                print(f"[{method}] → Status: {test_response.status_code} | Reason: {test_response.reason}")
            except requests.exceptions.RequestException as e:
                print(f"[{method}] → Error: {e}")

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Connection Error: {e}")

def main():
    print("\n🌐 HTTP Header & Method Tester Tool\n")
    print("🔧" + "="*60)
    print("🔧        \033[1m\033[97mDEVELOPED BY: SAINI01SANDEEP\033[0m")
    print("🔧" + "="*60 + "\n")
    url = input("Enter website URL or domain (e.g. example.com or https://example.com): ")
    fetch_headers_and_test_methods(url)

if __name__ == "__main__":
    main()
