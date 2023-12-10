import requests
from bs4 import BeautifulSoup
import json

 # Створення порожнього списку для збереження цитат
authors = []
quotes = []
author_link_set = []

def search_quotes():
    for i in range(1, 11):   
        print (f'page number: {i}')  
        url = f'https://quotes.toscrape.com/page/{i}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        # Знаходження всіх елементів з класом 'quote'
        quote_elements = soup.find_all('div', class_='quote')

        # Обробка кожного елементу 'quote'
        for quote_element in quote_elements:
            # Збір інформації про цитату та додавання до списку quotes
            quote = {
                "tags": [tag.text for tag in quote_element.select('.tags a.tag')],
                "author": quote_element.select_one('.author').text,
                "quote": quote_element.select_one('.text').text.strip('“”')
            }
            quotes.append(quote)
    

    # Запис у JSON-файл
def write_quotes_to_file(quotes):
    with open('quotes.json', 'a', encoding='utf-8') as json_file:
        json.dump(quotes, json_file, ensure_ascii=False, indent=2)
        
def write_authors_to_file(authors):
    with open('authors.json', 'a', encoding='utf-8') as json_file:
        json.dump(authors, json_file, ensure_ascii=False, indent=2)
        
def search_authors_links():
    autors_links = list()
    for i in range (1, 11):
        url = f'https://quotes.toscrape.com/page/{i}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        a_tags = soup.select('.quote a[href^="/author/"]')
        
        for a_tag in a_tags:
            href_value = a_tag['href']
            autors_links.append(href_value)
    return autors_links



def search_authors():
    
    authors_links = search_authors_links()
    author_link_set = (set(authors_links))
    
    for author_element in author_link_set:     
        url = f'https://quotes.toscrape.com{author_element}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        author_details = soup.find('div', class_='author-details')
        author = {
            "fullname":  author_details.find('h3', class_='author-title').text,
            "born_date": author_details.find('span', class_='author-born-date').text,
            "born_location": author_details.find('span', class_='author-born-location').text,
            "description": author_details.find('div', class_='author-description').text
        }
        authors.append(author)
   
   

search_quotes()
write_quotes_to_file(quotes) 

search_authors()
write_authors_to_file(authors)


            