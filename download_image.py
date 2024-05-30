import requests
import json
import base64

url = 'http://128.105.144.183:5000/generate'
data = {'prompt': 'a sunset over a mountain range'}

response = requests.post(url, json=data)

if response.status_code == 200:
    response_data = response.json()
    image_data = response_data['images'][0]  # Take the first image
    image_bytes = base64.b64decode(image_data)
    with open('~/Desktop/tamuq_img.png', 'wb') as img_file:
        img_file.write(image_bytes)
else:
    print('Error:', response.status_code, response.text)
