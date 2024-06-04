#!/bin/bash

# Define the server URL
url="http://128.105.144.183:5000/generate"

# Define the JSON payload
json_payload='{"prompt":"Playing billiard"}'

# Send the POST request and save the response
response=$(curl -s -X POST -H "Content-Type: application/json" -d "$json_payload" $url)

# Extract the base64 encoded image from the response using jq
image_data=$(echo $response | jq -r '.images[0]')

# Decode the base64 image data and save it to a file
echo $image_data | base64 --decode > ~/Desktop/tamuq_img.png

echo "Image saved successfully."
