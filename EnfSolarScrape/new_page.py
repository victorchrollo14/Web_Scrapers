from bs4 import BeautifulSoup
import requests

def newpageScrape(link):
    new_content = requests.get(f"{link}").text
    soup = BeautifulSoup(new_content,'lxml')
    
    content_req = soup.find('div',class_ = 'enf-company-profile-info-main-spec')
    details_GI = content_req.find_all('table')

    address = details_GI[0].tr.contents[3].text.strip()
    website = details_GI[3].tr.contents[3].a.text.strip()
    country = details_GI[4].tr.contents[3].text.strip()
    # print(f"{address}\n{website}\n{country}")

    bisnes_det = soup.find_all('div',class_ = 'enf-section-body-title')
    bisnes_cnt  = soup.find_all('div',class_ = 'col-xs-10')
   
    prdt = {}
    for i,(det,cnt) in enumerate(zip(bisnes_det,bisnes_cnt)):
         if(det.text.strip() != "Established Date"):
            prdt[det.text.strip()] = cnt.text.strip()
    

    new_val = list(prdt.items())
    # print(len(new_val))
    serv_cov = new_val[0][1]
    Lang_spkn = new_val[1][1] 
    item1 = new_val[2][0]
    item1_des = new_val[2][1]
    
    item2 = item2_des = item3 = item3_des = item4 = item4_des = item5 = item5_des = item6 = item6_des = ''

    if(len(new_val) > 3):
        item2 = new_val[3][0]
        item2_des = new_val[3][1]
    if(len(new_val) > 4):
        item3 = new_val[4][0]
        item3_des = new_val[4][1]
    if(len(new_val) > 5):
        item4 = new_val[5][0]
        item4_des = new_val[5][1]
    if(len(new_val) > 6):
        item5 = new_val[6][0]
        item5_des = new_val[6][1]
    if(len(new_val) > 7):
        item6 = new_val[7][0]
        item6_des = new_val[7][1]
   
    final_output = [address,website,country,serv_cov,Lang_spkn,item1,item1_des,item2,item2_des,item3,item3_des,item4,item4_des,item5,item5_des,item6,item6_des]

    return final_output

def data_ouput():
    pass