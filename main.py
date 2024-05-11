from camera import capture_image
from aiwork import analyze_image, text_to_speech
import subprocess
from pathlib import Path

if __name__ == "__main__":
    while True:
        user_input = input("Want to take a photo? (y/n): ").strip().lower()
        if user_input == 'y':
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

            # Play the speech file
            subprocess.run(['aplay', str(speech_file_path)])

            continue_prompt = input("Take another photo? (y/n): ").strip().lower()
            if continue_prompt != 'y':
                break
        else:
            print("Exiting...")
            break
