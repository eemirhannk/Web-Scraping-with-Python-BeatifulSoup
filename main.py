from itertools import product
import random
from xml.sax.xmlreader import AttributesImpl 
import numpy as np
import requests
from bs4 import BeautifulSoup

pages=np.arange(1,2,1)

for r in pages:
     r=requests.get("http://127.0.0.1:8000/notebook")
     soup=BeautifulSoup(r.content,"html.parser")
     products=soup.find_all(["div"],attrs={"class":"col-4"})
     #print(products)
     headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117"}
     liste = []

     for div in products:
        
           emir=div.find("a")
           #print(div)

           flink = "http://127.0.0.1:8000"

           link = flink+emir["href"]
           print("Site : notebookcu".strip())
           print("Ürün Linki : "+link.strip())

           for ozo in div:


            ptitle=ozo.find("h5")
            pdetails=ozo.find("p")

            try:
                print("Ürün Adı : "+ptitle.get_text().strip())
            except:
                print(" ")
            try:
               print(pdetails.get_text().strip())
            except:
                print(" ")
