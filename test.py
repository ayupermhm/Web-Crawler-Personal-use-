#Tester file. DO NOT RUN

import datetime
import time

date_time = datetime.datetime(2021, 7, 26, 21, 20)
unix_timestamp = time.mktime(date_time.timetuple())

print(unix_timestamp)

def generate_search_link(words, start_date, end_date):
    base_url = "https://www.foodnavigator-asia.com/search?q={query}&t=all&p=1&sd={sd}&ed={ed}&ob=date&range_date=this_year"
    query = " ".join(words)
    link = base_url.format(query=query, sd=start_date, ed=end_date)
    return link

# Example usage:
words = ["apple", "banana", "cherry", "date"]
start_date = "2023-01-01"
end_date = "2023-12-31"

search_link = generate_search_link(words, start_date, end_date)
print(search_link)
