import subprocess
import io
import openai
import time


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

  # Read image data
  with open(image_path, 'rb') as image_file:
    image_data = image_file.read()

  # Upload the image to OpenAI and analyze it
  try:
    response = openai.Image.create(model="openai-vision-latest",
                                   file=image_data,
                                   tasks=["classify"])

    # Print the result
    print(response['data'][0]['response']['results'])
  except Exception as e:
    print(f"An error occurred: {e}")


if __name__ == "__main__":
  # Path where the image will be saved
  image_path = 'captured_image.jpg'

  # Capture an image
  capture_image(image_path)

  # Analyze the captured image
  analyze_image(image_path)
