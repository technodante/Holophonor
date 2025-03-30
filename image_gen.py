import requests
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("HIVE_API_KEY")

print(key)

headers = {
    'authorization': 'Bearer ' + key,
    'Content-Type': 'application/json',
}

json_data = {
    'input': {
        'prompt': 'Nestled within the depths of an enchanted forest, a wooden bridge serves as a pathway lined with glowing lanterns, casting a warm, golden light across its surface. Surrounded by dense trees, the bridge is carpeted with fallen leaves, adding to the mystical ambiance of the setting. The air seems filled with a magical mist, enhancing the dreamlike quality of the forest, inviting onlookers into a tranquil, otherworldly journey.',
        'negative_prompt': 'blurry',
        'image_size': { 'width': 1024, 'height': 1024},
        'num_inference_steps': 15,
        'guidance_scale': 3.5,
        'num_images': 1,
        'seed': 67,
        'output_format': 'png'
    }
}
    
def sendImage():
    response = requests.post('https://api.thehive.ai/api/v3/hive/sdxl-enhanced', headers=headers, json=json_data)
    json_response = response.json()
    image_urls = [entry["url"] for entry in json_response.get("output", [])]
    return image_urls[0]

# print(image_urls)
# print("abel")