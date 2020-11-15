import hashlib
import random
import struct
import time
from multiprocessing.dummy import Pool


def slow_calculate(value: int) -> int:
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def sum_of_numbers(n: int) -> int:
    with Pool(500) as pool:
        answer = sum(pool.map(slow_calculate, list(range(n))))
        return answer
