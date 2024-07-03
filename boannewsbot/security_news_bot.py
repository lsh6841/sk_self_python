import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import urllib3
from urllib.parse import urlparse, parse_qs

#warring 제거 (InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#임시 제거


intents = discord.Intents.default()
intents.message_content = True



class MyClient(discord.Client):
    async def on_ready(self):
        pass

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.lower() == '!news':
            news_articles = scrape_boannews()
            if not news_articles:
                await message.channel.send('Failed to retrieve news articles.')
                return

            # 뉴스 기사를 임베드 메시지로 게시합니다.
            for article in news_articles:
                embed = discord.Embed(title=article[0], url='', description=article[1])
                await message.channel.send(embed=embed)

def scrape_boannews():
    boannews1 = "https://boannews.com/media/view.asp?idx="
    boannews2 = "https://boannews.com/media/t_list.asp"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    #option verify = False 안넣으면 sslerror뜸
    data1 = requests.get(boannews2,headers=headers,verify=False)

    soup = BeautifulSoup(data1.text, 'html.parser')
        #가장 위에있는 뉴스 번호
    news = soup.find_all('div',"news_list")
    list_n = []
    for i in news:
        list_n.append(i.find('a').get('href'))

        # 'idx' 값 가져오기 = 가장 최신 뉴스 번호
    idx_value = []
        #나중에 5를 변수로 넣고 원하는 수 뽑기
    for i in range(5):
        parsed_url = urlparse(list_n[i])
        query_params = parse_qs(parsed_url.query)
        idx_value_single = int(query_params.get('idx', [None])[0])
        idx_value.append(idx_value_single)

    print(idx_value)

    news_list = []
    for i in range(5):
        ne = requests.get(f"{boannews1}{idx_value[i]}&page=1&kind=1",headers=headers,verify=False)
        ssoup = BeautifulSoup(ne.text, 'html.parser')
        name = ssoup.find('div',id="news_title02").find('h1').text
        print(name)
        n = ssoup.find('div',id="news_content").text
        print(n)
        news_list.append((name,n))
    
    return news_list


TOKEN = ''
 
bot = MyClient(intents=intents)
bot.run(TOKEN)


