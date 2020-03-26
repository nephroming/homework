import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

music_list = soup.select('#body-content > div.newest-list > div.music-list-wrap > table > tbody > tr')
rank = 0
for music_ranking in music_list:
    title = music_ranking.select_one('td.info > a.title.ellipsis')
    artist = music_ranking.select_one("td.info > a.artist.ellipsis")
    rank += 1
    print (rank, title.text.strip(), '/', artist.text)

    rank2 = list(range(1, 51))
    print(rank2)


    df = pd.DataFrame(
        {'순위' : [print(rank2)],
         '노래' : [print (title.strip())],
         '가수' : [print (artist)]
         }
    )