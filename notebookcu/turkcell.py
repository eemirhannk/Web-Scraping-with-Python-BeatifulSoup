from itertools import product
from os import link
import random
from xml.sax.xmlreader import AttributesImpl 
import numpy as np
import requests
import sqlite3
from bs4 import BeautifulSoup

pages=np.arange(1,3,1)
liste = []
for r in pages:

    r = requests.get("https://m.turkcell.com.tr/pasaj/bilgisayar-tablet/bilgisayarlar/laptoplar")
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117"}
    soup = BeautifulSoup(r.content,"html.parser")
    products = soup.find_all("div",attrs={"class":"m-grid-col-4"})
    #print(products)
    for div in products:
        puan = random.uniform(3.0, 5.0)
        puan=round(puan,1)
        front_link = "https://m.turkcell.com.tr"
    
        div=div.find("a")
        link = front_link + div["href"]
    
        #print(link)

        detay = requests.get(link,headers=headers)
        #print(detay)
        detay_soup = BeautifulSoup(detay.content,"html.parser")
        #print(detay_soup)
        teknik_ayrıntılar = detay_soup.find_all("div",attrs={"class":"m-product-detail-features__container"})
        #print(teknik_ayrıntılar)
        for teknik in teknik_ayrıntılar:
            ozellikler = teknik.find_all("div",attrs={"class":"m-product-detail-features__wrap"})
            #print(ozellikler)
            for i in ozellikler:
                #cart özelliğin başlığı(işlemci tipi vb.)
                #curt özelliğin texti(intel i5,16gb ram vb.)
                cart = i.find("div",attrs={"class":"m-product-detail-features__title"})
                curt = i.find("div",attrs={"class":"m-product-detail-features__text"})
                if(cart.get_text() == "Marka" or cart.get_text() == "Ekran Boyutu" or cart.get_text() == "İşlemci Modeli (cpu)" or cart.get_text() == "İşlemci Markası (cpu)" or cart.get_text() == "Sabit Disk Ssd Boyutu" or cart.get_text() == "Bellek Ram" or cart.get_text() == "İşletim Sistemi" or cart.get_text() == "Ürün Model Adı"):
                    print(cart.get_text() + "  ===  "+curt.get_text())
                    liste.append([curt.get_text()])
            print("Ürün Puanı  ===  "+str(puan))            
        print("----------------------")
print(liste)


sql = ''' INSERT INTO notebook_notebook (marka, resim, model, modelNo, isletimSistemi, islemciTipi, ram, diskBoyutu, diskTuru, ekranBoyutu, fiyat, urunLink, urunSite, islemciNesli, puan)
                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
sayac = 0
flag = False
for item in liste:
    
    if flag and marka != "ASUS":
        print('VeriTabanina atma islemine girdim')
        conn = None
        try:    
            conn = sqlite3.connect("db.sqlite3")
            print('Baglanti Basarli')
        except Exception as e:
            print(e)
        degerler = (marka,'',ptitle,'',os,islemci,ram,disk_boyutu,'',inc,'',link,"Trendyol",'',str(puan))
        cur = conn.cursor()
        cur.execute(sql, degerler)
        conn.commit()
        flag = False

    if sayac % 8 == 0:
        ptitle = item[0]
        sayac = 1 + sayac
        continue


    if sayac % 8 == 1:
        os = item[0]
        sayac = 1 + sayac
        continue

    if sayac % 8 == 2:
        ram = item[0]
        sayac = 1 + sayac
        continue

    if sayac % 8 == 3:
        disk_boyutu = item[0]
        sayac = 1 + sayac
        continue

    if sayac % 8 == 4:
        islemci = item[0]
        sayac = 1 + sayac
        continue

    if sayac % 8 == 5:
        sayac = 1 + sayac
        continue

    if sayac % 8 == 6:
        inc = item[0]
        sayac = 1 + sayac
        continue

    if sayac % 8 == 7:
        marka = item[0]
        sayac = 1 + sayac
        flag = True
        continue