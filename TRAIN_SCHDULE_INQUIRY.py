from selenium import webdriver
import bs4
headless = webdriver.ChromeOptions()
headless.add_argument('headless')
browser = webdriver.Chrome(options=headless)
url = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobystation'
browser.get(url)
stations = browser.find_element_by_xpath("//button[contains(text(),'文字站點查詢')]")
stations.click()
banqiao = browser.find_element_by_xpath('//body/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[7]/button[1]')
banqiao.click()
searching = browser.find_element_by_xpath('/html[1]/body[1]/div[3]/div[3]/div[1]/form[1]/div[1]/div[4]/input[1]')
searching.click()
print(browser.current_url)
soup = bs4.BeautifulSoup(browser.page_source, 'lxml')
list = soup.find('div', 'main-tab')
lists = list.find_all('tr')
for i in lists:
    try:
        inf = i.find_all('td')
        time = inf[1].text
        timetext = '時間:' + time
        destination = inf[2].text
        destinationtext = '往:' + destination
        print('%10s' %destinationtext,'%s' %timetext)
    except:
        continue