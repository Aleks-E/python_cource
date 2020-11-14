import time
import struct
import random
import hashlib


from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import timeit
import pytest



pool = ThreadPool(4)

def a(x):
    return x*x

results = pool.map(a, [1, 2, 3])

print(results)




# -------------------

# def slow_calculate(value):
#     """Some weird voodoo magic calculations"""
#     time.sleep(random.randint(1, 3))
#     data = hashlib.md5(str(value).encode()).digest()
#     return sum(struct.unpack('<' + 'B' * len(data), data))
#
#
#
# def f(n):
#     if __name__ == '__main__':
#         with Pool(1) as p:
#             # start = timeit.default_timer()
#             answer = sum(p.map(slow_calculate, list(range(n))))
#             # end = timeit.default_timer()
#             # time_1 = end - start
#             # print(time_1)
#             return answer
#
#
# if __name__ == '__main__':
#     start = timeit.default_timer()
#     actual_result = f(1)
#     end = timeit.default_timer()
#     time_1 = end - start
#     print(actual_result)
#     print(time_1)















# -------------------


# if __name__ == '__main__':
#     main()





# print('actual_result', actual_result)
# print('time_1', time_1)



    # @pytest.mark.parametrize(
    #     ("value", "expected_result"),
    #     [
    #         (11, 2785),
    #     ],
    # )

    # def test_f(value: int, expected_result: int):
    # if __name__ == '__main__':
    #     start = timeit.default_timer()

# actual_result = f(1)



        # end = timeit.default_timer()
        # time_1 = end - start

# expected_result = 11
# assert actual_result == expected_result





# expected_result = 22

# assert actual_result == expected_result



# if __name__ == '__main__':
#     import timeit
#     import pytest
#
#     # pytest.main()
#
# if __name__ == '__main__':
#     @pytest.mark.parametrize(
#         ("value", "expected_result"),
#         [
#             (11, 2785),
#         ],
#     )
#     def test_f(value: int, expected_result: int):
#     # if __name__ == '__main__':
#         start = timeit.default_timer()
#         actual_result = f(value)
#         end = timeit.default_timer()
#         time_1 = end - start
#         assert actual_result == expected_result




























