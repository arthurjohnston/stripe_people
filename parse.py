from bs4 import BeautifulSoup as bs
from nltk.corpus import stopwords
import re
def print_words_with_at_least_n(occurrences):
	stop = stopwords.words('english')
	soup=bs(open("people_2015_01_31.html"))
	raw_bios=soup.findAll('span',{"class":"inner"})
	bios=[b.text.replace('\n','').replace(',','').lower() for b in raw_bios]
	text=''.join(bios)
	tokens=re.split('\W+',text)
	wordCount=dict()
	total=0
	for t in (t for t in tokens if t not in stop):
		if t not in wordCount:
			wordCount[t]=1
		else:
			wordCount[t]+=1
		total+=1
	results=sorted(wordCount.items(),key=lambda x:x[1],reverse=True)
	results=[r for r in results if r[1]>=occurrences]
	print ("There were a total of "+str(total)+" 'real' words")
	for word,count in results:
		print(word+"-"+str(count)+" times")
if __name__ == "__main__":
	print_words_with_at_least_n(9)