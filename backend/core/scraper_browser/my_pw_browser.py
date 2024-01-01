import dataclasses
import json
import os
from concurrent.futures import ThreadPoolExecutor
from dataclasses import field
import time
from random import choice

import requests
from fp.fp import FreeProxy
from playwright.sync_api import sync_playwright, Browser, Page


@dataclasses.dataclass
class MyPlaywrightBrowser:
    context: Browser = field(init=False)
    headless: bool = True
    page: Page = field(init=False)
    time: time = field(init=False)
    proxy: bool = False
    headers: bool = False
    proxy_elite: bool = False
    proxy_https: bool = True
    base_dir: str = f"{os.path.join(os.getcwd())}"

    def __post_init__(self):
        self.time = time.time()
        p = sync_playwright().start().chromium
        with ThreadPoolExecutor() as executor:
            self.context = p.launch(
                headless=self.headless,
                args=executor.submit(self.__get_launch_args, ).result(),
                proxy=executor.submit(self.__get_proxy, ).result()
            )
        self.page = self.context.new_page(
            extra_http_headers=self.__get_headers()
        )
        print(f"Browser is init in (minutes): {(time.time() - self.time) / 60}")

    def get_new_page(self):
        return self.context.new_page()

    def __get_launch_args(self):
        return []

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
                        _headers = json.load(file) or []
                        resp = choice(json.loads(_headers)) or ''
                        return resp
                    except Exception as err:
                        self.headers = True
                        print(f'!!! Failed {loop} attempt to get fake headers')
                        loop += 1

    def __get_proxy(self):
        if self.proxy:
            loop = 1
            while loop:
                try:
                    _proxy = FreeProxy(elite=self.proxy_elite, rand=True, https=self.proxy_https).get()
                    with open(os.path.join(self.base_dir, 'storage', 'proxy.json'), 'w+') as file:
                        json.dump(_proxy, file)
                    return {"server": _proxy}
                except Exception as err:
                    print(f'!!! Failed {loop} attempt to get free proxy')
                    loop += 1
        else:
            with open(os.path.join(self.base_dir, 'storage', 'proxy.json'), 'r+') as file:
                try:
                    _proxy = json.load(file) or ''
                    return {"server": _proxy}
                except Exception as err:
                    print(err)

    def close_browser(self):
        self.context.close()
        print('!!! Browser is closed')


if __name__ == "__main__":
    if not os.environ.get('DOCKER'):
        import dotenv

        dotenv.load_dotenv()

    browser = MyPlaywrightBrowser(headless=False, headers=True, proxy=False, proxy_https=True)

    try:
        with browser.page as page:
            page.goto('https://myip.com.ua/', wait_until='load')
            time.sleep(10)
    except Exception as err:
        print(err)
