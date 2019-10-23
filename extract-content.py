import sys
import re
import os
import subprocess
from extractcontent3 import ExtractContent

#Argumen check
if len(sys.argv) !=3 :
    print ("\n\nPenggunaan\n\textract-content.py [pathSource] [pathOutput]\n")
    sys.exit(1)

#Argumen store
source = sys.argv[1]
output = sys.argv[2]

#get list file from source
data = str(subprocess.getoutput("ls "+source+" -v"))
list_file = data.split("\n") 

# Clean string function
def clean_str(text) :
    text = re.sub("&.*?;", "", text)
    text = re.sub(">", "", text)    
    text = re.sub("[\]\|\[\@\#\$\%\*\&\\\(\)\"]", "", text)
    text = re.sub(" - ", " ", text)
    text = re.sub("\xc2\xa0/", " ", text)
    text = re.sub("\.+", ".", text)
    text = re.sub("\n+", " ", text)
    text = re.sub("\s+\.", ". ", text)
    text = re.sub("\.\s+", ". ", text)
    text = re.sub("\s+", " ", text)
    text = re.sub("^$", "", text)
    text = re.sub("\.\s$", "", text)
    text = re.sub("^\s+","" ,text)
    return text


#Extract Content Html
extractor = ExtractContent()
for x in list_file :
    html = open(source+"/"+x).read()        #read file
    date_time = re.findall(r'<meta name="content_PublishedDate" content=\"(.*?)\" />', html)#get date and time
    link = re.findall(r'<meta property="og:url" content=\"(.*?)\" />', html)                #get link
    extractor.analyse(html)                 #analise html
    content, title = extractor.as_text()    #html to text
    content = clean_str(content)            #clean conten
    title = clean_str(title)                #clean title

    #date time
    try : 
        date, time = date_time[0].split(" ")
    except :
        continue
    
    #make directory to each date
    dir_name = output+"/"+date
    filename = x.split(".")[0]
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print("Directory " , dir_name,  " Created ")
    
    #make and write file
    file = open(dir_name+"/"+filename+".dat", "w+")
    file.write("<url>"+link[0]+"</url>\n")
    file.write("<date>"+date+"</date>\n")
    file.write("<time>"+time+"</time>\n")
    file.write("<title>"+title+"</title>\n")
    file.write("<content>"+content+"</content>")
    file.close
