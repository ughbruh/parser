 from bs4 import BeautifulSoup
import requests

product = input()
url = "https://www.avito.ru/samarskaya_oblast?q=" + product 
request = requests.get(url)
bs = BeautifulSoup(request.text, "html.parser")

all_links = bs.find_all("a", class_="title-root-zZCwT")

for link in all_links:
  print(link["href"])