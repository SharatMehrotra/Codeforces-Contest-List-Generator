import requests
from bs4 import BeautifulSoup
import csv
'''
Generates a text file consisting of all the active, upcoming and past contests.
If a contest shows Virtual Participation, it's a past contest
If it shows Enter, it's a an active contest
If it's written in a single line, it's an upcoming contest.
'''
URL = "https://codeforces.com/contests"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
file1 = open("DOC_HTML.html","w")
file1.write(soup.prettify())
quotes=[]  # a list to store quotes

table = soup.find('div', attrs = {'id':'pageContent'})
count=0
file3=open("SCHEDULE","w")
for row in table.findAll('tr'):
    if(row.has_attr('data-contestid')):
        count+=1
        file3.write("\n")
        file3.write(row.td.text.strip())
        file3.write("\n")
        file3.write("###################")
