import os
import io
import time
import base64
from flask import Flask, request, jsonify
import keras_cv
import matplotlib.pyplot as plt

# Directory to save images
output_dir = "generated_images"
os.makedirs(output_dir, exist_ok=True)

def plot_and_save_images(images, prompt, step):
    plt.figure(figsize=(20, 20))
    image_paths = []
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i])
        plt.axis("off")
        image_path = os.path.join(output_dir, f"{prompt.replace(' ', '_')}_{step}_{i}.png")
        plt.imsave(image_path, images[i])
        image_paths.append(image_path)
    plt.show()
    return image_paths

# Initialize the model once (warm start)
model = keras_cv.models.StableDiffusion(
    img_width=512, img_height=512, jit_compile=False
)

# Warm up the model
# model.text_to_image("warming up the model", batch_size=1)

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.get_json()
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    # Generate images
    start_time = time.time()
    images = model.text_to_image(prompt, batch_size=1)
    end_time = time.time()
    image_paths = plot_and_save_images(images, prompt, "api_request")
    
    print(f"Time taken to generate images: {end_time - start_time:.2f} seconds")

    # Convert images to base64 to send in response
    image_files = []
    for image_path in image_paths:
        with open(image_path, 'rb') as img_file:
            img_bytes = img_file.read()
            img_base64 = base64.b64encode(img_bytes).decode('utf-8')
            image_files.append(img_base64)

    return jsonify({
        'prompt': prompt,
        'images': image_files  # List of base64 encoded images
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
