import pika
import json
import requests
import cv2

def connect_to_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue="fps_converter")

    return channel, connection

def process_video(url, fps):
    filename = url.split("/")[-1].split(".")[0]
    vcap = cv2.VideoCapture(url)

    if not vcap.isOpened():
        raise ValueError("Erro ao baixar o vídeo.")

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(f'videos/{filename}.mp4',
            fourcc,
            fps,
            (int(vcap.get(3)), int(vcap.get(4))))

    while vcap.isOpened():
        ret, frame = vcap.read()
        if not ret:
            break
        out.write(frame)

    vcap.release()
    out.release()

def handle_message(ch, method, properties, body):
    try:
        message = json.loads(body)
        print(f"Mensagem recebida: {message}")
        process_video(message["url"], message["fps"])
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f" Erro ao processar a mensagem: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

def main():
    channel, connection = connect_to_rabbitmq()
    channel.basic_consume(queue='fps_converter',
            auto_ack=False,
            on_message_callback=handle_message)

    print('Esperando mensagens...')
    channel.start_consuming()
    connection.close()

if __name__ == '__main__':
    main()
