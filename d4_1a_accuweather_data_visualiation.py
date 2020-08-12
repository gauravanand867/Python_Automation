from selenium import webdriver
import pandas as pd


month='august' #input('Enter Month in small letters: ')
year='2020'	#input('Enter Year')
city='patna' #dalsinghsarai'	#input('Enter City')

browser=webdriver.Chrome('//home//gaurav//Documents//chromedriver')
browser.get('https://www.accuweather.com/en/in/'+city+'/187244/'+month+'-weather/187244?year='+year+'&view=list')

highT_list=browser.find_elements_by_class_name('high')
high_temp=[]
for i in highT_list:
	t=i.get_attribute('textContent')
	high_temp.append(int(t[:2]))



lowT_list=browser.find_elements_by_class_name('low')
low_temp=[]
for i in lowT_list:
	t=i.get_attribute('textContent')
	low_temp.append(int(t[3:5]))

data3=browser.find_elements_by_xpath("//div[@class='info precip']/p[2]") #Precipitation
precip=[]
for i in data3:
    t=i.get_attribute('textContent')
    precip.append(float(t[:2]))

date=[]
for i in range(len(precip)):
	date.append(i+1)

d={'Date':date,'High_Temperature':high_temp,'Low_Temperature':low_temp,'Precipitation':precip}
df=pd.DataFrame(d)
df.to_csv("//home//gaurav//Documents//weatherdata"+month+city+".csv")
print("Done",df)