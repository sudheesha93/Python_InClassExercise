import requests
from bs4 import BeautifulSoup
import os

data=requests.get("https://en.wikipedia.org/wiki/UMKC")
parse=BeautifulSoup(data.content,"html.parser")

output1=parse.find_all('div')
for div in output1:
    R1=div.find('h1')
    if R1!=None:
        print("dhebd")
        print(R1.string)
print(parse.find('body').text)






