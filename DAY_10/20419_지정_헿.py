from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')

try:
	driver.get('https://www.wemakeprice.com')
	print(driver.title)

	wmp = driver.find_element_by_id('wrap_main_best_area')
	wmp_list = wmp.find_elements_by_tag_name('li')

	ex = Workbook()
	es = ex.active	

	for wmp in wmp_list:
		wmp_title = wmp.find_element_by_class_name('tit_desc')
		print(wmp_title.text)
		print('-'*40)	
		es.append([wmp_title.text])	 
	ex.save('20419_지정_헿.xlsx')

except Exception as e:
	print(e)
finally:
	driver.close()

