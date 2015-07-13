from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
page_body = browser.find_element_by_tag_name('body')

assert 'It worked!' in page_body.text
