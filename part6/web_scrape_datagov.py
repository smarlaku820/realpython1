import re
from urllib.request import urlopen, Request

req = Request("https://www.data.gov/", headers={'User-Agent': 'Mozilla/5.0'})
html_page = urlopen(req)

#print(html_page.read())
html_text = html_page.read().decode('utf-8')


for tag in ["Search over .*?datasets"]:
    match_results = re.search(tag, html_text)
    print(match_results.group())
    result = re.sub("Search over <.*?>","",match_results.group()).strip(" datasets")
    print(result)

for tag in ['<span>.*?</span>']:
    match_results = re.findall(tag, html_text, re.MULTILINE)
    for text in match_results:
        print(re.sub("span","",text).strip("<>").strip("</"))
    #print(match_results.group() if match_results is not None else match_results)
