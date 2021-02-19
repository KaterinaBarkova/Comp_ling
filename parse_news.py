from bs4 import BeautifulSoup
import requests

url = "https://upravadorogomilovo.ru/news"

amount = 0
_links = []
for i in range(7):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')
    for links in soup.find_all('a', 'read-more-button'):
        _links.append(links.get('href'))
        amount = amount + 1
    
    _next = soup.find('a', 'next')
    url = "https://upravadorogomilovo.ru/" + _next.get('href')
    
print(amount)
with open("Дорогомилово.txt", "w", encoding="utf-8") as f:
    for link in _links:
        f.write(link + "\n") 


with open("Дорогомилово.txt", "r", encoding="utf-8") as f:
    links = f.readlines()

amount = 0
for link in links:
    html = requests.get(link[:-1]).text
    soup = BeautifulSoup(html, 'html5lib')
    div = soup.find('div', 'entry-content')
    with open("news/Dorogomilovo" + str(amount) + ".txt", "w", encoding="utf-8") as f:
        for p in div.find_all('p'):
            f.write(p.text + "\n")
    amount += 1