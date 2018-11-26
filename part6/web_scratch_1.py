from urllib.request import  urlopen

my_address="https://wiki.python.org/moin/PostgreSQL"
html_page = urlopen(my_address)
html_text = html_page.read().decode('utf-8')
start_idx = html_text.find('<title>') + len('<title>')
end_idx = html_text.find('</title>')
print(html_text[start_idx:end_idx])