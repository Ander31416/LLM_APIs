# 1. crear endpoint de fastAPI que tenga como input la URL de una imagen y un String
# 2. crear un nuevo archivo con el código en colab
# 3. Implementar la  2 lógica del archivo del punto en el endpoint creado en el punto 1

# correr programa: uvicorn LLMcontroller:app --reload
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

from LLMservice import process_image_and_text

app = FastAPI()

# Esquema de la solicitud con Pydantic
class ImageRequest(BaseModel):
    image_url: HttpUrl  # Validar que sea una URL válida
    description: str    # Un string que acompaña la imagen

# Ruta raíz ("/") para evitar el 404
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI image processor!"}

# Crear un endpoint para recibir la URL de la imagen y el string
@app.post("/process_image/groq")
async def process_image_groq_LLaVA(request: ImageRequest):
    # Aquí se procesaría la imagen y el string
    print("kfjksdjfds")
    response = process_image_and_text("LLaVA", request.image_url, request.description)
    return {
        "message": "Datos recibidos con éxito",
        "response": response
    }

@app.post("/process_image/openai")
async def process_image_openai_gpt4o(request: ImageRequest):
    # Aquí se procesaría la imagen y el string
    print("kfjksdjfds")
    response = process_image_and_text("GPT4o", request.image_url, request.description)
    return {
        "message": "Datos recibidos con éxito",
        "response": response
    }

# Ejecutar el servidor en modo local
# Puedes usar uvicorn desde la línea de comandos con este archivo
# uvicorn nombre_del_archivo:app --reload
