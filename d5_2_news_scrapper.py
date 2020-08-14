from bs4 import BeautifulSoup
import pandas as pd
import urllib.request

pages=int(input('No of pages you want: '))
titles=[]
links=[]
for i in range(pages):
	page=urllib.request.urlopen('https://news.ycombinator.com/news?p='+str(i+1))
	data=page.read()
	parsed_data=BeautifulSoup(data,'html.parser')
	b=parsed_data.find('table',{'class':'itemlist'}).find_all('a',{'class':'storylink'})

	for j in b:
		title=j.text
		titles.append(title)
		link=j.get('href')
		links.append(link)

disc={'Title':titles,'URL':links}

df=pd.DataFrame(disc)
df.to_csv('//home//gaurav//Documents//Coding//Alien Brains//Python_Automation//news.csv',index=False)
print(df,'\n Done')