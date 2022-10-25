from bs4 import BeautifulSoup as bs
import csv

def description(details):
    try:
        for i,p in enumerate(details):
            if(i == 0):
                describe = p.contents[4].strip('\t\n')
                tags_list = p.find_all('span')
                tag = [tags_list[i].text for i in range(len(tags_list))]
                tags = " ".join(tag)

            if (i == 1):
                location = p.contents[4].strip(",\t\n")
                num_of_employee = p.contents[6].text.strip("employees")
                found_year = p.contents[8].text.strip("Founded: ")
                print(f"{location}\n{num_of_employee}\n{found_year}")

            if (i == 3):
                linkedIn = p.contents[4]['href']
                website = p.contents[10]['href']
                reviews = p.contents[7]['href']

        detail_list = [describe, tags, location, num_of_employee, found_year, website, linkedIn, reviews]
        
        return detail_list

    except Exception as e:
        print(e)

def log(company, detail_list):
    try:
        tech = detail_list[1]
        location = detail_list[2]
        employee = detail_list[3]
        found = detail_list[4]
        website = detail_list[5]
        linkedin = detail_list[6]
        reviews = detail_list[7]
        
        # enclose data containing commas in double quotes to avoid error
        with open('AI-Startups.csv', 'a', encoding="utf-8") as filename:
           filename.write(f'{company},"{detail_list[0]}",{tech},"{location}",{employee},{found},{website},{linkedin},"{reviews}",\n')
    
    except Exception as e:
        print(e)

    


    
  




        