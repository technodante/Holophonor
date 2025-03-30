import requests
import json
from dotenv import load_dotenv
import os
#use this link for help making key https://docs.dolby.io/media-apis/docs/guides-api-authentication
# Fetch environment variables correctly
load_dotenv()

app_key = os.getenv("APP_KEY")
app_secret = os.getenv("APP_SECRET")

# Ensure the values exist before making a request
# if not APP_KEY or not APP_SECRET:
#     raise ValueError("Missing API credentials. Make sure APP_KEY and APP_SECRET are set as environment variables.")

payload = {'grant_type': 'client_credentials', 'expires_in': 1800}
response = requests.post(
    'https://api.dolby.io/v1/auth/token',
    data=payload,
    auth=requests.auth.HTTPBasicAuth(app_key, app_secret)
)

if response.status_code == 200:
    body = response.json()
    access_token = body['access_token']
    print("Access Token:", access_token)
else:
    print("Error:", response.status_code, response.text)


import requests

# Dolby API Token
api_token = os.getenv("DOLBYIO_API_TOKEN", access_token)  

# File to upload
file_path = "wet_hands.mp3"

# Dolby API URL to get a pre-signed upload URL
url = "https://api.dolby.com/media/input"

# Request headers
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Request body (dlb:// URL for Dolby storage)
body = {"url": "dlb://in/wet_hands.mp3"}

# Send request to Dolby API
response = requests.post(url, json=body, headers=headers)

# Debug: Print response content
print("Response Status Code:", response.status_code)
print("Response Text:", response.text)

# Check if request was successful
if response.status_code != 200:
    print("❌ Failed to get a pre-signed URL. Check your API key and request format.")
    exit()

# Parse response JSON
data = response.json()

# Ensure 'url' key exists
if "url" not in data:
    print("❌ Key 'url' not found in response:", data)
    exit()

# Extract pre-signed URL
presigned_url = data["url"]

# Upload media file to Dolby storage
print(f"Uploading {file_path} to {presigned_url}...")

with open(file_path, "rb") as input_file:
    upload_response = requests.put(presigned_url, data=input_file)

# Check upload status
if upload_response.status_code != 200:
    print("❌ Upload failed:", upload_response.status_code, upload_response.text)
    exit()

print("✅ Upload successful!")

# Now, request media analysis
analyze_url = "https://api.dolby.com/media/analyze/music"

body = {
    "input": "dlb://in/wet_hands.mp3",
    "output": "dlb://out/airplane.analysis.json"
}

response = requests.post(analyze_url, json=body, headers=headers)

# Check response
if response.status_code != 200:
    print("❌ Analysis request failed:", response.status_code, response.text)
else:
    print("✅ Analysis request successful!", response.json())

import shutil

output_path = "test.json"

url = "https://api.dolby.com/media/output"

args = {
    "url": "dlb://out/airplane.analysis.json",
}

with requests.get(url, params=args, headers=headers, stream=True) as response:
    response.raise_for_status()
    response.raw.decode_content = True
    print("Downloading from {0} into {1}".format(response.url, output_path))
    with open(output_path, "wb") as output_file:
        shutil.copyfileobj(response.raw, output_file)