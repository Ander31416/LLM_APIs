import base64

import requests
from groq import Groq
from openai import OpenAI

def generate_response_groq_LLaVA(image_url, text):
    # Descargar la imagen desde la URL
    response = requests.get(image_url)
    image_data = response.content

    # Convertir la imagen a base64
    image_base64 = base64.b64encode(image_data).decode('utf-8')

    # Crear el objeto de mensaje
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

    # Crear la solicitud de completación
    client = Groq(
        api_key="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"
    )
    completion = client.chat.completions.create(
        model="llava-v1.5-7b-4096-preview",
        messages=[message],
        temperature=1,
        max_tokens=4096,
        top_p=1,
        stream=False,
        stop=None
    )

    # Obtener la respuesta
    response = completion.choices[0].message.content

    return response

def generate_response_openai_gpt4o(image_url, text):
    client = OpenAI(
        api_key="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"
    )

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
                            "url": "https://imagenes.20minutos.es/files/image_990_556/uploads/imagenes/2019/08/08/1028312.jpg"
                        }
                    },
                    {
                        "type": "text",
                        "text": "Describe el contenido de esta imagen"
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
    print("hola")
    if model == "LLaVA":
        print("groq")
        response = generate_response_groq_LLaVA(image_url, text)
    if model == "GPT4o":
        print("gpt4")
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