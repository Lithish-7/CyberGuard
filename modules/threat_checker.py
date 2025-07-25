import requests

API_URL = "https://api.abuseipdb.com/api/v2/check"
API_KEY = "demo"  # Replace with your key from abuseipdb.com

def check_ip(ip):
    headers = {"Key": API_KEY, "Accept": "application/json"}
    params = {"ipAddress": ip, "maxAgeInDays": "90"}
    try:
        response = requests.get(API_URL, headers=headers, params=params)
        data = response.json()
        if "data" in data:
            print(f"IP: {data['data']['ipAddress']}")
            print(f"Abuse Confidence Score: {data['data']['abuseConfidenceScore']}")
        else:
            print("Error: Could not retrieve data.")
    except Exception as e:
        print("Error:", e)
