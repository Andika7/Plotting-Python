import sys
import subprocess as sp
import re
import matplotlib.pyplot as plt
import numpy as np

#Argumen check
if len(sys.argv) !=3 :
    print ("\n\nPenggunaan\n\tdownload.py [pathFreq] [days]\n")
    sys.exit(1)

#store argumen
source = sys.argv[1]
days= int(sys.argv[2])

#list file in source
data = str(sp.getoutput("ls "+source+" -v")).split("\n")

if (days > len(data)-1) :
    print("not enough data")
    sys.exit(1)

#read top 10
file = open(source+"/"+data[len(data)-1]).read().split("\n")
top_10=[]
for x in range(0,10) :
    top_10.append(file[x].split("\t")[0])

#insert top 10 to dictionary
dict_days={}
count = 0
del data[len(data)-1]
for word in top_10:
    days_freq=[]
    i=1
    for list in data:
        if (i>days) : break

        isi = open(source+"/"+list).read()
        wd = re.findall(r''+word+'\t(.*?)\n', isi)
        days_freq.append(int(wd[0]))
        i+=1
    dict_days[word]=[]
    dict_days[word].extend(days_freq)
    days_freq.clear()


#days arragement
y_post = np.arange(days)

for x in dict_days : 
    plt.plot(y_post, dict_days[x], label=x)

plt.title("Grafik Top 10 Kata Perhari pada "+str(days)+" Hari Pertama Agustus 2019")    
plt.xlabel('Days')
plt.ylabel('Frequency')
plt.legend(loc=1)
plt.show()
