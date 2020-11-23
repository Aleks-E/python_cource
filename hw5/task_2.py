"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func

print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий

До применения вашего декоратор будет вызываться AttributeError при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция

Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""
from functools import wraps
from typing import Callable, Union


def print_result(func: Callable) -> Callable:
    def store_original_func_info(wrapper: Callable) -> Callable:
        wrapper.__original_func = func
        return wrapper

    @store_original_func_info
    @wraps(func)
    def wrapper(
        *args: Union[int, float, complex], **kwargs: any
    ) -> Union[int, float, complex]:
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper
