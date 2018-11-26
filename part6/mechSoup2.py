import mechanicalsoup
my_browser = mechanicalsoup.Browser()
login_page = my_browser.get("https://realpython.com/practice/login.php")
login_html = login_page.soup

# select the form and fill in its fields.
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = my_browser.submit(form, login_page.url) #submit_form

print(profiles_page.url) # make sure we were redirected
print(profiles_page.soup) # shows html