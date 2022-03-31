from selenium import webdriver
chrome_path = 'C:\히히호호\chromedriver.exe'
url = 'https://www.naver.com/'
browser = webdriver.Chrome(chrome_path)
browser.get(url)