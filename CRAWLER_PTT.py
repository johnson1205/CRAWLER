import requests
import bs4
import os

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
response = requests.get('YOUR_URL', headers=headers)
objSoup = bs4.BeautifulSoup(response.text, 'lxml')

destDir = 'image_file'
if os.path.exists(destDir) == False:
    os.mkdir(destDir)       

dataTag = objSoup.select('#main-container')
urlurl = dataTag[0].find_all('a')
for i in range(len(urlurl)):
    url = urlurl[i].get('href')
    pic = requests.get(url, headers=headers)
    pictFile = open(os.path.join(destDir, os.path.basename(url)), 'wb')
    for diskStorage in pic.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()