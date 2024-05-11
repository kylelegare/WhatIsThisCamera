import base64
import requests
import os
import openai
from pathlib import Path


def encode_image_to_data_uri(image_path):
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        return f"data:image/jpeg;base64,{base64_image}"


def analyze_image(image_path):
    api_key = os.getenv('OPENAI_API_KEY')
    image_data_uri = encode_image_to_data_uri(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model":
        "gpt-4-turbo",
        "messages": [{
            "role":
            "user",
            "content": [{
                "type": "text",
                "text": "What’s in this image?"
            }, {
                "type": "image_url",
                "image_url": {
                    "url": image_data_uri
                }
            }]
        }],
        "max_tokens":
        300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions",
                             headers=headers,
                             json=payload)
    try:
        return response.json()['choices'][0]['message']['content']
    except KeyError:
        return response.json()


def text_to_speech(text, speech_file_path):
    client = openai.OpenAI()
    response = client.audio.speech.create(model="tts-1",
                                          voice="alloy",
                                          input=text)
    # Write the binary audio content to a file
    with open(speech_file_path, "wb") as audio_file:
        audio_file.write(response.content)