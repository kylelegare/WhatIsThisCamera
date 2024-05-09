import subprocess
import base64
import requests
import os

# Function to capture an image using libcamera-still
def capture_image(image_path):
    # Use libcamera-still to capture an image
    try:
        subprocess.run(['libcamera-still', '-o', image_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while capturing the image: {e}")

# Function to encode the image in base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to analyze the captured image using OpenAI
def analyze_image(image_path):
    # Get the API key from environment variables
    api_key = os.getenv('OPENAI_API_KEY')

    # Encode the image
    base64_image = encode_image(image_path)

    # Headers for the OpenAI API request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Payload for the OpenAI API request
    payload = {
        "model": "gpt-4-turbo",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image?"},
                    {"type": "image", "image": {"data_base64": base64_image}}
                ]
            }
        ],
        "max_tokens": 300
    }

    # Sending the request to OpenAI
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    # Print the result from OpenAI
    try:
        # Attempt to parse and print the response
        print(response.json()['choices'][0]['message']['content'])
    except KeyError:
        # If there's an issue in the path, print the whole response to debug
        print(response.json())

if __name__ == "__main__":
    # Path where the image will be saved
    image_path = 'captured_image.jpg'

    # Capture an image
    capture_image(image_path)

    # Analyze the captured image
    analyze_image(image_path)
