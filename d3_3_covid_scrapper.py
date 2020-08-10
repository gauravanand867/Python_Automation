from selenium import webdriver
import pandas as pd
import time
import os


browser_path='//home//gaurav//Documents//chromedriver'
browser=webdriver.Chrome(browser_path)
browser.get('https://www.worldometers.info/coronavirus/')
time.sleep(10)


colunm_list=['Rank','Country', 'Total Cases', 'New Cases', 'Deaths', 'New Deaths','Recovered', 'Active Cases', 'Critical']
df=pd.DataFrame(columns=colunm_list)

for i in browser.find_elements_by_xpath('//table[@id="main_table_countries_today"]/tbody/tr'):
	each_row=i.find_elements_by_tag_name('td')
	row=[]
	for k in each_row:
		row.append(k.text)
	d={}
	for j in range(len(df.columns)):
		d[df.columns[j]]=row[j]
	df=df.append(d,ignore_index=True)



df=df.iloc[1:]
print(df)

save_path='//home//gaurav//Documents'

file_path=os.path.join(save_path,'covid.csv')

df.to_csv(file_path,index=False)

print("The data has been feteched from server and saved at"+save_path)
browser.quit()