import base64
import requests
from groq import Groq
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Accessing the API keys
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def generate_response_groq_LLaVA(image_url, text):
    # Download the image from the URL
    response = requests.get(image_url)
    image_data = response.content

    # Convert the image to base64
    image_base64 = base64.b64encode(image_data).decode('utf-8')

    # Create the message object
    message = {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": text
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": "data:image/jpeg;base64," + image_base64
                }
            }
        ]
    }

    # Create the completion request
    client = Groq(api_key=GROQ_API_KEY)
    completion = client.chat.completions.create(
        model="llava-v1.5-7b-4096-preview",
        messages=[message],
        temperature=1,
        max_tokens=4096,
        top_p=1,
        stream=False,
        stop=None
    )

    # Get the response
    response = completion.choices[0].message.content
    return response

def generate_response_openai_gpt4o(image_url, text):
    client = OpenAI(api_key=OPENAI_API_KEY)

    input("GPT4o")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": ""
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": str(image_url)
                        }
                    },
                    {
                        "type": "text",
                        "text": text
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=2708,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "text"
        }
    )

    return response.choices[0].message.content

def process_image_and_text(model, image_url, text):
    print("Processing...")
    if model == "LLaVA":
        print("Using Groq")
        response = generate_response_groq_LLaVA(image_url, text)
    elif model == "GPT4o":
        print("Using GPT-4o")
        response = generate_response_openai_gpt4o(image_url, text)

    print(response)
    return response

"""
# URL de la imagen
image_url = "https://imagenes.20minutos.es/files/image_990_556/uploads/imagenes/2019/08/08/1028312.jpg"

# Generar la respuesta
text = "hazme una descripción completa de la imagen"
response = process_image_and_text("GPT4o", image_url, text)
print(response)"""