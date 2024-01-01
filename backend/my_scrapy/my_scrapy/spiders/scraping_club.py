import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import numpy
import scrapy

from core.scraper_browser.my_playwright_browser import MyPlaywrightBrowser


# import logging
#
# logging.getLogger('scrapy').setLevel(logging.WARNING)


class ScrapingClubSpider(scrapy.Spider):
    name = "scraping_club"
    start_urls = ["https://auto.ria.com/uk/"]

    def __init__(self, targets: list = ('Легкові',)):
        super().__init__()
        self.start_time = time.time()
        '''headless=True, proxy=True, proxy_elite=True, proxy_https=True'''
        self.browser = MyPlaywrightBrowser()
        self.targets = list(targets)

    def parse(self, response):
        # loop = True
        browser = self.browser
        filters = ['Будь-який']
        page = browser.page
        try:
            page.goto(self.start_urls[0], wait_until='load', timeout=50000)
            time.sleep(2)
            categories = filter(lambda i: i in self.targets and i not in filters,
                                page.locator('#categories option').all_inner_texts())
            for i in categories:
                print(i)
                # with ThreadPoolExecutor() as executor:
                #     args = []
                #     for category in categories:
                #         category_item = dict(category=category)
                #         args.append(category_item)
                #
                #     for i, res in enumerate(
                #             executor.map(self.brand_by_category_parse, args, numpy.repeat(browser, len(args)))):
                #         yield from res
                #         filters.append(args[i]['category'])
                #
                #     loop = False
        except Exception as err:
            print('😈 My_err: ', err)
            # self.browser.close_browser()
            # self.browser = MyPlaywrightBrowser(proxy=True, proxy_https=True)

    # print(f"👀 Processed in (min): {(time.time() - self.start_time) / 60}")
    # browser.close_browser()

# def brand_by_category_parse(self, category_item, browser):
#     time_t = time.time()
#     filters = ['ТОП марки', 'Усі марки']
#     with browser.context.new_page() as page:
#         try:
#             page.goto(self.start_urls[0], wait_until='load', timeout=50000)
#             time.sleep(2)
#             page.get_by_label("Тип транспорту").select_option(category_item['category'])
#             time.sleep(.3)
#             brands = filter(lambda i: i not in filters, page.locator(
#                 '#brandTooltipBrandAutocomplete-brand > ul > li').all_inner_texts())
#             with ThreadPoolExecutor() as executor:
#                 args = []
#                 for brand in brands:
#                     category_brand_item = dict(**category_item, brand=brand)
#                     args.append(category_brand_item)
#                 for i, res in enumerate(
#                         executor.map(self.mark_by_category_brand_parse, args, numpy.repeat(browser, len(args)))):
#                     yield from res
#                     filters.append(args[i]['category'])
#                     print(f'Time elapsed (seconds): {round(time.time() - time_t)}')
#                     time_t = time.time()
#         except Exception as err:
#             raise Exception(err)
#
#
# def mark_by_category_brand_parse(self, category_brand_item, browser):
#     filters = ['ТОП моделі', 'Усі моделі']
#     with browser.context.new_page() as page:
#         try:
#             page.goto(self.start_urls[0], wait_until='load', timeout=50000)
#             time.sleep(2)
#             page.get_by_label("Тип транспорту").select_option(category_brand_item['category'])
#             page.locator("#brandTooltipBrandAutocomplete-brand label").click()
#             time.sleep(.3)
#             page.locator("#brandTooltipBrandAutocomplete-brand").get_by_text(
#                 category_brand_item['brand']).first.click()
#             time.sleep(.3)
#             models = filter(lambda i: i not in filters, page.locator(
#                 '#brandTooltipBrandAutocomplete-model > ul > li').all_inner_texts())
#
#             for model in models:
#                 category_brand_model_item = dict(**category_brand_item, model=model)
#                 yield category_brand_model_item
#                 filters.append(model)
#             print(category_brand_item)
#         except Exception as err:
#             raise Exception(err)
