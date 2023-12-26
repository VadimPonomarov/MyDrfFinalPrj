import multiprocessing
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor()

import settings

from scraper.items import CarBrandItem


def f1(_time):
    time.sleep(_time)
    return {'f1': threading.get_ident()}


def f2(_time):
    time.sleep(_time)
    return {'f2': os.getpid()}


def main():
    p1 = pool.submit(f1, 1)
    p2 = pool.submit(f1, 1)
    p3 = pool.submit(f1, 1)

    print(p1.result(), p2.result(), p3.result())


if __name__ == '__main__':
    t = time.time()
    main()
    print(time.time() - t)
