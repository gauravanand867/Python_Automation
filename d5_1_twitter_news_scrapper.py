from selenium import webdriver
import time
from urllib.request import urlopen
import pandas as pd

browser=webdriver.Chrome('//home//gaurav//Documents//Coding//Alien Brains//Python_Automation//chromedriver')

browser.get('https://twitter.com/explore/tabs/trending')
time.sleep(5)
hashtag=browser9.find_elements_by_tag_name('span')
hashtag_text=[]
for i in hashtag:
	t=i.get_attribute('textContent')
	if (t.startswith('#')):
		if t not in hashtag_text:
			hashtag_text.append(t)
hashtag_url=[]
for text in hashtag_text:
	url='https://twitter.com/search?q=%'+text+'&src=promoted_trend_click'
	hashtag_url.append(url)

dics={'Hashtag':hashtag_text,'URL':hashtag_url}
df=pd.DataFrame(dics)
df.to_csv('//home//gaurav//Documents//Coding//Alien Brains//Python_Automation//twitter.csv',index=False)
print('Done')