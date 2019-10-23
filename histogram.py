import sys
import numpy as np
import matplotlib.pyplot as plt

#Argumen check
if len(sys.argv) !=2 :
    print ("\n\nPenggunaan\n\tdownload.py [frequen.txt]\n")
    sys.exit(1)

#store argumen
freq = sys.argv[1]

#open file
file = open(freq).read()
file = file.split("\n")
word =[]
value =[] 
for x in range(0, 10):
    wd, fq = file[x].split("\t")
    word.append(wd)
    value.append(int(fq))

# set ploting y
y_pos = np.arange(len(word))

#set color
# color_hist = ['purple', 'pink', 'red','orange', 'yellow', 'green', 'blue', "cyan", "brown", "black"]

#create bar
plt.bar(y_pos, value, color='orange')

for i, v in enumerate(value):
    plt.text(i-.15, 
              v/value[i]+800, 
              value[i], 
              fontsize=12, color='black', rotation=90)

# Add title and axis names
plt.title("Top 10 word Agustus 2019")
plt.xlabel('Words')
plt.ylabel('Frequency')

#insert word and rotate word
plt.xticks(y_pos, word, rotation=90)

#set margin bottom
plt.subplots_adjust(bottom= 0.2)

#show histogram
plt.show()





