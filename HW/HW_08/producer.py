import json
import pika
from faker import Faker
from models import Contact
from mongoengine import connect
from connect import uri

# Підключення до MongoDB
connect('contacts', host=uri)

fake = Faker()


# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='contacts_queue')

# Генерація фейкових контактів
contacts = []
for _ in range(5):
    contact = Contact(fullname=fake.name(), email=fake.email())
    contact.save()
    contacts.append(str(contact.id))

# Відправлення повідомлень у чергу
for contact_id in contacts:
    message = {'contact_id': contact_id}
    channel.basic_publish(exchange='', routing_key='contacts_queue', body=json.dumps(message))

print("Contacts sent to the queue")

# Закриття з'єднань
connection.close()
