# mcp_cli.py

import requests

API_URL = "http://127.0.0.1:8000/calculate"

def main():
    print("MCP CLI Calculator")
    print("Enter math expressions like: 5+7, 10-3, 8/2, 2**3")
    print("Type 'exit' to quit.\n")

    while True:
        expr = input(">> ").strip()
        if expr.lower() == "exit":
            break
        if not expr:
            continue

        try:
            response = requests.post(API_URL, json={"expr": expr})
            response.raise_for_status()
            result = response.json().get("result")
            print(f"Result: {result}")
        except requests.exceptions.RequestException as e:
            print(f"[HTTP Error] {e}")
        except Exception as e:
            if response.content:
                print(f"[Server Error] {response.json().get('detail')}")
            else:
                print(f"[Error] {e}")

if __name__ == "__main__":
    main()
