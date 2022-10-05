from itertools import count
from bs4 import BeautifulSoup
import requests
from new_page import newpageScrape


url = "https://www.enfsolar.com/directory/seller/Austria"

html_content = requests.get(f"{url}").text
soup = BeautifulSoup(html_content,'lxml')

needed_content = soup.find('table',class_ = 'enf-list-table')
table = needed_content.find_all('tr')

for i,row in enumerate(table):
    company_name = row.contents[1].a.text.strip()
    Area = row.contents[7].text.strip()
    seller_type = row.contents[9].find_all('img')
    sell_type = []

    for j,type in enumerate(seller_type):
         sell_type.append(type['title'])

    brands_crd = row.contents[11].text.strip()
    Min_order_val = row.contents[13].text.strip()

    products = row.contents[15].find_all('img')
    product_list = []

    for i,value in enumerate(products):
        product_list.append(value['title'])
    
    link = row.contents[1].a['href']
    extra_items = newpageScrape(link)
    
    print(company_name,Area,sell_type,brands_crd,Min_order_val,product_list)
    print(extra_items)
    print('\n_________________________________________')
    