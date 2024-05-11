from camera import capture_image
from aiwork import analyze_image

if __name__ == "__main__":
    while True:
        user_input = input("Want to take a photo? (y/n): ").strip().lower()
        if user_input == 'y':
            image_path = 'captured_image.jpg'
            capture_image(image_path)
            result = analyze_image(image_path)
            print(result)

            continue_prompt = input("Take another photo? (y/n): ").strip().lower()
            if continue_prompt != 'y':
                break
        else:
            print("Exiting...")
            break
