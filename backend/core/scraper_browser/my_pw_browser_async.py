import asyncio
import dataclasses
import json
import os
from dataclasses import field
import time
from random import choice

import requests
from fp.fp import FreeProxy
from playwright.async_api import async_playwright, Browser, Page


@dataclasses.dataclass
class MyPwBrowserAsync:
    context: Browser = field(init=False)
    headless: bool = True
    page: Page = field(init=False)
    time: time = field(init=False)
    proxy: bool = False
    headers: bool = False
    proxy_elite: bool = False
    proxy_https: bool = True
    base_dir: str = f"{os.path.join(os.getcwd())}"

    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            await self.close_browser()
        except Exception as err:
            pass

    async def post_init(self):  # Делаем метод асинхронным
        self.time = time.time()
        p = await async_playwright().start()  # Используем start и stop вместо контекстного менеджера
        self.context = await p.chromium.launch(  # Используем await для асинхронных методов
            headless=self.headless,
            # args=self.__get_launch_args(),
            # proxy=self.__get_proxy()
        )

        self.page = await self.context.new_page(  # Используем await для асинхронных методов
            extra_http_headers=self.__get_headers()
        )

        print(f"Browser is init in (minutes): {(time.time() - self.time) / 60}")
        # await p.stop()  # Останавливаем экземпляр Playwright

    @property  # Делаем метод свойством
    def __call__(self, *args, **kwargs):  # Делаем метод асинхронным
        return self.context

    async def get_new_page(self):  # Делаем метод асинхронным
        return await self.context.new_page()  # Используем await для асинхронных методов

    def __get_launch_args(self):
        return [
            "--ignore-certificate-errors=True",
            "--ignoreHTTPSErrors=True",
            "--disable-blink-features=AutomationControlled",
            # "--headless=True"
        ]

    def __get_headers(self):
        loop = 1
        while loop:
            if self.headers:
                try:
                    _headers = requests.get(
                        url=os.environ.get("SCRAPE_OPS_URL"),
                        params={
                            'api_key': os.environ.get("SCRAPE_OPS_KEY"),
                            'num_results': '2'}
                    )
                    resp = choice(_headers.json()['result'])

                    with open(os.path.join(self.base_dir, 'storage', 'headers.json'), 'w+') as file:
                        file.write(json.dumps(_headers.json()['result']))
                    return resp
                except Exception as err:
                    print(f'!!! Failed {loop} attempt to get fake headers')
                    loop += 1
            else:
                with open(os.path.join(self.base_dir, 'storage', 'headers.json'), 'r+') as file:
                    try:
                        _headers = json.load(file)
                        resp = choice(json.loads(_headers)) or ''
                        loop = 0
                        return resp
                    except Exception as err:
                        self.headers = True
                        print(f'!!! Failed {loop} attempt to get fake headers')
                        loop += 1

    def __get_proxy(self):
        loop = 1
        if self.proxy:
            while loop:
                try:
                    _proxy = FreeProxy(elite=self.proxy_elite, rand=True, https=self.proxy_https).get()
                    with open(os.path.join(self.base_dir, 'storage', 'proxy.json'), 'w+') as file:
                        json.dump(_proxy, file)
                    loop = 0
                    return {"server": _proxy}  # Добавляем порт к ключу прокси
                except Exception as err:
                    print(f'!!! Failed {loop} attempt to get free proxy')
                    loop += 1
        else:
            with open(os.path.join(self.base_dir, 'storage', 'proxy.json'), 'r+') as file:
                try:
                    _proxy = json.load(file)
                    loop = 0
                    return {"server": _proxy}  # Добавляем порт к ключу прокси
                except Exception as err:
                    self.proxy = True
                    print(f'!!! Failed {loop} attempt to get free proxy')
                    loop += 1

    async def close_browser(self):  # Делаем метод асинхронным
        await self.context.close()  # Используем await для асинхронных методов
        print('!!! Browser is closed')


async def main():
    try:
        import dotenv
        dotenv.load_dotenv()

        browser = MyPwBrowserAsync(headless=False, proxy=False, proxy_https=True)
        async with browser:
            await browser.post_init()
            await browser.page.goto('https://myip.com.ua/', wait_until='load',
                                    timeout=50000)  # Используем await для асинхронных методов
            await asyncio.sleep(10)
    except Exception as err:
        pass


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    import asyncio
    import nest_asyncio

    try:
        nest_asyncio.apply()
        asyncio.run(main())
    except Exception as err:
        pass
