"""Пример работы с beautifulsoup"""
# 1. регулярные выражения
# 2. сторонние библиотеки beautifulsoup, lxml
# 3. scrapy
import requests
from bs4 import BeautifulSoup
import json
import pprint
domain = 'https://www.gazeta.ru/'
url = f'{domain}/sport'

response = requests.get(url)

# print(response.status_code)

# print(response.text)

# Создаем суп для разбора html
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
result = {}
news_a = soup.find_all('a', class_='b_ear m_simple')
for one_news_a in news_a:
    # print(one_news_a)
    href = one_news_a.get('href')
    text = one_news_a.find('div', class_="b_ear-title").text
    text = text.replace('\n', '')
    text = text.replace('\xa0', ' ')

    # print(text)
    # шаг 2
    url = f'{domain}{href}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # получаем заголовки
    news_titles_tag = soup.find_all('h1', class_='headline')
    news_subhead_tag = soup.find_all('h2', class_='subheader')
    news_textbig = soup.find('div', class_='b_article-text').text
    print(news_textbig)
    time = soup.find('time', class_='time').text
    time = time.replace('\n', '')
    # print(news_titles_tag)
    # print(news_titles_tag)
    # print(news_subhead_tag)
    titles = []
    # text = news_titles_tag
    for title_tag in news_subhead_tag:
        # print(time.text)
        # print(title_tag.text)
        titles.append(time)
        titles.append(title_tag.text)
        titles.append(f'{domain}{href}')
        titles.append(news_textbig)
    # добавим в словарь
    result[text] = titles
print(result)
with open('data.json', 'w') as outfile:
    json.dump(result, outfile)
