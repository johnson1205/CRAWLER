#Due to there is a small number of students in NTUST plan to study abroad,
#it is very difficult for me to find concerning information.
#Thus, I write this shit to help me searching these.
import bs4, requests, os
import concurrent.futures
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
articleIncludeLists = []
url = 'https://www.ptt.cc/bbs/studyabroad/index.html'
html = requests.get(url, headers=headers)
objSoup = bs4.BeautifulSoup(html.text, 'lxml')
pre_page = objSoup.findAll('a','btn wide')
#print('https://www.ptt.cc/'+pre_page[1].get('href'))
while(pre_page[1].get('href')!='/bbs/studyabroad/index1.html'):
    print('https://www.ptt.cc'+pre_page[1].get('href'))
    html = requests.get('https://www.ptt.cc'+pre_page[1].get('href'))
    objSoup = bs4.BeautifulSoup(html.text, 'lxml')
    pre_page = objSoup.findAll('a','btn wide')
    articles = objSoup.findAll('div', 'r-ent')
    for i in articles:
        articlehtml=requests.get('https://www.ptt.cc'+i.find('a')['href'], headers=headers)
        #print('https://www.ptt.cc'+i.find('a')['href'])
        articleObjSoup= bs4.BeautifulSoup(articlehtml.text, 'lxml')
        if("NTUST" in articleObjSoup.find('div', 'bbs-screen bbs-content').text):
            print('https://www.ptt.cc'+i.find('a')['href'])
            articleIncludeLists.append('https://www.ptt.cc'+i.find('a')['href'])
f = open('NTUSTLISTS.txt', 'w')
for i in articleIncludeLists:
    f.write(i)
f.close()
