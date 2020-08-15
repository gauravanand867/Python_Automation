from selenium import webdriver
import smtplib
import schedule

browser=webdriver.Chrome('//home//gaurav//Documents//chromedriver')

def getprice():
	browser.get('https://www.amazon.in/Test-Exclusive-750/dp/B078BN55WZ/ref=sr_1_1?crid=3OEL6DKYVV850&dchild=1&keywords=one%2Bpluse8%2Bpro%2Bmobile&qid=1597315955&sprefix=one%2Caps%2C290&sr=8-1&th=1')
	pe=browser.find_element_by_id('priceblock_ourprice')
	pr=pe.get_attribute('textContent')
	pr=pr[2:]
	pl=pr.split(',')
	price_a=''
	for i in pl:
		price_a+=i
	print('Price on amazon is '+price_a)
	price_a=float(price_a)
	return price_a

def mail():
	s=smtplib.SMTP('smtp.gmail.com','587')			# (Host and port number)
	s.starttls()									#For secure connection
	m='gayravanand867@gmail.com'
	p='Poggy@7785'
	s.login(m,p)
	mt='gauravanand867@gmail.com'
	message='Hurry Up Price is Good to buy'
	s.sendmail(m,mt,message)
	s.quit()
def task():
	desired=19000
	a=getprice()

	if(desired<=a):
		mail()
		print('Mailed')
	else:
		print("Don't Buy now")

schedule.every(10).seconds.do(task)
print("Checking Service On..........")
while True:
	schedule.run_pending()


