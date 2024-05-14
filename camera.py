# camera.py
import subprocess

def capture_image(image_path):
    try:
        subprocess.run([
            'libcamera-still',
            '-o', image_path,
            '--width', '800', '--height', '600',
            '--shutter', '30000',    # Fixed exposure time (30,000 microseconds)
            '--gain', '4',           # Fixed analog gain
            '--awbgains', '1,1',     # Fixed automatic white balance gains
            '--framerate', '30'      # Fixed frame rate
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while capturing the image: {e}")
