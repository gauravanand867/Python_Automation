from selenium import webdriver

user=input('Enter user name:')


browser_path='//home//gaurav//Documents//chromedriver'
browser=webdriver.Chrome(browser_path)

url='https://www.instagram.com/'
url=url+user

browser.get(url)

try:
	image=browser.find_element_by_xpath('//img[@class="_6q-tv"]')
except:
	image=browser.find_element_by_xpath('//img[@class="be6sR"]')

img_link=image.get_attribute('src')
print(img_link)

save_path='//home//gaurav//Documents//'+user+'.jpg'

import urllib.request

urllib.request.urlretrieve(url,save_path)
print("Profile image Download successfully to:"+save_path)
