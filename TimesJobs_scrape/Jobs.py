from bs4 import BeautifulSoup
import requests
import time
import sys


url = sys.argv[1]
with open(url,"r") as urlfile:
    urlval = urlfile.readlines()

for val in urlval:
    print(val)
    print(val.strip("\n"))
    print("put some skill that you are not familiar with")
    unfamiliar_skills = input('>')
    print(f'filtering out {unfamiliar_skills}')
    unfamList = unfamiliar_skills.split()
    print(unfamList)

    def find_jobs():
        html_text = requests.get(f'{val}').text        # its like opening a website by a human
        soup = BeautifulSoup(html_text,'lxml')        # reading the html page
        # print(soup)

        rows = 0
        jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')

        for job in jobs:
            job_pub_date = job.find('span',class_='sim-posted').span.text

            if 'few' in job_pub_date:
                company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
                skills = job.find('span',class_='srp-skills').text.replace(' ','')
                more_info = job.header.h2.a['href']
                if unfamiliar_skills not in skills:
                    rows = rows + 1
                    print(f"company name: {company_name.strip()}")
                    print(f"Required Skills: {skills.strip()}")
                    print(f"more info: {more_info}")

                    print('')
        print(rows)

    find_jobs()
    # if __name__ == '--main__':
    #     while True:
    #         find_jobs()
    #         time.sleep()