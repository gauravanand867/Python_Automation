user_id=input('Enter Mobile no or Email:')
password=input('Enter password:')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser=webdriver.Chrome('//home//gaurav//Documents//chromedriver')
browser.get('https://www.facebook.com/')
id=browser.find_element_by_id('email')
id.send_keys(user_id)
passd=browser.find_element_by_id('pass')
passd.send_keys(password)
submit=browser.find_element_by_id('u_0_b')
submit.click()
# browser.quit()
time.sleep(5)
add='//*[@id="home_birthdays"]/div/div/div/div/a/div/div/span/span[2]'
content=browser.find_element_by_xpath(add).get_attribute('textContent')
fcontent=content.split(' ')
todayno=fcontent[0]
todayno=int(todayno)+1

browser.get('https://www.facebook.com/events/birthdays/')
time.sleep(5)

bday_list=browser.find_elements_by_xpath("//*[@class='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")
c=1
message='Happy Birthday to U'
for element in bday_list:
	each_element=str(element.get_attribute('id'))
	xpath='//*[@id="' +each_element+ '"]'
	place=browser.find_element_by_xpath(xpath)	#To fetch the box where to enter text
	place.send_keys(message)
	place.send_keys(Keys.RETURN)
	c+=1
	if(c>todayno):
		break


