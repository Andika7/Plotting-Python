import sys
import matplotlib.pyplot as plt

#Argumen check
if len(sys.argv) !=2 :
    print ("\n\nPenggunaan\n\tdownload.py [frequen.txt]\n")
    sys.exit(1)

#load argumen
source = sys.argv[1]

#open file frequency
file = open(source).read()
file = file.split("\n")
word =[]
value =[] 
for x in range(0, 10):
    wd, fq = file[x].split("\t")
    word.append(wd)
    value.append(int(fq))

plt.pie(value,
autopct='%1.1f%%', shadow=True, startangle=100)

plt.title("Pie Chart Top 10 Kata Agustus 2019")
plt.legend(word,loc='best')
plt.axis('equal')
plt.show()