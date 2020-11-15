# def decorator(argument):
#     def dec_1(func):
#         def inner():
#             print(argument)
#             print('12')
#             func()
#
#         return inner
#     return dec_1
#
#
# @decorator(34)
# def func():
#     print('ok')
#
# func()      # 34
#             # 12
#             # ok

# ---------------------------


def dec_2(n):
    def dec_1(func):
        count = n
        def inner():
            nonlocal count
            a = 0
            while True:
                while count:
                    if count == n:
                        # print('ok_1')
                        # func()
                        a = func()
                        print(a)

                        count -= 1
                        return
                        # return n
                    else:
                        # func()
                        print(a)
                        count -= 1
                        return
                        # return n
                count = n

        return inner
    return dec_1


@dec_2(3)
def func():
    return int(input('? '))


func()      # ok_1
            # ok

func()      # ok
func()      # ok

func()      # ok_1
            # ok

func()      # ok
func()      # ok





