import requests
from bs4 import BeautifulSoup
import subprocess
import time
import sys
import os
import json


def getBannerImage():
    banner_location = "/home/victor/project/web-scrapers/banner"

    for url in urlList:
        url = f"https://www.taylorstitch.com/collections/{url}"
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        collections = soup.find("div", class_="banner")
        links = collections.img["data-srcset"].split(" ")
        link = f'https:{links[len(links) - 2]}'.split("?")[0]
        print(link)
        cmd = ["wget", '-P', banner_location, link]
        subprocess.run(cmd)


def getImages(filename):
    location = f"/home/victor/project/web-scrapers/{filename.replace('.html', '')}"
    print(location)

    folder = open(f"html_pages/{filename}", "r")

    soup = BeautifulSoup(folder, "lxml")
    product_matrix = soup.find('ul', class_="matrix")
    product_list = product_matrix.find_all('li')
    count = 0

    for product in product_list:
        try:
            image1 = product.find("img", class_="feature")
            image2 = product.find("img", class_="swap")
            images = [image1, image2]
            for image in images:
                img1_links = image["data-srcset"].split(" ")
                links = list(filter(None, img1_links))
                for link in links:
                    if ("530x" in link):
                        link = f'https:{link}'.split("?")[0]
                        print(link)
                        cmd = ["wget", '-P', location, link]
                        subprocess.run(cmd)
                        count += 1
                        break
        except Exception as e:
            print(e)

        print("\n \n")

    print(count)


def createJson(filename):
    fcount = 0
    scount = 1
    count = 1

    # reading the images from each folders
    folder_name = filename.replace('.html', "")
    location = f"/home/victor/project/web-scrapers/{folder_name}"
    location_files = sorted(os.listdir(location))

    # reading the html files
    folder = open(f"html_pages/{filename}", "r")
    soup = BeautifulSoup(folder, "lxml")
    product_matrix = soup.find('ul', class_="matrix")
    product_list = product_matrix.find_all('li')

    # output file
    jsonOuput = open(f"{folder_name}.json", "a")
    jsonOuput.write("{ ")

    for product in product_list:
        if (product.figure):
            try:
                title = product.find("span", class_="title").text.strip()
                subtitle = product.find(
                    "span", class_="subtitle").text.strip(" \n\t")
                price = product.find("span", class_="igPrice").text

                image_href = f"/ProductAssets/{folder_name}/{location_files[fcount]}"
                image_hover_href = f"/ProductAssets/{folder_name}/{location_files[scount]}"

                finalJson = {
                    f"id": count,
                    f"src": image_href,
                    f"src2": image_hover_href,
                    f"title": title,
                    f"subtitle": subtitle,
                    f"price": price
                }

                jsonOuput.write(f"{json.dumps(finalJson)},")
                print(finalJson, "\n\n")

                if (len(location_files) <= fcount or len(location_files) <= scount):
                    break
                fcount += 2
                scount += 2
                count += 1

            except Exception as e:
                print(e)

    jsonOuput.write("}")
    jsonOuput.close()


urlList = ["mens-shirts", "mens-knits", "mens-sweaters", "mens-bottoms",
           "mens-denim", "mens-outerwear", "mens-footwear", "mens-accessories"]

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}


folder = "/home/victor/project/web-scrapers/ecommerce/html_pages"
files = os.listdir(folder)
for filename in files:
    createJson(filename)
