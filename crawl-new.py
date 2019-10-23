import os
import sys
import requests
from parsel import Selector
import re

#Argumen check
if len(sys.argv) !=4 :
    print ("\n\nPenggunaan\n\tcrawl.py [file-url.txt] [n-days] [dd-mm-yyyy]\n\n")
    sys.exit(1)

#Make file with name from argumen
print("Loading ..")
print("Membuat File ",sys.argv[1],"..")
filename = sys.argv[1]
file = open(filename, "w+")
print ("Berhasil Membuat File", sys.argv[1], "..")
print("Loading ..")

#Var declare
count =0
urls ={}

#get date
dd, mm, yyyy =sys.argv[3].split("-")
tanggal = int(dd)
bulan = int(mm)
tahun = int(yyyy)
iterasi = int(sys.argv[2])
hal = 5

n = 0
while(n <= iterasi ) :
    halaman = 1
    while (halaman <= hal) :
        url=""
        print ("mendapatkan link tgl: "+str(tanggal)+"/"+str(bulan)+"/"+str(tahun)+" page :"+str(halaman))
        if (tanggal < 10) :
            if (bulan <10) : 
                url = "https://indeks.kompas.com/?site=all&date="+str(tahun)+"-0"+str(bulan)+"-0"+str(tanggal)+"&page="+str(halaman)
            else : 
                url = "https://indeks.kompas.com/?site=all&date="+str(tahun)+"-"+str(bulan)+"-0"+str(tanggal)+"&page="+str(halaman)
        else : 
            if (bulan <10) : 
                url = "https://indeks.kompas.com/?site=all&date="+str(tahun)+"-0"+str(bulan)+"-"+str(tanggal)+"&page="+str(halaman)
            else : 
                url = "https://indeks.kompas.com/?site=all&date="+str(tahun)+"-"+str(bulan)+"-"+str(tanggal)+"&page="+str(halaman)
        
        #get response from url
        response = requests.get(url)

        #"response.text" contain all web page content
        selector = Selector(response.text)

        #Extracting href attribute from anchor tag <a href="*">
        href_links = selector.xpath('//a/@href').getall()

        for link in href_links: #loop each link from href_links
            if link in urls : #if url exist in dictionary continue loop 
                continue

            if (re.search("\/read\/", link) ) : #if url contains words "berita"
                urls[link] = 1
                count+=1
        
        halaman+=1
        
    iterasi-=1
    tanggal-=1
    
    if(tanggal < 1) :
        bulan-=1
        tanggal = 29
    

    if(bulan < 1) :
        bulan = 12
        tahun-=1
    
print("Tanggal "+str(tanggal)+" bulan "+str(bulan)+" => Total link(s) : "+str(count))
print("Menulis link kedalam file....")

# Write url to file
for x in urls:
    file.write(x+"\n")
file.close

print("berhasil mendapatkan : "+str(count)+" url :)\n")




