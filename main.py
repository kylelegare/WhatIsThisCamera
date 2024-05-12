from gpiozero import Button
from camera import capture_image
from aiwork import analyze_image, text_to_speech
import subprocess
from pathlib import Path
import time

# Initialize the button
# The Button is connected to GPIO 17 on the ReSpeaker 2-Mics Pi HAT
button = Button(17)

def handle_button_press():
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

# Assign the handler to the button press event
button.when_pressed = handle_button_press

print("Ready! Press the button to take a photo.")

# Keep the program running to monitor the button
while True:
    time.sleep(0.1)
