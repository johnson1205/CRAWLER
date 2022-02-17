from threading import activeCount
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4
from pynput.keyboard import Key, Controller
browser = webdriver.Chrome()
keyboard = Controller()
url = 'https://courseselection.ntust.edu.tw/'
browser.get(url)
accout = browser.find_element_by_xpath("//body/div[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[1]/input[1]")
accout.send_keys('STUDENTID')
password = browser.find_element_by_xpath("//body/div[1]/form[1]/div[2]/div[2]/div[2]/div[2]/div[1]/input[1]")
password.send_keys('PASSWORD')
button = browser.find_element_by_xpath("//button[@id='btnLogIn']")
button.click()
time.sleep(10)
url = 'https://courseselection.ntust.edu.tw/AddAndSub/B01/B01'
browser.get(url)
while(1):
    time.sleep(1)
    try:
        course = browser.find_element_by_xpath("//body/div[3]/div[1]/div[1]/form[1]/div[1]/div[1]/div[6]/div[4]/span[1]")
        course.click()
        time.sleep(3)
        keyboard.press(Key.enter)
    except:
        print("boom")
        course = browser.find_element_by_xpath("//body/div[3]/div[1]/div[1]/form[1]/div[1]/div[1]/div[6]/div[4]/span[1]")
        course.click()
        time.sleep(3)
        keyboard.press(Key.enter)
        
