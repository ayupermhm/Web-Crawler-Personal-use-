#TEST FILE DO NOT RUN
from requests_html import HTMLSession

url = "https://www.foodnavigator-asia.com/search?q=popping%20candy&t=all&p=1&ob=date&range_date=date"

s = HTMLSession()
r = s.get(url)

r.html.render(sleep =1)

products = r.html.xpath('//*[contains(@class,"search-results")]', first = True)

for item in products.absolute_links:
    r = s.get(item)
    article_name = r.html.find('h1.Detail-title', first = True).text
    article_author = r.html.find('a.Detail-author', first = True).text
    article_date_published = r.html.find('p.Detail-date', first = True).text
    article_summary = r.html.find('div.Detail-intro', first = True).text
