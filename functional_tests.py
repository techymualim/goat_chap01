from selenium import webdriver

browser =webdriver.Chrome(executable_path='C:/bin/chromedriver.exe')
browser.get('http://localhost:8000')

assert 'install' in browser.title