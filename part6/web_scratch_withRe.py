from urllib.request import  urlopen
import re

my_address="https://wiki.python.org/moin/PostgreSQL"
html_page = urlopen(my_address)
html_text = html_page.read().decode('utf-8')
match_results=re.search('<title.*?>.*</title.*?>', html_text, re.IGNORECASE)
print(match_results.group())
title = re.sub("<.*?>", "" , match_results.group())
print(title)

