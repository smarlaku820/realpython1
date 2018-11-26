from urllib.request import  urlopen, Request
import re

req = Request('https://realpython.com/practice/dionysus.html', headers={'User-Agent': 'Mozilla/5.0'})
html_page = urlopen(req)
html_text = html_page.read().decode('utf-8')
start_element='<h2>Name: '
s_idx = html_text.find(start_element) + len(start_element)
end_element='</h2>'
e_idx = html_text.find(end_element)
print(html_text[s_idx:e_idx])
start_element='Favorite Color: '
s_idx = html_text.find(start_element) + len(start_element)
end_element='</center>'
e_idx = html_text.find(end_element)
print(html_text[s_idx:e_idx].strip())
print("==")
#print(html_text)