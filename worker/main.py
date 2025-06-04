import pika
import os
import json
from datetime import datetime
import time

def callback(ch, method, properties, body):
    message = body.decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}\n"
    
    with open('/app/messages/received_messages.log', 'a') as f:
        f.write(log_message)
    
    print(f" [x] Received {message}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def get_connection():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=os.getenv('RABBITMQ_HOST', 'rabbitmq'),
                port=5672,
                credentials=pika.PlainCredentials(
                    os.getenv('RABBITMQ_USER', 'guest'),
                    os.getenv('RABBITMQ_PASS', 'guest')
                ),
                connection_attempts=5,
                retry_delay=5
            ))
            return connection
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ no está listo, reintentando en 5 segundos...")
            time.sleep(5)

def main():
    connection = get_connection()
    channel = connection.channel()
    
    # Asegurarse de que la cola exista
    channel.queue_declare(queue='messages', durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='messages', on_message_callback=callback)
    
    print(' [*] Esperando mensajes. Presiona CTRL+C para salir')
    channel.start_consuming()

if __name__ == '__main__':
    main()