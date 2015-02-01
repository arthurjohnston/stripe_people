from bs4 import BeautifulSoup as bs
from nltk.corpus import stopwords
import re

stop = stopwords.words('english')
soup=bs(open("people.html"))
raw_bios=soup.findAll('span',{"class":"inner"})
bios=[b.text.replace('\n','').replace(',','').lower() for b in raw_bios]
text=''.join(bios)
tokens=re.split('\W+',text)
wordCount=dict()
for t in (t for t in tokens if t not in stop):
	if t not in wordCount:
		wordCount[t]=1
	else:
		wordCount[t]+=1
sorted(wordCount.items(),key=lambda x:x[1],reverse=True)