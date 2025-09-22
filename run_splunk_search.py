#This script demonstrates your ability to programmatically interact with Splunk, a crucial skill for automating SOC tasks or integrating Splunk with other security tools (like a SOAR platform). It uses Splunk's REST API to run a search and retrieve the results.

#Setup:
# You'll need Python's requests library: pip install requests
# In Splunk Cloud, go to Settings > Tokens and create a new token to use for authentication.


------

import requests
import json
import time
import sys

# --- Configuration ---
# IMPORTANT: Replace these with your Splunk Cloud details
SPLUNK_HOST = "your-instance.splunkcloud.com" 
SPLUNK_TOKEN = "your-authentication-token" # This is the token you create in Splunk Settings

# Disable SSL warnings for self-signed certs if any; not recommended for production
requests.packages.urllib3.disable_warnings()

# --- Functions ---
def run_splunk_search(query):
    """Runs a search job in Splunk and returns the results."""
    
    # 1. Create the search job
    search_url = f"https://{SPLUNK_HOST}:8089/services/search/jobs"
    headers = {'Authorization': f'Bearer {SPLUNK_TOKEN}'}
    data = {'search': f'search {query}', 'output_mode': 'json'}

    print(f"▶  Creating search job for query: '{query}'")
    try:
        response = requests.post(search_url, headers=headers, data=data, verify=False)
        response.raise_for_status()
        sid = response.json()['sid']
        print(f" Search job created with SID: {sid}")
    except requests.exceptions.HTTPError as e:
        print(f" Error creating search job: {e}")
        print(f"   Response: {response.text}")
        return None

    # 2. Poll for search job completion
    job_status_url = f"{search_url}/{sid}"
    while True:
        try:
            response = requests.get(job_status_url, headers=headers, params={'output_mode': 'json'}, verify=False)
            response.raise_for_status()
            job_status = response.json()['entry'][0]['content']['dispatchState']
            print(f"   ...Job status: {job_status}")
            if job_status in ['DONE', 'FAILED', 'CANCELED']:
                break
            time.sleep(2)
        except requests.exceptions.HTTPError as e:
            print(f" Error checking job status: {e}")
            return None
    
    if job_status != 'DONE':
        print(f" Search job did not complete successfully. Final status: {job_status}")
        return None

    # 3. Retrieve the results
    results_url = f"{search_url}/{sid}/results"
    try:
        print("▶  Retrieving results...")
        response = requests.get(results_url, headers=headers, params={'output_mode': 'json'}, verify=False)
        response.raise_for_status()
        results = response.json()['results']
        print(" Results retrieved successfully!")
        return results
    except requests.exceptions.HTTPError as e:
        print(f" Error retrieving results: {e}")
        return None

# --- Main Execution ---
if __name__ == "__main__":
    # Example SPL query to run
    spl_query = 'index="main" host="mail.sv" sourcetype="linux_secure" "failed password for root" | head 5'

    search_results = run_splunk_search(spl_query)

    if search_results:
        print("\n--- Search Results ---")
        # Pretty print the JSON results
        print(json.dumps(search_results, indent=2))
        print("----------------------")
