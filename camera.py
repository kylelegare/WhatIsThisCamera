# camera.py
from picamera2 import Picamera2
from time import sleep

def capture_image(image_path):
    try:
        picam2 = Picamera2()
        config = picam2.create_still_configuration(main={"size": (800, 600)}, display=None)  # Disable preview window
        picam2.configure(config)
        picam2.start()
        sleep(1)  # Let the camera warm up (you can adjust this value)
        picam2.capture_file(image_path)
        picam2.stop()
    except Exception as e:
        print(f"An error occurred while capturing the image: {e}")
