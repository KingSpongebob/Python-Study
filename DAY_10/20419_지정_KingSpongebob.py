from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')

try:
	driver.get('http://www.11st.co.kr')
	print(driver.title)

	elem = driver.find_element_by_id('AKCKwd')
	elem.clear()
	elem.send_keys("라즈베리파이")
	elem.send_keys(Keys.RETURN)

	hot = driver.find_element_by_class_name('hotClick_wrap')
	hot_list = hot.find_elements_by_tag_name('li')

	ex = Workbook()
	es = ex.active	

	for hot in hot_list:
		hot_title = hot.find_element_by_class_name('info_tit')
		print(hot_title.text)
		print('-'*40)	
		es.append([hot_title.text])	 
	ex.save('20419_지정.xlsx')

except Exception as e:
	print(e)
finally:
	driver.close()

