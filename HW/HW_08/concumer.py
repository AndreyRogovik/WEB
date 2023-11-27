import json
import pika
from time import sleep
from mongoengine import connect
from connect import uri 
from models import Contact
# Підключення до MongoDB
connect('contacts', host=uri)

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='contacts_queue')

def send_email(contact_id):
    # Функція-заглушка для відправлення email
    print(f"Sending email to contact with id {contact_id}")
    sleep(2)  # Імітація тривалості відправлення email
    contact = Contact.objects.get(id=contact_id)
    contact.is_sent = True
    contact.save()

# Обробник повідомлень з черги
def callback(ch, method, properties, body):
    message = json.loads(body)
    contact_id = message.get('contact_id')
    
    if contact_id:
        send_email(contact_id)
        print(f"Email sent for contact with id {contact_id}")

# Підписка на чергу
channel.basic_consume(queue='contacts_queue', on_message_callback=callback, auto_ack=True)

print("Consumer is waiting for messages. To exit press CTRL+C")
channel.start_consuming()
