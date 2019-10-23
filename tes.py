import requests
from parsel import Selector

import time
start = time.time()

### Crawling to the website

# GET request to recurship site
response = requests.get('https://news.detik.com/indeks/all?date=09%2F28%2F2019')

## Setup for scrapping tool

# "response.txt" contain all web page content
selector = Selector(response.text)

# Extracting href attribute from anchor tag <a href="*">
href_links = selector.xpath('//a/@href').getall()


#Extracting src attribute from img tag <img src="*">
image_links = selector.xpath('//img/@src').getall()

print('*****************************href_links************************************')
for x in href_links:
    print(x)
print('*****************************/href_links************************************')



print('*****************************image_links************************************')
print(image_links)
print('*****************************/image_links************************************')



end = time.time()
print("Time taken in seconds : ", (end-start))