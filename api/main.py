from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pika
import os
from typing import Optional
import secrets
from fastapi import APIRouter

# Definir el modelo de mensaje
class Message(BaseModel):
    content: str

# Configuración de autenticación básica
security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "admin")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

def get_rabbitmq_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=os.getenv('RABBITMQ_HOST', 'rabbitmq'),
        credentials=pika.PlainCredentials(
            os.getenv('RABBITMQ_USER', 'guest'),
            os.getenv('RABBITMQ_PASS', 'guest')
        )
    ))
    return connection

# Creamos el router con el prefijo /api
router = APIRouter(prefix="/api")

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

@router.post("/message")
async def create_message(message: Message, username: str = Depends(get_current_username)):
    try:
        connection = get_rabbitmq_connection()
        channel = connection.channel()
        
        channel.queue_declare(queue='messages', durable=True)
        channel.basic_publish(
            exchange='',
            routing_key='messages',
            body=message.content.encode(),
            properties=pika.BasicProperties(delivery_mode=2)
        )
        
        connection.close()
        return {"status": "Message sent to queue"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Crear la aplicación FastAPI
app = FastAPI()

# Incluir el router
app.include_router(router)

# Configuración de CORS (opcional pero recomendado)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)