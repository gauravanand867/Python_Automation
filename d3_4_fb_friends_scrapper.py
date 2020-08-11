user_id=input('Enter Mobile no or Email:')
password=input('Enter password:')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

browser=webdriver.Chrome('//home//gaurav//Documents//chromedriver')
browser.get('https://www.facebook.com/')
id=browser.find_element_by_id('email')
id.send_keys(user_id)
passd=browser.find_element_by_id('pass')
passd.send_keys(password)
submit=browser.find_element_by_id('u_0_b')
submit.click()
time.sleep(120)

fbutton=browser.find_element_by_xpath('//a[@class="_2s25 _606w"]')
time.sleep(5)
fbutton.click()

time.sleep(2)

fcbutton=browser.find_element_by_xpath('//ul[@class="_6_7 clearfix"]/li[3]/a')
fcbutton.click()

while True:
	browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
	browser.execute_script('window.scrollTo(0,0);')
	try:
		check_exit=browser.find_element_by_xpath("//*[contains(text(), 'More about you')]")
		break
	except:
		continue

ps=browser.page_source
parced_data=BeautifulSoup(ps,'html.parser')

flist=parced_data.find('div',{'class':'_3i9'})

friend=[]

for i in flist.findAll('a'):
	friend.append(i.text)

friend_name=[]
for j in friend:
	if(j=='FriendFriends'):
		continue
	if('friends' in j):
		continue
	if(j==''):
		continue
	else:
		friend_name.append(j)

print(friend_name)