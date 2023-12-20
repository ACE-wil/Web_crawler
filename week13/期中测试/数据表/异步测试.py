import asyncio
from requests_html import HTMLSession

async def main():
    url = 'https://jobs.51job.com/beijing-cyq/151690627.html?s=sou_sou_soulb&t=0_0&req=d3310cd415ac789e4f3a5075ca48ef9a'

    session = HTMLSession()
    response = session.get(url)

    # 等待5秒钟
    await asyncio.sleep(5)

    # 在等待时间后再继续处理
    # 注意：在实际使用中，请根据网站的加载时间和异步处理的需要进行调整
    # 这里只是为了演示在请求后等待一段时间
    print(response.content)
    msg = response.html.find('div.job_msg')
    print(msg)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
