#크롬 브라우저를 띄우기 위해 selenium 웹드라이버를 가져옴
from selenium import webdriver

#크롬 드라이버로 크롬 브라우저를 실행
driver = webdriver.Chrome('chromedriver')

try:
    driver.get('http://dsm2015.cafe24.com/#/')
    
    #DMS를 알 수 있도록 현재 타이틀 출력
    print(driver.title)

    #최근 뉴스 목록을 가진 div id 태그를 가져옴
    title_id = driver.find_element_by_id('food-wrapper')

    #위 div_id 안에 li태그로 구분되어 있는 정보를 가져와 리스트로 저장.
    news_list = title_id.find_elements_by_tag_name('p.food')

    #가져온 태그들에 대해 반목문을 수행하면서 각각의 문자열을  출력
    for news in dms_list:
        print()


except Exception as e:
    print(e)

finally:
    #브라우저 종료
    driver.quit()