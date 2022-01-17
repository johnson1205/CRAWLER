import bs4, requests, os

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url = 'https://nhentai.net/g/YOUR_URL/'
html = requests.get(url, headers=headers)
destDir = 'image_file'
if os.path.exists(destDir) == False:
    os.mkdir(destDir)
objSoup = bs4.BeautifulSoup(html.text, 'lxml')
imgTag = objSoup.select('img')
if len(imgTag) > 0:
    for i in range(len(imgTag)):
        imgUrl = imgTag[i].get('src')
        finUrl = imgUrl
        try:
            picture = requests.get(finUrl, headers=headers)
            pictFile = open(os.path.join(destDir, os.path.basename(imgUrl)), 'wb')
            for diskStorage in picture.iter_content(10240):
                pictFile.write(diskStorage)
            pictFile.close()
        except Exception as err:
            continue