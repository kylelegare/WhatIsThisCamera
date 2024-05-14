# camera.py
import subprocess

def capture_image(image_path):
    try:
        subprocess.run(['libcamera-still', '-o', image_path, '--width', '800', '--height', '600'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while capturing the image: {e}")
