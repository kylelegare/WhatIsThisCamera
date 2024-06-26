import RPi.GPIO as GPIO
from camera import capture_image
from aiwork import analyze_image, text_to_speech
import subprocess
from pathlib import Path
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

last_press_time = 0

def handle_button_press(channel):
    global last_press_time
    current_time = time.time()

    if (current_time - last_press_time) < 1.0:  # 1000 ms debounce
        return

    last_press_time = current_time
    print("Button pressed! Taking photo...")

    image_path = 'captured_image.jpg'
    capture_image(image_path)

    result = analyze_image(image_path)
    print(result)

    speech_file_path = Path("speech.mp3")
    text_to_speech(result, speech_file_path)

    subprocess.run(['mpg123', str(speech_file_path)])

# Increase bouncetime to 1000 ms to match the software debounce time
GPIO.add_event_detect(17, GPIO.FALLING, callback=handle_button_press, bouncetime=1000)

try:
    print("Ready! Press the button to take a photo.")
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
