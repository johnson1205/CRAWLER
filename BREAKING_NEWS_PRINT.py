import requests, bs4, os

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
f = open("output.txt", "a", encoding='utf-8')

url = 'https://tw.appledaily.com/realtime/recommend/'
html = requests.get(url, headers=headers)
soupobj = bs4.BeautifulSoup(html.text, 'lxml')
list = soupobj.find('div', 'article-list-container')
lists = list.find_all('div', 'storycard-headline text_greyish-brown-two')
for i in lists:
    name = i.span.text
    f.write(name)
    f.write('\n')
f.write('\n')

url = 'https://udn.com/news/breaknews/1'
html = requests.get(url, headers=headers)
soupobj = bs4.BeautifulSoup(html.text, 'lxml')
list = soupobj.find('div', 'context-box__content story-list__holder story-list__holder--full')
lists = list.find_all('div', 'story-list__news')
for i in lists:
    name = i.find('div', 'story-list__text').a.text
    f.write(name)
    f.write('\n')
f.write('\n')
url = 'https://money.udn.com/rank/newest/1001/0/1?from=edn_navibar'
html = requests.get(url, headers=headers)
soupobj = bs4.BeautifulSoup(html.text, 'lxml')
list = soupobj.find('ul', 'story-list-holder')
lists = list.find_all('h3', 'story__headline')
for i in lists:
    name = i.text.strip()
    f.write(name)
    f.write('\n')
f.write('\n')
url = 'https://www.chinatimes.com/realtimenews/?chdtv'
html = requests.get(url, headers=headers)
soupobj = bs4.BeautifulSoup(html.text, 'lxml')
list = soupobj.find('ul', 'vertical-list list-style-none')
lists = list.find_all('li')
for i in lists:
    name = i.find('h3', 'title').a.text
    f.write(name)
    f.write('\n')
f.write('\n')

url = 'https://ctee.com.tw/livenews'
html = requests.get(url, headers=headers)
soupobj = bs4.BeautifulSoup(html.text, 'lxml')
list = soupobj.find('div', 'listing listing-text listing-text-2 clearfix')
lists = list.find_all('p', 'now-title')
for i in lists:
    name = i.find_all('a')
    classify = name[0].text.strip()
    title = name[1].text.strip()
    ctee_context = classify+title
    f.write(ctee_context)
    f.write('\n')