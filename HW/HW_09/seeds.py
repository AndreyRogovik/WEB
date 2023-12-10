import json
from mongoengine import connect
from models import Quote, Author
from connect import uri
from dateutil import parser

# Підключення до MongoDB
connect('web16', host=uri)


# Завантаження даних з JSON-файлу
with open('authors.json', 'r', encoding='utf-8') as file:
    authors_data = json.load(file)


for author_data in authors_data:
    author_data['born_date'] = parser.parse(author_data['born_date'])
    author = Author(**author_data)
    author.save()

print("Authors data loaded successfully.")


# Завантаження даних з JSON-файлу
with open('quotes.json', 'r', encoding='utf-8') as file:
    quotes_data = json.load(file)
    print (quotes_data)
# Запис цитат у базу даних
for quote_data in quotes_data:
    # Отримання автора за ім'ям
    author_name = quote_data.pop('author')
    author = Author.objects.get(fullname=author_name)

    # Створення цитати та збереження авторського об'єкта
    quote = Quote(author=author, **quote_data)
    quote.save()

print("Quotes data loaded successfully.")
