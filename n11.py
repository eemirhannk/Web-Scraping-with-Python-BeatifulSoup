from itertools import product
import random
from xml.sax.xmlreader import AttributesImpl 
import numpy as np
import requests
from bs4 import BeautifulSoup

pages=np.arange(1,20,1)
liste = []
for r in pages:

    r = requests.get("https://www.n11.com/bilgisayar/dizustu-bilgisayar")
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117"}
    soup = BeautifulSoup(r.content,"html.parser")
    products = soup.find_all("li",attrs={"class":"column"})
    for product in products:
          puan = random.uniform(3.0, 5.0)
          puan=round(puan,1)
          productlinks = product.find_all("div",attrs={"class":"columnContent"})
          for i in productlinks:
                link = i.find("div",attrs={"class":"pro"})
                link_full = link.a.get("href")
                
                ptitle = product.find("h3",attrs={"class":"productName"})
                numan = ptitle.get_text().split()
                #print(numan)
                pPrice = product.find("span",attrs={"class":"newPrice"})

                detail = requests.get(link_full,headers=headers)
                detail_soup = BeautifulSoup(detail.content,"html.parser")

                teknik = detail_soup.find_all("ul",attrs={"class":"unf-prop-list"})
                for tek in teknik:
                      print("Site İsmi  ===  n11")
                      print("Ürün Linki  ===  "+link_full)
                      print("Marka  ===  "+numan[0])
                      liste.append([numan[0]])
                      print("Fiyat  ===  "+pPrice.get_text().strip())
                      liste.append([pPrice.get_text().strip()])
                      print("Ürün Puanı  ===  "+str(puan))
                      liste.append([str(puan)])
                      detaylar = tek.find_all("li",attrs={"class":"unf-prop-list-item"})
                      for i in detaylar:
                            etiket = i.find("p",attrs={"class":"unf-prop-list-title"})
                            deger = i.find("p",attrs={"class":"unf-prop-list-prop"})
                            if(str(etiket.get_text()) == "İşlemci Modeli"):
                              try:

                                nesil = str(deger.get_text()).split("-")
                                nesil = nesil[1]
                                islemci_nesli = nesil[:2]
                              except:
                                nesil = nesil

                            if(str(etiket.get_text()) == "İşlemci" or (str(etiket.get_text())) == "Disk Kapasitesi" or (str(etiket.get_text())) == "İşletim Sistemi" or (str(etiket.get_text())) == "Bellek Kapasitesi" or (str(etiket.get_text())) == "Ram (Sistem Belleği)" or (str(etiket.get_text())) == "Ekran Kartı Modeli" or (str(etiket.get_text())) == "Ekran Boyutu" or str(etiket.get_text()) == "Disk Türü"):

                                if((str(etiket.get_text())) == "Bellek Kapasitesi"):
                                  etiket = "Ram"
                                elif((str(etiket.get_text())) == "Ekran Kartı Modeli"):
                                  etiket = "Ekran Kartı"
                                elif((str(etiket.get_text())) == "Disk Kapasitesi"):
                                  etiket = "Disk Boyutu"
                                try:
                                  print(etiket + " === " + str(deger.get_text()))
                                except:
                                  print(str(etiket.get_text()) + " === " +str(deger.get_text()))
                                try:
                                  liste.append([str(etiket.get_text()),str(deger.get_text())])
                                except:
                                  try:
                                    kaka = etiket.get_text()
                                  except:
                                    kaka = str(etiket)
                                  try:
                                    koko = deger.get_text()
                                  except:
                                    koko = str(deger)
                                  liste.append([kaka,koko])
                print("İşlemci Nesli  ===  "+islemci_nesli)
                liste.append([islemci_nesli])                  
                print("------------------------------------")
                print(" ")
print(liste)
print(len(liste))
                


