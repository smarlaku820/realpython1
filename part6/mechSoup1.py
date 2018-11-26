import mechanicalsoup
my_browser = mechanicalsoup.Browser()
page = my_browser.get("https://realpython.com/practice/login.php")
print(page.soup)
