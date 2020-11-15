# def dec_2(n):
#     def dec_1(func):
#         count = n
#         def inner():
#             nonlocal count
#             a = 0
#             while True:
#                 while count:
#                     if count == n:
#                         print('ok_1')
#                         func()
#                         count -= 1
#                         return n
#                     else:
#                         func()
#                         count -= 1
#                         return n
#                 count = n
#
#         return inner
#     return dec_1
#
#
# @dec_2(3)
# def func():
#     return int(input('? '))
#
#
# func()      # ok_1
#             # ?
# func()      # ?
# func()      # ?

# ---------------------------------

def dec_2(n):
    def dec_1(func):
        count = n
        def inner():
            nonlocal count
            # a = 0
            while True:
                # print('in while_1')
                a = func()
                # print(a)
                while count:
                    # print('in while_2')
                    if count == n:
                        # print('ok_1')
                        # func()
                        count -= 1
                        # print(a)
                        return a
                    else:
                        # func()
                        count -= 1
                        return a
                count = n

        return inner
    return dec_1


@dec_2(3)
def func():
    return int(input('? '))


print(func())
print(func())
print(func())
print(func())
# print(func())
# print(func())
# print(func())
# print(func())
# print(func())
# print(func())


# func()      # ok_1
#             # ?
# func()      # ?
# func()      # ?
#
# func()      # ok_1
#             # ?
# func()      # ?
# func()      # ?



















