from threading import activeCount
from selenium import webdriver
import bs4
browser = webdriver.Chrome()
url = 'https://courseselection.ntust.edu.tw/'
browser.get(url)
accout = browser.find_element_by_xpath("//body/div[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[1]/input[1]")
accout.send_keys('STUDENT ID')
password = browser.find_element_by_xpath("//body/div[1]/form[1]/div[2]/div[2]/div[2]/div[2]/div[1]/input[1]")
password.send_keys('PASSWORD')
button = browser.find_element_by_xpath("//button[@id='btnLogIn']")
button.click()
# ----------------NOT COMPLETED----------------