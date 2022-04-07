from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys # 키 함수들을 사용하기위해 불러옴
chrome_path = 'C:\히히호호\chromedriver.exe' #크롬드라이버 경로
url = 'https://www.naver.com/'   #들어가고싶은 url
browser = webdriver.Chrome(chrome_path)
browser.get(url)
time.sleep(3)


# browser.find_element_by_xpath('//*[@id="account"]/a').click() # 로그인까지 눌러주는 기능

# browser.find_element_by_css_selector('#query').send_keys('안녕')
# browser.find_element_by_css_selector('#query').send_keys(Keys.ENTER)

# 위에 방법을 간단하게 
sendbox = browser.find_element_by_css_selector('#query')
sendbox.send_keys('안녕')
sendbox.send_keys(Keys.ENTER)


#find element_by_id() => id속성을 사용하여 접근
#               _name() => name 속성을 사용하여 접근
#               _xpath() => xpath 속성을 사용하여 접근
#               _link_text() => 앵커태그(a태그)에 사용되는 텍스트로 접근
#               _partial_link_text() => 앵커태그(a태그)에 사용되는 일부 텍스트로 접근
#               _tag_name() => 태그를 사용해서 접근
#               _class_name() => 클래스를 사용해서 접근
#               _css_selsctor() => css 선택자를 사용하여 접근
#  위의 내용을 작성 하고 뒤에   .click() => 클릭해라   /   .send_keys('') => 원하는 키(글) 입력 
# send_keys() 안에 넣을수 있는 함수 : Keys.ENTER => 엔터 / Keys.RETURN => 엔터 / Keys.SPACE => 스페이스 / Keys.ARROW_up => 방향키 위쪽 / Keys.ARROW_DOWN => 방향키 아랫쪽
# Keys.ARROW_LEFT => 방향키 왼쪽 / Keys.ARROW_RIGHT => 방향키 오른쪽 / Keys.BACK_SPACE => 지우기 / Keys.DELETE =>지우기(딜리트) / Keys.CONTROL => Ctrl 버튼
# Keys.ALT => alt 키 / Keys.SHIFT => shift 키 / Keys.TAB => tab 키 / Keys.PAGE_UP(DOWN) => 스크롤 업(다운) / Keys.F1~9 => f1~f9 까지 
# 맨 처음 탭으로 이동 => browser.switch_to.window(window_handles[0]) 
# 새롭게 열린 창, 팝업, 탭 으로 전환 => browser.switch_to.window(window_handles[-1]) -> 여기서 쓰는 browser창은 위에서 수업할때 임의로 지정해준 이름 다른이름 지정해주면 다른 것도 사용 가능
# 스크린 샷(현재 켜있는 창) => browser.get_screenshot_as_file('capture.png') -> 괄호안에는 저장할 이름 작성 또는 폴더 작성 
# 브라우저 창 닫기 => browser.close()


####내 아이디와 비번으로 수업 페이지 로그인한거####
# from selenium import webdriver
# import time
# chrome_path = 'C:\히히호호\chromedriver.exe' #크롬드라이버 경로
# url = 'https://codepen.io/login'   #들어가고싶은 url
# browser = webdriver.Chrome(chrome_path)
# browser.get(url)

# browser.find_element_by_css_selector('#login-with-github > span').click()

# id = ''
# browser.find_element_by_css_selector('#login_field').send_keys(id)

# ps = "'
# browser.find_element_by_css_selector('#password').send_keys(ps)
# browser.find_element_by_css_selector('#login > div.auth-form-body.mt-3 > form > div > input.btn.btn-primary.btn-block.js-sign-in-button').click()
