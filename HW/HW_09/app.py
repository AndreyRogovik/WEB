import json
from mongoengine import connect
from models import Quote, Author
from  connect import uri

# Підключення до MongoDB
connect('web16', host=uri)

while True:
    command = input("Введіть команду (формат: команда:значення): ").strip()

    if command.lower() == 'exit':
        break

    command_parts = command.split(':')
    if len(command_parts) != 2:
        print("Неправильний формат команди. Спробуйте ще раз.")
        continue

    action, value = command_parts

    if action == 'name':
        # Пошук цитат за ім'ям автора
        author = Author.objects(fullname=value).first()
        if author:
            quotes = Quote.objects(author=author)
            for quote in quotes:
                print(quote.quote)
        else:
            print(f"Автора {value} не знайдено.")

    elif action == 'tag':
        # Пошук цитат за тегом
        quotes = Quote.objects(tags=value)
        for quote in quotes:
            print(quote.quote)

    elif action == 'tags':
        # Пошук цитат за набором тегів
        tags = value.split(',')
        quotes = Quote.objects(tags__in=tags)
        for quote in quotes:
            print(quote.quote)

    else:
        print("Невідома команда. Спробуйте ще раз.")
