import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

WAZUH_MANAGER = "https://127.0.0.1:55000"
USER = "wazuh"
PASSWORD = "wazuh" 

def get_auth_token():
    response = requests.get(f"{WAZUH_MANAGER}/security/user/authenticate", auth=(USER, PASSWORD), verify=False)
    return response.json()['data']['token'] if response.status_code == 200 else None

def hunt_security_alerts(token):
    headers = {'Authorization': f'Bearer {token}'}
    
    # Query for security configuration and operational events across all agents
    endpoint = f"{WAZUH_MANAGER}/security/audit/logs?limit=10"
    response = requests.get(endpoint, headers=headers, verify=False)
    
    if response.status_code == 200:
        return response.json().get('data', {}).get('affected_items', [])
    return []

# --- Run the Hunt ---
token = get_auth_token()
if token:
    print("[+] SOC Pipeline Active. Searching for recent security log triggers...")
    logs = hunt_security_alerts(token)
    
    if logs:
        print(f"\n[!] Detected {len(logs)} recent security tracking events:")
        for log in logs:
            print(f"--------------------------------------------------")
            print(f" Time   : {log.get('timestamp')}")
            print(f" User   : {log.get('login_user', 'System')}")
            print(f" Action : {log.get('action', 'Unknown Action')}")
            print(f" Policy : {log.get('description', 'No description provided')}")
    else:
        print("[-] Stream is quiet. No recent alerts matching criteria found.")