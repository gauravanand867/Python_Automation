from selenium import webdriver

browser=webdriver.Chrome('//home//gaurav//Documents//chromedriver')

browser.get('https://www.amazon.in/Test-Exclusive-750/dp/B078BN55WZ/ref=sr_1_1?crid=3OEL6DKYVV850&dchild=1&keywords=one%2Bpluse8%2Bpro%2Bmobile&qid=1597315955&sprefix=one%2Caps%2C290&sr=8-1&th=1')
pe=browser.find_element_by_id('priceblock_ourprice')
pr=pe.get_attribute('textContent')
pr=pr[2:]
pl=pr.split(',')
price_a=''
for i in pl:
	price_a+=i
print('Price on amazon is '+price_a)

browser.get('https://www.flipkart.com/oneplus-8-pro-onyx-black-256-gb/p/itm4dcbd336cdd4f?pid=MOBFU897DEZ4SZ9X&lid=LSTMOBFU897DEZ4SZ9X3XJTWH&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=b0ba3921-ac6d-468a-8282-a92473384b97.MOBFU897DEZ4SZ9X.SEARCH&ppt=sp&ppn=sp&ssid=scq9tf7ek00000001597226823165&qH=5894ab4766000b8e')
fpe=browser.find_element_by_xpath('//div[@class="_1vC4OE _3qQ9m1"]')
fpr=fpe.get_attribute('textContent')

fpr=fpr[1:]
fpl=fpr.split(',')
price_f=''
for v in fpl:
	price_f+=v

print('Price on Flipkart is '+price_f)

price_f=float(price_f)
price_a=float(price_a)

if(price_a<price_f):
	print('Aamazon has best price, buy from here ')
elif(price_a>price_f):
	print('Flipkart has best price, Buy from here.')
else:
	print('Both has equal price, Buy from anywhere')
