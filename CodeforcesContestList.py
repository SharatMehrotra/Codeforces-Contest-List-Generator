import requests
from bs4 import BeautifulSoup
import csv

URL = "https://codeforces.com/contests"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
file1 = open("DOC_HTML.html","w")
file1.write(soup.prettify())
quotes=[]  # a list to store quotes

table = soup.find('div', attrs = {'id':'pageContent'})
count=0
file3=open("SCHEDULE","w")
name=[]
date=[]
time=[]
for row in table.findAll('tr'):
    if(row.has_attr('data-contestid')):
        count+=1
        name.append(row.td.text)
        for row1 in row.findAll('td'):
            if(row1.find('span') and row1.span.has_attr('data-locale')):
                date.append(row1.span.text)
            elif(not(row1.find('span')) and not(row1.has_attr('span')) and (':' in row1.text) and row1.text!=row.td.text):    
                time.append(row1.text)
newname=[]
print(time)
for i in range(len(name)):
    name[i] = name[i].split()
    x=0
    st=""
    while(x<len(name[i]) and name[i][x]!='Enter'):
        st+=name[i][x]+" "
        x+=1
    newname.append(st)
for i in range(len(name)):
    s1="Contest Name: " + newname[i]+"\n"
    s2="Contest Date: " + date[i]+"\n"
    s3="Contest Run Time: "+time[i].strip()+"\n\n"
    file3.write(s1)
    file3.write(s2)
    file3.write(s3)
