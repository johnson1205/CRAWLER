from selenium import webdriver


search = input()
browser = webdriver.Chrome()
browser.get("https://www.google.com.tw/")
n = browser.find_element_by_xpath('//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]')
n.send_keys(search)
n.submit()