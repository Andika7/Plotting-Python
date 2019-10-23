import sys
import os

#Argumen check
if len(sys.argv) !=3 :
    print ("\n\nPenggunaan\n\tdownload.py [FileUrl] [Pathoutput]\n")
    sys.exit(1)

#Read file with name from argumen
print("Loading ..")
print("Membaca File ",sys.argv[1],"..")

#Open Url file
filename = sys.argv[1]
file = open(filename, "r")

#read file
print ("Berhasil Membaca File "+filename+" ..")
print("Loading ..")
contents = file.read()
urls = contents.split("\n")

#download file
i = 1
for url in urls:
    if not url :
        continue
    # print("wget -O crawl/file-"+str(i)+".html "+url)
    os.system("wget -O "+sys.argv[2]+"/kompas-"+str(i)+".html "+url)
    i+=1