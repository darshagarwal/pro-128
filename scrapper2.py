from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
 
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("D:/coding/cl127/chromedriver")
browser.get(START_URL)
time.sleep(10)
headers = ['Star','Constellation','Right ascension','Declination','App. mag.','Distance (ly)','Spectral type','Brown dwarf','Mass (MJ)','Radius(RJ)','Orbital period (d)','Semimajor axis(AU)','Ecc.','Discovery year']
planet_data = []
new_planet_data=[]

def scrape():
    soup = BeautifulSoup(browser.page_source,"html.parser")
    table_tag=soup.find_all("table")
    print("table",len(table_tag))
    tr_tags = table_tag[4].find_all("tr")
    print("tr",len(tr_tags))
    temp_list=[]
    for i in tr_tags:
        td=i.find_all('td')
        row=[j.text.rstrip() for j in td]
        temp_list.append(row)
    print("td:",len(td))

    print(temp_list[0])

with open("final.csv","w") as f:
        csv_write = csv.writer(f)
        csv_write.writerow(headers)


scrape()