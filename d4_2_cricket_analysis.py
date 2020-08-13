from bs4 import BeautifulSoup
from urllib.request import urlopen

page=urlopen('https://www.espncricinfo.com/rankings/content/page/211271.html')
pg=BeautifulSoup(page,'html.parser')

body=pg.find('div',{'class':'ciPhotoContainer'})
head=pg.findAll('h3')

heading_l=[]
for i in head:
	t=i.text
	heading_l.append(t)
#print(heading_l)

import pandas as pd
colunm_l=['pos','team','matches','points','rating']
df=pd.DataFrame(columns=colunm_l)
#print(df)

tr_list=pg.findAll('tr')

n=0
for i in tr_list:
	row=[]
	td_list=i.findAll('td')
	for j in td_list:
		t=j.text
		row.append(t)
		dics={}
	try:
		for k in range(len(df.columns)):
			dics[df.columns[k]]=row[k]
		df=df.append(dics,ignore_index=True)
	except:
		df=pd.DataFrame(columns=colunm_l)
		file_name=heading_l[n]
		n+=1
	df.to_csv('//home//gaurav//Documents//cricket'+file_name+'.csv', index=False)
print("Done")