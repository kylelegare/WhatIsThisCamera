import subprocess
import openai
import time
import os


# Function to capture an image using libcamera-still
def capture_image(image_path):
  # Use libcamera-still to capture an image
  try:
    subprocess.run(['libcamera-still', '-o', image_path], check=True)
  except subprocess.CalledProcessError as e:
    print(f"An error occurred while capturing the image: {e}")


# Function to analyze the captured image
def analyze_image(image_path):
  # Initialize OpenAI client
  openai.api_key = os.getenv('OPENAI_API_KEY')

  try:
    # Open the image file in binary mode
    with open(image_path, 'rb') as image_file:
      # Upload the image to OpenAI
      image_data = openai.File.create(file=image_file, purpose='answers')
      image_url = image_data['url']

    # Create a conversation completion to analyze the image
    response = openai.ChatCompletion.create(model="gpt-4-turbo",
                                            messages=[{
                                                "role":
                                                "user",
                                                "content": [{
                                                    "type":
                                                    "text",
                                                    "text":
                                                    "What's in this image?"
                                                }, {
                                                    "type":
                                                    "image_url",
                                                    "image_url":
                                                    image_url
                                                }]
                                            }])

    # Print the result
    print(response['choices'][0]['message']['content'])

  except Exception as e:
    print(f"An error occurred: {e}")


if __name__ == "__main__":
  # Path where the image will be saved
  image_path = 'captured_image.jpg'

  # Capture an image
  capture_image(image_path)

  # Analyze the captured image
  analyze_image(image_path)
