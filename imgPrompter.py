import requests

headers = {
    'authorization': '5KuH4XBp0J5APgj9biFBRdd0gIvkzJAS',
    'Content-Type': 'application/json',
}

json_data = {
    'input': {
        'prompt': 'A happy smile in anticipated for the feast',
        'negative_prompt': 'blurry',
        'image_size': { 'width': 1024, 'height': 1024},
        'num_inference_steps': 15,
        'guidance_scale': 3.5,
        'num_images': 1,
        'seed': 67,
        'output_format': 'png'
    }
}
response = requests.post('https://api.thehive.ai/api/v3/hive/sdxl-enhanced', headers=headers, json=json_data)
print(response)
