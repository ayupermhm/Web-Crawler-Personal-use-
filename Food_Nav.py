from requests_html import HTMLSession
import pandas as pd
import time
import datetime

##DO NOT CHANGE##
s = HTMLSession()
links_list = []

def request(url):
    r= s.get(url)
    r.html.render(sleep=1) #gives 1 second break after rendering - security measures can change accordingly 
    #print(r.status_code) #check if render gives you a status code, you may remove the hashtag to test if device can run
    return r.html.xpath('//*[contains(@class,"search-results")]', first = True) #just in case other elements have same name first = True must be inside
     #obtain xpath from inspect on chrome, use the xpath of search results --reminder to explain 

def parse(products):
    list_links = products.absolute_links
    for item in list_links:
        #print(item) #print individual links in a list
        r = s.get(item)
        article_name = r.html.find('h1.Detail-title', first = True).text
        article_author = r.html.find('a.Detail-author', first = True).text
        article_date_published = r.html.find('p.Detail-date', first = True).text
        article_summary = r.html.find('div.Detail-intro', first = True).text

        summary = {
            'Name': article_name,
            'Author': article_author,
            'Date Published': article_date_published,
            'Article Summary': article_summary,
            'Link': item
        }
        links_list.append(summary)
        #print(summary)
        
def output():
    df = pd.DataFrame(links_list)
    df.to_csv('pf1.csv', index = False) #change file name accordingly, do not remove the .csv
    print('Saved to CSV')

def generate_search_link(search_terms, start_date, end_date):
    base_url = 'https://www.foodnavigator-asia.com/search?q={query}&t=all&p=1&sd={sd}&ed={ed}&ob=date&range_date=custom_dates'
    query = "%20".join(search_terms)
    start_date = int(time.mktime(start_date.timetuple()))
    end_date = int(time.mktime(end_date.timetuple()))
    link = base_url.format(query = query, sd = start_date, ed = end_date)
    print(link)
    return link

x = 1
search_terms = ["precision", "fermentation"] #change words according to what you want to search
start_date = datetime.datetime(2023, 10, 1, 1, 00) #Year, Month,Day ,Hour ,Min -> only change year month date
end_date = datetime.datetime(2023, 11, 3, 1, 00) #Year, Month,Day ,Hour ,Min -> only change year month date

while True:
    try:
        products = request(generate_search_link(search_terms, start_date, end_date)) #insert the link that you want to view, shift the x accordingly 
        print(f'Getting links from page {x}')
        parse(products)
        print('Total Items: ', len(links_list))
        x = x+1
        time.sleep(2)

        if x == 1 or len(links_list) == 0: #Change the maximum number of pages accordingly 
            break

    except: 
        print('No more links')
        break
output()