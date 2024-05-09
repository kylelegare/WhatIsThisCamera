import io
import openai
import time
from picamera import PiCamera

# Function to capture and analyze the image
def capture_and_analyze():
    # Initialize the camera
    camera = PiCamera()
    camera.resolution = (1024, 768)

    # Give the camera some time to warm up
    time.sleep(2)

    # Capture the image to a stream
    stream = io.BytesIO()
    camera.capture(stream, format='jpeg')
    stream.seek(0)

    # Initialize OpenAI client
    client = openai.OpenAI()

    # Upload the image to OpenAI and analyze it
    try:
        response = client.images.create(
            model="openai-vision-latest",
            images=[
                {"type": "image", "image": {"data": stream.read()}}
            ],
            tasks=["classify"]
        )

        # Print the result
        print(response['tasks'][0]['response']['results'])

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        camera.close()

if __name__ == "__main__":
    capture_and_analyze()
