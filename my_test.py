import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor


def my_test(a: int, b: int):
    time.sleep(1)
    res = a + b
    return res


if __name__ == '__main__':
    t = time.time()
    with ThreadPoolExecutor() as executor:
        for res in executor.map(my_test, [1, 2, 3], [1, 2, 3]):
            print(res)
        # print(futures)
    print(f'Time elapsed: {time.time() - t}')
