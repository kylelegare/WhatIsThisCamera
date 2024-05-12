import RPi.GPIO as GPIO
from camera import capture_image
from aiwork import analyze_image, text_to_speech
import subprocess
from pathlib import Path
import time

# Initialize GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button pin set as input with an internal pull-up resistor

def handle_button_press(channel):
    print("Button pressed! Taking photo...")
    # Path where the image will be saved
    image_path = 'captured_image.jpg'

    # Capture the image
    capture_image(image_path)

    # Analyze the image
    result = analyze_image(image_path)
    print(result)

    # Path where the speech will be saved
    speech_file_path = Path("speech.mp3")

    # Convert text to speech
    text_to_speech(result, speech_file_path)

    # Play the speech file using mpg123
    subprocess.run(['mpg123', str(speech_file_path)])

# Add event detection to the button pin
GPIO.add_event_detect(17, GPIO.FALLING, callback=handle_button_press, bouncetime=300)

try:
    print("Ready! Press the button to take a photo.")
    # Keep the program running to monitor the button
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()  # Clean up GPIO on exit
