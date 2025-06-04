# Sistema de Mensajería con FastAPI y RabbitMQ

Este proyecto implementa un sistema de mensajería distribuido utilizando:
- FastAPI como API REST
- RabbitMQ como broker de mensajes
- Worker para procesamiento asíncrono
- Traefik como reverse proxy

## Estructura del Proyecto

```
ParcialFinal/
├── api/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── worker/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

## Requisitos Previos

- Docker
- Docker Compose
- Git (opcional)

## Instalación y Ejecución

1. Clona el repositorio:
   ```bash
    git clone https://github.com/CASILA-19/ParcialFinal_SD
   cd ParcialFinal_SD
   ```

2. Construye y ejecuta los contenedores:
   ```bash
   docker-compose up --build
   ```

3. Accede a la API:
   - Abre tu navegador y ve a `http://localhost/api/health` para verificar que la API está funcionando.
   - Puedes enviar mensajes a través de la API. 

4. Envía un mensaje:
   ```bash
   curl -X POST http://localhost/api/message -H "Content-Type: application/json" -d '{"content": "Hola, mundo!"}'
   ```
5. Ver mensajes recibivos
    - docker exec worker cat /app/messages/received_messages.log
6. Monitoreo:
   - Abre tu navegador y ve a `http://localhost/monitor` para ver el estado de RabbitMQ.
   - API Docs: http://localhost/api/docs
   - Traefik Dashboard: http://localhost:8080/dashboard/
