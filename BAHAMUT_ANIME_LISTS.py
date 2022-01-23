#SORT ANIME BY NAME

import bs4, requests
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
bahaurl = 'https://ani.gamer.com.tw/animeList.php?page='
information = '&c=All&sort=2'
page = 1
f = open('anime_lists.txt', 'w', encoding='utf-8')
arr = []
while True:
    response = requests.get(bahaurl+str(page)+information, headers=headers)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    list = soup.find('div', 'theme-list-block')
    lists = list.find_all('a')
    if(len(lists)!=0):
        for i in lists:
            name = i.find('p', 'theme-name').text
            arr.append(name)
    else:
        break
    page+=1
arr.sort();
for i in range(len(arr)):
    f.write(arr[i])
    f.write('\n')