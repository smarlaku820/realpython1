from urllib.request import  urlopen, Request
import re

req = Request('https://realpython.com/practice/dionysus.html', headers={'User-Agent': 'Mozilla/5.0'})
html_page = urlopen(req)
html_text = html_page.read().decode('utf-8')

# get the "Name" and "Favourite Color" using regular expressions
for tag in ["Name: .*?[\n<]", "Favorite Color: .*?[\n<]"]:
    match_results = re.search(tag, html_text)
    result = re.sub(".*?:","",match_results.group()).strip("\n<")
    print(result)