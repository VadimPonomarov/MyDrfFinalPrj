import dataclasses
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from random import choice

from scraper import settings

import requests
from attr import field
from fp.fp import FreeProxy
from playwright.sync_api import Browser, BrowserType, Page, sync_playwright


@dataclasses.dataclass
class MyPlaywrightBrowser:
    browser_type: BrowserType = sync_playwright().start().chromium
    context: Browser = field(init=False)
    headless: bool = True
    page: Page = field(init=False)
    time: time = field(init=False)
    proxy: bool = False
    proxy_elite: bool = False
    proxy_https: bool = False
    base_dir: str = f"{Path(__file__).resolve().parent.parent}"

    def __post_init__(self):
        self.time = time.time()
        with ThreadPoolExecutor(max_workers=4) as executor:
            proxy = executor.submit(self.__get_proxy, )
            headers = executor.submit(self.__get_headers, )
            args = executor.submit(self.__get_launch_args, )
        # if proxy.done() and headers.done() and args.done():
        self.context = self.browser_type.launch(
            headless=self.headless,
            args=args.result(),
            proxy={'server': proxy.result()}
        )
        self.page = self.context.new_page(
            extra_http_headers=headers.result()
        )
        print(f"Browser is init in (minutes): {(time.time() - self.time) / 60}")

    def __call__(self, *args, **kwargs):
        return self.context

    def get_new_page(self):
        return self.context.new_page()

    def __get_launch_args(self):
        return [f"{i}" for i in settings.BROWSER_LAUNCH_ARGS]

    def __get_headers(self):
        response = requests.get(
            url=f"{os.getenv('SCRAPE_OPS_URL')}",
            params={'api_key': os.getenv('SCRAPE_OPS_KEY')}
        )
        resp = choice(response.json()['result'])
        return resp

    def set_proxy(self, *args, **kwargs):
        for i, v in kwargs.items():
            self[i] = v
        self.proxy = self.__get_proxy()

    def __get_proxy(self):
        if self.proxy:
            loop = 1
            while loop:
                try:
                    _proxy = FreeProxy(elite=self.proxy_elite, rand=True, https=self.proxy_https).get()
                    with open(os.path.join(self.base_dir, 'storage/proxy.json'), 'w+') as file:
                        json.dump(_proxy, file)
                    return _proxy
                except Exception as err:
                    print(f'!!! Failed {loop} attempt to get free proxy')
                    loop += 1
        else:
            with open(os.path.join(self.base_dir, 'storage/proxy.json'), 'r+') as file:
                try:
                    _proxy = json.load(file) or ''
                    return _proxy
                except Exception as err:
                    print(err)

    def close_browser(self):
        self.context.close()
        print('!!! Browser is closed')


if __name__ == "__main__":
    browser = MyPlaywrightBrowser()
    with browser.page as page:
        try:
            page.goto('https://myip.com.ua/', wait_until='load')
        except:
            pass
