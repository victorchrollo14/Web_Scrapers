from pickle import NONE
import requests
from bs4 import BeautifulSoup as bs
import re

from helpers import description,log


URL = "https://topstartups.io/?industries=Artificial+Intelligence&sort=valuation"

with open('AI-Startups.csv', 'a') as filename:
    filename.write(f"company_name, Description, Technology, Location, No_of_Employees, Founded, website, linkedIn, reviews\n")

try: 
    def main_scrape(url):
        response = requests.get(url).text
        soup = bs(response, "lxml")
        company_list = soup.find_all("div", class_ = ["col-md-6"])
        
        for company in company_list:
            comp_name = company.div.div.contents[3].a.text.strip()
            details = company.find_all('p')

            detail_list = description(details)
            log(comp_name,detail_list)
        newurl = soup.find('a', class_= "infinite-more-link")
        if (newurl is not None):
            new_url = newurl['href']
            new_url = f"https://topstartups.io/{new_url}"
            main_scrape(new_url)

except Exception as e:
    print(e)

if __name__ == "__main__":
    main_scrape(URL)
        
    

