from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

search = input('상품들을 출력한 검색어를 입력하세요 :')
driver = webdriver.Chrome('chromedriver')

try:
	driver.get('https://www.wemakeprice.com')
	print(driver.title)

	elem = driver.find_element_by_id('searchKeyword')
	elem.clear()
	elem.send_keys(search)
	elem.send_keys(Keys.RETURN)

	wmp = driver.find_element_by_class_name('section_list')
	wmp_list = wmp.find_elements_by_tag_name('li')

	ex = Workbook()
	es = ex.active	

	for wmp in wmp_list:
		wmp_title = wmp.find_element_by_class_name('tit_desc')
		print(wmp_title.text)
		print('-'*40)	
		es.append([wmp_title.text])	 
	ex.save('20419_지정_KingSpongebob.xlsx')

except Exception as e:
	print(e)
finally:
	driver.close()