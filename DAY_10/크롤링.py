from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')

try:
	driver.get('http://www.naver.com')
	print(driver.title)

	search = driver.find_element_by_id('query')
	search.clear()
	search.clear()
	search.send_keys('대덕소프트웨어마이스터고')
	search.send_keys('Keys.RETURN')

	elem = driver.find_element_by_class_name('news')
	new_list = elem.find_elements_by_tag_name('li')
	
	ex = Workbook()
	es = ex.active

	for news in news_list:
		news_title = new.find_element_by_class_name('_sp_each_title')
		print(new_title.text)
		es.append([news_title.text]) #append / 대괄호 사용
		
	ex.save('result.xlsx')
except Exception as e:
	print(e)

finally:
	driver.close()