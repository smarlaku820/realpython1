from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

req = Request('https://realpython.com/practice/dionysus.html', headers={'User-Agent': 'Mozilla/5.0'})
html_page = urlopen(req)
html_text = html_page.read().decode('utf-8')

my_soup = BeautifulSoup(html_text, features="html.parser")
print(my_soup.get_text().replace("\n"," "))