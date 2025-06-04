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
![Captura de pantalla 2025-06-03 190423](https://github.com/user-attachments/assets/ee49f818-b308-4463-9e42-2f7f4da659b9)

3. Accede a la API:
   - Abre tu navegador y ve a `http://localhost/api/health` para verificar que la API está funcionando.
  
   ![SD_2](https://github.com/user-attachments/assets/021d822e-c7a7-4538-99e7-d77b7bf3a6e8)

   - Puedes enviar mensajes a través de la API. 

4. Envía un mensaje:
   ```bash
   curl -X POST http://localhost/api/message -H "Content-Type: application/json" -d '{"content": "Hola, mundo!"}'
   ```

![SD_3](https://github.com/user-attachments/assets/879eeb87-bcbf-4b96-a815-251cffcee54f)
![SD_4](https://github.com/user-attachments/assets/0de1643d-3a19-40f5-8dba-a68ca5f530a3)
5. Ver mensajes recibivos

    - docker exec worker cat /app/messages/received_messages.log
![SD_5](https://github.com/user-attachments/assets/b00aeab6-91a5-4dc1-a1ac-9cdc05225db9)

6. Monitoreo:
   - Abre tu navegador y ve a `http://localhost/monitor` para ver el estado de RabbitMQ.
   - API Docs: http://localhost/api/docs
   - Traefik Dashboard: http://localhost:8080/dashboard/
  
Punto 1....
![image](https://github.com/user-attachments/assets/52975e9b-6904-4f85-9cb0-3529129491fb)
![image](https://github.com/user-attachments/assets/a8e927b6-2ce0-4dc6-83d0-c4bc63f0d60c)
![image](https://github.com/user-attachments/assets/51f63cd9-18e4-4d66-aaaa-b1612ebb2ecb)



