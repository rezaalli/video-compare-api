import requests
import time

# API endpoint and key
API_URL = "http://indexapi.thinkbot.dev/compare"
STATUS_URL = "https://indexapi.thinkbot.dev/compare/status"
API_KEY = "V0U9W1wrNiMjZFosQTMwTllUNSlTSSNua1E"

# Video URLs for comparison
data = {
    'mode': 'json',
    'url1': 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4',
    'url2': 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'
}

# Make initial request
response = requests.post(API_URL, data=data, params={'api_key': API_KEY})

# Check if the request was successful
if response.status_code == 200:
    response_data = response.json()
    request_id = response_data.get('job_id')
    print(f"Request initiated successfully. ID: {request_id}")
else:
    print(f"Failed to initiate request: {response.text}")
    exit()

# Polling the status
while True:
    status_response = requests.get(f"{STATUS_URL}/{request_id}", params={'api_key': API_KEY})
    if status_response.status_code == 200:
        status_data = status_response.json()
        status = status_data.get('status')
        
        if status == "completed":
            print("✅ Comparison completed successfully!")
            print(status_data)
            break
        elif status == "queued":
            print("⏳ Job is in queue... retrying in 15 seconds.")
            time.sleep(15)
        elif status == "processing":
            print("🔄 Processing... waiting 10 seconds before checking again.")
            time.sleep(10)
        else:
            print(f"⚠️ Unexpected status: {status}")
            break
    else:
        print(f"❌ Failed to retrieve status: {status_response.text}")
        break
