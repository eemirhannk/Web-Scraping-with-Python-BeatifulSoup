import numpy as np
import requests
from bs4 import BeautifulSoup


pages=np.arange(1,2,1)

liste = []
for r in pages:
    para_indeksi = 0
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117"}
    r = requests.get("https://www.teknosa.com/laptop-notebook-c-116004")
    soup = BeautifulSoup(r.content,"html.parser")
    products = soup.find_all("div",attrs={"class":"prd"})
    #print(products)

    paralar = soup.find_all('div', {'id':'product-item'})
    for div in products:

        div=div.find("a")

        flink = "https://www.teknosa.com/"

        link = flink+div["href"]
        #print(link)

        money = paralar[para_indeksi].get('data-product-discounted-price')

        detail = requests.get(link,headers=headers)
        #print(detail)
        detail_soup = BeautifulSoup(detail.content,"html.parser")

        teknik_ayrıntılar = detail_soup.find_all("div",attrs={"class":"ptf-body"})
        #print(teknik_ayrıntılar)
        for teknik in teknik_ayrıntılar:
            price = teknik.find("span",{"class":"prc prc-last"})
            detayss = teknik.find_all("tr")
            detayss2 = teknik.find_all("tr")

            print("Site İsmi  ===  Teknosa")
            print("Ürün Linki  ===  "+link)
            print("Ürün Fiyatı  ===  "+money)
            #site özellikleri 4 lü paketler halinde tuttuğu için ilk dört ikinci dört diye ayrı ayrı çektim değişken adları onlar
            ilk_dort_ozellik_title = (detayss[0].get_text().split("\n"))
            ilk_dort_ozellik = (detayss[1].get_text().split("\n"))

            if(ilk_dort_ozellik_title[1] == "SSD Kapasitesi"):
                ilk_dort_ozellik_title[1] = "Disk Boyutu"
            elif(ilk_dort_ozellik_title[1] == "Model Kodu"):
                ilk_dort_ozellik_title[1] = "Model No"
            elif(ilk_dort_ozellik_title[1] == "İşlemci"):
                ilk_dort_ozellik_title[1] = "İşlemci Tipi"
            elif(ilk_dort_ozellik_title[1] == "İşletim Sistemi Yazılımı"):
                ilk_dort_ozellik_title[1] = "İşletim Sistemi"
            elif(ilk_dort_ozellik_title[1] == "Ekran Kartı Modeli"):
                ilk_dort_ozellik_title[1] = "Ekran Kartı"

            print(ilk_dort_ozellik_title[1]+"  ===  "+ilk_dort_ozellik[1])
            liste.append([ilk_dort_ozellik_title[1],ilk_dort_ozellik[1]])

            if(ilk_dort_ozellik_title[2] == "SSD Kapasitesi"):
                ilk_dort_ozellik_title[2] = "Disk Boyutu"
            elif(ilk_dort_ozellik_title[2] == "Model Kodu"):
                ilk_dort_ozellik_title[2] = "Model No"
            elif(ilk_dort_ozellik_title[2] == "İşlemci"):
                ilk_dort_ozellik_title[2] = "İşlemci Tipi"
            elif(ilk_dort_ozellik_title[2] == "İşletim Sistemi Yazılımı"):
                ilk_dort_ozellik_title[2] = "İşletim Sistemi"
            elif(ilk_dort_ozellik_title[2] == "Ekran Kartı Modeli"):
                ilk_dort_ozellik_title[2] = "Ekran Kartı"
            
            print(ilk_dort_ozellik_title[2]+"  ===  "+ilk_dort_ozellik[2])
            liste.append([ilk_dort_ozellik_title[2],ilk_dort_ozellik[2]])

            if(ilk_dort_ozellik_title[3] == "SSD Kapasitesi"):
                ilk_dort_ozellik_title[3] = "Disk Boyutu"
            elif(ilk_dort_ozellik_title[3] == "Model Kodu"):
                ilk_dort_ozellik_title[3] = "Model No"
            elif(ilk_dort_ozellik_title[3] == "İşlemci"):
                ilk_dort_ozellik_title[3] = "İşlemci Tipi"
            elif(ilk_dort_ozellik_title[3] == "İşletim Sistemi Yazılımı"):
                ilk_dort_ozellik_title[3] = "İşletim Sistemi"
            elif(ilk_dort_ozellik_title[3] == "Ekran Kartı Modeli"):
                ilk_dort_ozellik_title[3] = "Ekran Kartı"

            print(ilk_dort_ozellik_title[3]+"  ===  "+ilk_dort_ozellik[3])
            liste.append([ilk_dort_ozellik_title[3],ilk_dort_ozellik[3]])

            if(ilk_dort_ozellik_title[4] == "SSD Kapasitesi"):
                ilk_dort_ozellik_title[4] = "Disk Boyutu"
            elif(ilk_dort_ozellik_title[4] == "Model Kodu"):
                ilk_dort_ozellik_title[4] = "Model No"
            elif(ilk_dort_ozellik_title[4] == "İşlemci"):
                ilk_dort_ozellik_title[4] = "İşlemci Tipi"
            elif(ilk_dort_ozellik_title[4] == "İşletim Sistemi Yazılımı"):
                ilk_dort_ozellik_title[4] = "İşletim Sistemi"
            elif(ilk_dort_ozellik_title[4] == "Ekran Kartı Modeli"):
                ilk_dort_ozellik_title[4] = "Ekran Kartı"

            print(ilk_dort_ozellik_title[4]+"  ===  "+ilk_dort_ozellik[4])
            liste.append([ilk_dort_ozellik_title[4],ilk_dort_ozellik[4]])

            ikinci_dort_ozellik_title = (detayss[2].get_text().split("\n"))
            ikinci_dort_ozellik = (detayss[3].get_text().split("\n"))


            if(ikinci_dort_ozellik_title[1] == "SSD Kapasitesi"):
                ikinci_dort_ozellik_title[1] = "Disk Boyutu"
            elif(ikinci_dort_ozellik_title[1] == "Model Kodu"):
                ikinci_dort_ozellik_title[1] = "Model No"
            elif(ikinci_dort_ozellik_title[1] == "İşlemci"):
                ikinci_dort_ozellik_title[1] = "İşlemci Tipi"
            elif(ikinci_dort_ozellik_title[1] == "İşletim Sistemi Yazılımı"):
                ikinci_dort_ozellik_title[1] = "İşletim Sistemi"
            elif(ikinci_dort_ozellik_title[1] == "Ekran Kartı Modeli"):
                ikinci_dort_ozellik_title[1] = "Ekran Kartı"

            print(ikinci_dort_ozellik_title[1]+"  ===  "+ikinci_dort_ozellik[1])
            liste.append([ikinci_dort_ozellik_title[1],ikinci_dort_ozellik[1]])

            if(ikinci_dort_ozellik_title[2] == "SSD Kapasitesi"):
                ikinci_dort_ozellik_title[2] = "Disk Boyutu"
            elif(ikinci_dort_ozellik_title[2] == "Model Kodu"):
                ikinci_dort_ozellik_title[2] = "Model No"
            elif(ikinci_dort_ozellik_title[2] == "İşlemci"):
                ikinci_dort_ozellik_title[2] = "İşlemci Tipi"
            elif(ikinci_dort_ozellik_title[2] == "İşletim Sistemi Yazılımı"):
                ikinci_dort_ozellik_title[2] = "İşletim Sistemi"
            elif(ikinci_dort_ozellik_title[2] == "Ekran Kartı Modeli"):
                ikinci_dort_ozellik_title[2] = "Ekran Kartı"
            
            print(ikinci_dort_ozellik_title[2]+"  ===  "+ikinci_dort_ozellik[2])
            liste.append([ikinci_dort_ozellik_title[2],ikinci_dort_ozellik[2]])

            if(ikinci_dort_ozellik_title[3] == "SSD Kapasitesi"):
                ikinci_dort_ozellik_title[3] = "Disk Boyutu"
            elif(ikinci_dort_ozellik_title[3] == "Model Kodu"):
                ikinci_dort_ozellik_title[3] = "Model No"
            elif(ikinci_dort_ozellik_title[3] == "İşlemci"):
                ikinci_dort_ozellik_title[3] = "İşlemci Tipi"
            elif(ikinci_dort_ozellik_title[3] == "İşletim Sistemi Yazılımı"):
                ikinci_dort_ozellik_title[3] = "İşletim Sistemi"
            elif(ikinci_dort_ozellik_title[3] == "Ekran Kartı Modeli"):
                ikinci_dort_ozellik_title[3] = "Ekran Kartı"

            print(ikinci_dort_ozellik_title[3]+"  ===  "+ikinci_dort_ozellik[3])
            liste.append([ikinci_dort_ozellik_title[3],ikinci_dort_ozellik[3]])

            if(ikinci_dort_ozellik_title[4] == "SSD Kapasitesi"):
                ikinci_dort_ozellik_title[4] = "Disk Boyutu"
            elif(ikinci_dort_ozellik_title[4] == "Model Kodu"):
                ikinci_dort_ozellik_title[4] = "Model No"
            elif(ikinci_dort_ozellik_title[4] == "İşlemci"):
                ikinci_dort_ozellik_title[4] = "İşlemci Tipi"
            elif(ikinci_dort_ozellik_title[4] == "İşletim Sistemi Yazılımı"):
                ikinci_dort_ozellik_title[4] = "İşletim Sistemi"
            elif(ikinci_dort_ozellik_title[4] == "Ekran Kartı Modeli"):
                ikinci_dort_ozellik_title[4] = "Ekran Kartı"

            print(ikinci_dort_ozellik_title[4]+"  ===  "+ikinci_dort_ozellik[4])
            liste.append([ikinci_dort_ozellik_title[4],ikinci_dort_ozellik[4]])

            ucuncu_dort_ozellik_title = (detayss[4].get_text().split("\n"))
            ucuncu_dort_ozellik = (detayss[5].get_text().split("\n"))

            if(ucuncu_dort_ozellik_title[1] == "SSD Kapasitesi"):
                ucuncu_dort_ozellik_title[1] = "Disk Boyutu"
            elif(ucuncu_dort_ozellik_title[1] == "Model Kodu"):
                ucuncu_dort_ozellik_title[1] = "Model No"
            elif(ucuncu_dort_ozellik_title[1] == "İşlemci"):
                ucuncu_dort_ozellik_title[1] = "İşlemci Tipi"
            elif(ucuncu_dort_ozellik_title[1] == "İşletim Sistemi Yazılımı"):
                ucuncu_dort_ozellik_title[1] = "İşletim Sistemi"
            elif(ucuncu_dort_ozellik_title[1] == "Ekran Kartı Modeli"):
                ucuncu_dort_ozellik_title[1] = "Ekran Kartı"

            print(ucuncu_dort_ozellik_title[1]+"  ===  "+ucuncu_dort_ozellik[1])
            liste.append([ucuncu_dort_ozellik_title[1],ucuncu_dort_ozellik[1]])

            if(ucuncu_dort_ozellik_title[2] == "SSD Kapasitesi"):
                ucuncu_dort_ozellik_title[2] = "Disk Boyutu"
            elif(ucuncu_dort_ozellik_title[2] == "Model Kodu"):
                ucuncu_dort_ozellik_title[2] = "Model No"
            elif(ucuncu_dort_ozellik_title[2] == "İşlemci"):
                ucuncu_dort_ozellik_title[2] = "İşlemci Tipi"
            elif(ucuncu_dort_ozellik_title[2] == "İşletim Sistemi Yazılımı"):
                ucuncu_dort_ozellik_title[2] = "İşletim Sistemi"
            elif(ucuncu_dort_ozellik_title[2] == "Ekran Kartı Modeli"):
                ucuncu_dort_ozellik_title[2] = "Ekran Kartı"
            
            print(ucuncu_dort_ozellik_title[2]+"  ===  "+ucuncu_dort_ozellik[2])
            liste.append([ucuncu_dort_ozellik_title[2],ucuncu_dort_ozellik[2]])

            if(ucuncu_dort_ozellik_title[3] == "SSD Kapasitesi"):
                ucuncu_dort_ozellik_title[3] = "Disk Boyutu"
            elif(ucuncu_dort_ozellik_title[3] == "Model Kodu"):
                ucuncu_dort_ozellik_title[3] = "Model No"
            elif(ucuncu_dort_ozellik_title[3] == "İşlemci"):
                ucuncu_dort_ozellik_title[3] = "İşlemci Tipi"
            elif(ucuncu_dort_ozellik_title[3] == "İşletim Sistemi Yazılımı"):
                ucuncu_dort_ozellik_title[3] = "İşletim Sistemi"
            elif(ucuncu_dort_ozellik_title[3] == "Ekran Kartı Modeli"):
                ucuncu_dort_ozellik_title[3] = "Ekran Kartı"

            print(ucuncu_dort_ozellik_title[3]+"  ===  "+ucuncu_dort_ozellik[3])
            liste.append([ucuncu_dort_ozellik_title[3],ucuncu_dort_ozellik[3]])

            if(ucuncu_dort_ozellik_title[4] == "SSD Kapasitesi"):
                ucuncu_dort_ozellik_title[4] = "Disk Boyutu"
            elif(ucuncu_dort_ozellik_title[4] == "Model Kodu"):
                ucuncu_dort_ozellik_title[4] = "Model No"
            elif(ucuncu_dort_ozellik_title[4] == "İşlemci"):
                ucuncu_dort_ozellik_title[4] = "İşlemci Tipi"
            elif(ucuncu_dort_ozellik_title[4] == "İşletim Sistemi Yazılımı"):
                ucuncu_dort_ozellik_title[4] = "İşletim Sistemi"
            elif(ucuncu_dort_ozellik_title[4] == "Ekran Kartı Modeli"):
                ucuncu_dort_ozellik_title[4] = "Ekran Kartı"

            print(ucuncu_dort_ozellik_title[4]+"  ===  "+ucuncu_dort_ozellik[4])
            liste.append([ucuncu_dort_ozellik_title[4],ucuncu_dort_ozellik[4]])
            
            dort_dort_title = (detayss[6].get_text().split("\n"))
            dort_dort = (detayss[7].get_text().split("\n"))


            if(dort_dort_title[1] == "SSD Kapasitesi"):
                dort_dort_title[1] = "Disk Boyutu"
            elif(dort_dort_title[1] == "Model Kodu"):
                dort_dort_title[1] = "Model No"
            elif(dort_dort_title[1] == "İşlemci"):
                dort_dort_title[1] = "İşlemci Tipi"
            elif(dort_dort_title[1] == "İşletim Sistemi Yazılımı"):
                dort_dort_title[1] = "İşletim Sistemi"
            elif(dort_dort_title[1] == "Ekran Kartı Modeli"):
                dort_dort_title[1] = "Ekran Kartı"

            print(dort_dort_title[1]+"  ===  "+dort_dort[1])
            liste.append([dort_dort_title[1],dort_dort[1]])

            if(dort_dort_title[2] == "SSD Kapasitesi"):
                dort_dort_title[2] = "Disk Boyutu"
            elif(dort_dort_title[2] == "Model Kodu"):
                dort_dort_title[2] = "Model No"
            elif(dort_dort_title[2] == "İşlemci"):
                dort_dort_title[2] = "İşlemci Tipi"
            elif(dort_dort_title[2] == "İşletim Sistemi Yazılımı"):
                dort_dort_title[2] = "İşletim Sistemi"
            elif(dort_dort_title[2] == "Ekran Kartı Modeli"):
                dort_dort_title[2] = "Ekran Kartı"
            
            print(dort_dort_title[2]+"  ===  "+dort_dort[2])
            liste.append([dort_dort_title[2],dort_dort[2]])

            if(dort_dort_title[3] == "SSD Kapasitesi"):
                dort_dort_title[3] = "Disk Boyutu"
            elif(dort_dort_title[3] == "Model Kodu"):
                dort_dort_title[3] = "Model No"
            elif(dort_dort_title[3] == "İşlemci"):
                dort_dort_title[3] = "İşlemci Tipi"
            elif(dort_dort_title[3] == "İşletim Sistemi Yazılımı"):
                dort_dort_title[3] = "İşletim Sistemi"
            elif(dort_dort_title[3] == "Ekran Kartı Modeli"):
                dort_dort_title[3] = "Ekran Kartı"

            print(dort_dort_title[3]+"  ===  "+dort_dort[3])
            liste.append([dort_dort_title[3],dort_dort[3]])

            if(dort_dort_title[4] == "SSD Kapasitesi"):
                dort_dort_title[4] = "Disk Boyutu"
            elif(dort_dort_title[4] == "Model Kodu"):
                dort_dort_title[4] = "Model No"
            elif(dort_dort_title[4] == "İşlemci"):
                dort_dort_title[4] = "İşlemci Tipi"
            elif(dort_dort_title[4] == "İşletim Sistemi Yazılımı"):
                dort_dort_title[4] = "İşletim Sistemi"
            elif(dort_dort_title[4] == "Ekran Kartı Modeli"):
                dort_dort_title[4] = "Ekran Kartı"

            print(dort_dort_title[4]+"  ===  "+dort_dort[4])
            liste.append([dort_dort_title[4],dort_dort[4]])

            try:

                bes_dort_title = (detayss[8].get_text().split("\n"))
                bes_dort = (detayss[9].get_text().split("\n"))


                if(bes_dort_title[1] == "SSD Kapasitesi"):
                    bes_dort_title[1] = "Disk Boyutu"
                elif(bes_dort_title[1] == "Model Kodu"):
                    bes_dort_title[1] = "Model No"
                elif(bes_dort_title[1] == "İşlemci"):
                    bes_dort_title[1] = "İşlemci Tipi"
                elif(bes_dort_title[1] == "İşletim Sistemi Yazılımı"):
                    bes_dort_title[1] = "İşletim Sistemi"
                elif(bes_dort_title[1] == "Ekran Kartı Modeli"):
                    bes_dort_title[1] = "Ekran Kartı"

                print(bes_dort_title[1]+"  ===  "+bes_dort[1])
                liste.append([bes_dort_title[1],bes_dort[1]])

                if(bes_dort_title[2] == "SSD Kapasitesi"):
                    bes_dort_title[2] = "Disk Boyutu"
                elif(bes_dort_title[2] == "Model Kodu"):
                    bes_dort_title[2] = "Model No"
                elif(bes_dort_title[2] == "İşlemci"):
                    bes_dort_title[2] = "İşlemci Tipi"
                elif(bes_dort_title[2] == "İşletim Sistemi Yazılımı"):
                    bes_dort_title[2] = "İşletim Sistemi"
                elif(bes_dort_title[2] == "Ekran Kartı Modeli"):
                    bes_dort_title[2] = "Ekran Kartı"
                
                print(bes_dort_title[2]+"  ===  "+bes_dort[2])
                liste.append([bes_dort_title[2],bes_dort[2]])

                if(bes_dort_title[3] == "SSD Kapasitesi"):
                    bes_dort_title[3] = "Disk Boyutu"
                elif(bes_dort_title[3] == "Model Kodu"):
                    bes_dort_title[3] = "Model No"
                elif(bes_dort_title[3] == "İşlemci"):
                    bes_dort_title[3] = "İşlemci Tipi"
                elif(bes_dort_title[3] == "İşletim Sistemi Yazılımı"):
                    bes_dort_title[3] = "İşletim Sistemi"
                elif(bes_dort_title[3] == "Ekran Kartı Modeli"):
                    bes_dort_title[3] = "Ekran Kartı"

                print(bes_dort_title[3]+"  ===  "+bes_dort[3])
                liste.append([bes_dort_title[3],bes_dort[3]])

                if(bes_dort_title[4] == "SSD Kapasitesi"):
                    bes_dort_title[4] = "Disk Boyutu"
                elif(bes_dort_title[4] == "Model Kodu"):
                    bes_dort_title[4] = "Model No"
                elif(bes_dort_title[4] == "İşlemci"):
                    bes_dort_title[4] = "İşlemci Tipi"
                elif(bes_dort_title[4] == "İşletim Sistemi Yazılımı"):
                    bes_dort_title[4] = "İşletim Sistemi"
                elif(bes_dort_title[4] == "Ekran Kartı Modeli"):
                    bes_dort_title[4] = "Ekran Kartı"

                print(bes_dort_title[4]+"  ===  "+bes_dort[4])
                liste.append([bes_dort_title[4],bes_dort[4]])
            
            except :
            
                exit


        print("------------------")
        para_indeksi = para_indeksi + 1
print(liste)
print(len(liste))