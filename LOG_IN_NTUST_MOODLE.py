from selenium import webdriver
import bs4
browser = webdriver.Chrome()
url = 'https://moodle.ntust.edu.tw/'
browser.get(url)
accout = browser.find_element_by_xpath("//input[@id='login_username']")
accout.send_keys('STUDENT ID')
password = browser.find_element_by_xpath("//input[@id='login_password']")
password.send_keys('PAWWSORD')
button = browser.find_element_by_xpath('/html[1]/body[1]/div[3]/section[2]/div[1]/section[1]/aside[1]/div[2]/div[2]/form[1]/div[4]/input[1]')
button.click()
