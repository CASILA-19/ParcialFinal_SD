FROM python:3.9-slim

WORKDIR /app

RUN mkdir -p /app/messages
VOLUME /app/messages

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]