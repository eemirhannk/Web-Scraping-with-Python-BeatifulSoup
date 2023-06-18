from itertools import product
from pickle import FALSE
import random
from xml.sax.xmlreader import AttributesImpl 
import numpy as np
import requests
import sqlite3
from bs4 import BeautifulSoup
conn = None
try:    
    conn = sqlite3.connect("db.sqlite3")
    print('Baglanti Basarli')
except Exception as e:
    print(e)

# tdetails = teknik detaylar
# div[href] = bilgisayarların linki 
pages=np.arange(1,3,1)
liste = []
for r in pages:
     r=requests.get("https://www.trendyol.com/laptop-x-c103108?pi=" + str(r))
     soup=BeautifulSoup(r.content,"html.parser")
     products=soup.find_all(["div","a"],attrs={"class":"p-card-wrppr"})
     headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117"}
     for div in products:
           puan = random.uniform(3.0, 5.0)
           puan=round(puan,1)
           div=div.find("a")

           flink = "https://www.trendyol.com/"

           link = flink+div["href"]
           ptitle=div.find("span",attrs={"class":"prdct-desc-cntnr-ttl"})

           print(" ")
           print(ptitle.get_text())
           
           a=div.find("span",attrs={"class":"prdct-desc-cntnr-name"})

           price=div.find("div",attrs={"class":"prc-box-dscntd"})

        
     #print(link)
     #print(" ")

           detail = requests.get(link,headers=headers)

           detail_soup = BeautifulSoup(detail.content,"html.parser")

           tdetails = detail_soup.find_all("ul",attrs={"class":"detail-attr-container"})

           name = detail_soup.find_all("h1",attrs={"class":"pr-new-br"})


           for technic in tdetails:

             details = technic.find_all("li",attrs={"class":"detail-attr-item"})
             print(" ")
             print("------------------------------------------")
             print("Site İsmi  ===  Trendyol")
             print("Ürün Linki  ===  "+link)
             print("Marka  ===  "+ptitle.get_text())

             liste.append([ptitle.get_text()])

             try:
               
               print("Model  ===  "+a.get_text())
               liste.append([a.get_text()])
               print("Ürün Puanı  ===  "+str(puan))
               liste.append([puan])
             except:

               print("0")

             try:

                 print("Fiyat  ===  "+price.get_text())
                 liste.append([price.get_text()])

             except:

                 print("0") 

             for i in details:

                cart = i.find("span").text
                curt = i.find("b").text
                #if(cart == "İşlemci Tipi" and ptitle.get_text() != "Apple"):
                    #tip = curt.split(" ")
                    #tip = tip[2]
                    #print("İşlemci Tipi  ===  "+tip)


                if(cart == "İşlemci Tipi" or cart == "SSD Kapasitesi" or cart == "İşletim Sistemi" or cart == "Ekran Kartı" or cart == "Ram (Sistem Belleği)"  or cart == "Ekran Boyutu"):
                    if(cart == "İşlemci Tipi"):
                        cart = "İşlemci"
                    elif(cart == "SSD Kapasitesi"):
                        cart = "Disk Boyutu"
                    elif(cart == "Ram (Sistem Belleği)"):
                        cart = "Ram"
                    liste.append([cart,curt])

                    print(cart + "  ===  " + curt)
                else:

                  exit
     


     #print(detail)
     print(" ")
     print(" ")
print(liste)
print(len(liste))


sql = ''' INSERT INTO notebook_notebook (marka, resim, model, modelNo, isletimSistemi, islemciTipi, ram, diskBoyutu, diskTuru, ekranBoyutu, fiyat, urunLink, urunSite, islemciNesli, puan)
                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

"""      
0,12,24
1,13,25
2,14,26
""" 
print('Liste ici donguye giriyorum')
sayac = 0
flag = False
for item in liste:

    if flag:
        print('VeriTabanina atma islemine girdim')
        conn = None
        try:    
            conn = sqlite3.connect("db.sqlite3")
            print('Baglanti Basarli')
        except Exception as e:
            print(e)
        degerler = (marka,'',ptitle,'',os,islemci,ram,disk_boyutu,'',inc,fiyat,link,"Trendyol",'',str(puan))
        cur = conn.cursor()
        cur.execute(sql, degerler)
        conn.commit()
        flag = False

    if sayac % 12 == 0:
        marka = item[0]
        print(marka)
        sayac = 1 + sayac
        continue

    if sayac % 12 == 1:
        ptitle = item[0]
        print(ptitle)
        sayac = 1 + sayac
        continue

    if sayac % 12 == 2:
        puan = item[0]
        print(puan)
        sayac = 1 + sayac
        continue

    if sayac % 12 == 3:
        fiyat = item[0]
        print(fiyat)
        print('sayac % 12 == 3')
        sayac = 1 + sayac
        continue

    if sayac % 12 == 4:
        islemci = item[1]
        print(islemci)
        sayac = 1 + sayac
        continue

    if sayac % 12 == 5:
        disk_boyutu = item[1]
        print(disk_boyutu)
        sayac = 1 + sayac
        continue

    if sayac % 12 == 6:
        os = item[1]
        print(os)
        sayac = 1 + sayac
        continue

    if sayac % 12 == 7:
        ram = item[1]
        print(ram)
        sayac = 1 + sayac
        continue

    if sayac % 12 == 8:
        ekran_karti = item[1]
        print(ekran_karti)
        sayac = 1 + sayac
        continue

    if sayac % 12 == 9:
        inc = item[1]
        print(inc)
        flag = True
        sayac = 1 + sayac
        continue