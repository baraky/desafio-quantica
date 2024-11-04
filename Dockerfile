FROM python:3.9-slim

WORKDIR /app

COPY consumer.py .
COPY multi.sh .
COPY requirements.txt .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["sh", "multi.sh"]
