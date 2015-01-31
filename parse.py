from bs4 import BeautifulSoup as bs
from nltk.corpus import stopwords
import re

stop = stopwords.words('english')
soup=bs(open("people.html"))
people=soup.findAll('span',{"class":"inner"})
rawtext=rawtext=''.join([p.text.replace('\n','').replace(',','').lower() for p in people])
tokens=re.split('\W+',rawtext)
wordCount=dict()
for t in (t for t in tokens if t not in stop):
	if t not in wordCount:
		wordCount[t]=1
	else:
		wordCount[t]+=1
sorted(wordCount.items(),key=lambda x:x[1])