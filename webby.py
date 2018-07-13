# requests info from web page
import requests
# this module gets data from website
from bs4 import BeautifulSoup


def spider(max_page):
    page = 1
    while page <= max_page:
        url = "https://www.flipkart.com/search?q=hp+laptops&sid=6bo%2Fb5g&as=on&as-show=on&marketplace=FLIPKART&otracker=start&as-pos=1_2_ic_hp+laptops&" + str(
            page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.find_all('a', {'class': '_31qSD5'}):
            href = "https://www.flipkart.com"+link.get('href')
            title=link.string
            print(title)
            print(href)

            page += 1


def spider_item(item_url):

    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.find_all('div',{'class':'_3iZgFn'}):
        print(item_name.string)

spider(3)
