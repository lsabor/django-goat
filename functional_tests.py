from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:9000/')

assert 'Babadook' in browser.title