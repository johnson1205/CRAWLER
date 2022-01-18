# ch8_15.py
import requests, bs4, os

url_ppt = 'https://www.ptt.cc'
beauty = '/bbs/beauty/index.html'

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }

ptthtml = requests.get(url_ppt+beauty, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')

destDir = 'image_file'
if os.path.exists(destDir) == False:
    os.mkdir(destDir)       

pttdiv = objSoup.find_all('div', 'r-ent')
for pttdivs in pttdiv:
    try:
        href = pttdivs.find('a')['href']                                 # 文章超連結

        print('目前連線網址 : ', url_ppt+href)
        beauty_html = requests.get(url_ppt+href, cookies={'over18':'1'})    # 進入超連結
        beauty_soup = bs4.BeautifulSoup(beauty_html.text, 'lxml')   

        dataTag = beauty_soup.select('#main-container')
        urlurl = dataTag[0].find_all('a')
        for i in range(len(urlurl)):
            url = urlurl[i].get('href')
            pic = requests.get(url, headers=headers)
            pictFile = open(os.path.join(destDir, os.path.basename(url)), 'wb')
            for diskStorage in pic.iter_content(10240):
                pictFile.write(diskStorage)
            pictFile.close()
    except:
        continue