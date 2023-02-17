import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup

HEADERS = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
    'Referer':'http://finance.sina.com.cn/',
}

async def crawl_xinlang_finance(session, url):
    print("发送请求:", url)
    html = requests.get(url=url, headers=HEADERS)#requests不支持非阻塞。即使使用异步编程，requests库还是按照同步那样访问完aurl，得到响应后才再访问burl
    # print(html.text)
    soup = BeautifulSoup(html.text,'lxml')
    print(soup)
    # async with session.get(url,verify_ssl=False) as response:
    #     print(response)
    #     content = await response.content()
    #     print(content)

def crawl_xinlang_finance():
    print("发送请求:", 'http://quote.eastmoney.com/center/gridlist.html?st=ChangePercent&sr=-1#sz_a_board')
    html = requests.get(url='http://quote.eastmoney.com/center/gridlist.html?st=ChangePercent&sr=-1#sz_a_board', headers=HEADERS)
    # print(html.text)
    soup = BeautifulSoup(html.text,'lxml')
    print(soup)

async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
        'http://finance.sina.com.cn/stock/sl/#area_1'
        ]
        tasks = [asyncio.create_task(crawl_xinlang_finance(session ,url))for url in url_list]
        await asyncio.wait(tasks)


if __name__ == '__main__':
    crawl_xinlang_finance()
    # asyncio.run( main() )
    
    
    