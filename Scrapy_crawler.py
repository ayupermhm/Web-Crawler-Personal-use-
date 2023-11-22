'''
Crawler - a scrapy script that crawls these sites with all their subpages (that's the easiest part) and transforms them into plain text
NLP Processing - some basic NLP (natural language) processing (tokenizing, part of speech (POS) tagging, named entity-recognition (NER)) on the plain text
Classification - a classifier that can use the data from step 2 to decide whether a page contains the data we're looking for - either simple rules based or - if needed - using machine learning. Those pages that are suspected to contain any usable data will be put into the next step:
Extraction - an grammar-based, statistical or machine learning based extractor that uses POS-tags and NER-tags (and any other domain specific factors) to extract that data we're looking for
Clean up - some basic matching of duplicate records that were created in step 4 and maybe it's also necessary to throw away records that had low confidence scores in steps 2 to 4.
'''


import csv
import time
import asyncio
import aiohttp #Understand problem with aiohttp

async def scrape(url):
    async with aiohttp.ClientSession() as Session:
        async with 

async def main():
    start_time = time.time()

    tasks = []
    with open('link_bank.csv') as file:
        csv_reader = csv.DictReader(file)
        for csv_row in csv_reader:
            #print(csv_row['url'])
            task = asyncio.create_task(scrape(csv_row['url']))
            tasks.append(task)

    print('Saving the output of extracted information')

    time_difference = time.time() - start_time
    print(f'Scraping time: %.2f seconds.' % time_difference)

loop =asyncio.get_event_loop()
loop.run_until_complete(main())