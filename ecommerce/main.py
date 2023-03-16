import requests
from bs4 import BeautifulSoup
import subprocess
import time
import sys


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
    shirt_location = "/home/victor/project/web-scrapers/shirts"

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
                        count += 1
                        break
        except Exception as e:
            print(e)

        print("\n \n")

    print(count)


urlList = ["mens-shirts", "mens-knits", "mens-sweaters", "mens-bottoms",
           "mens-denim", "mens-outerwear", "mens-footwear", "mens-accessories"]
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

filename = sys.argv[1]
getImages(filename)
