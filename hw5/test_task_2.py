import functools

from hw5.task_2 import print_result


def test_store_original_func_info():
    def custom_sum(*args):
        """This function can sum any objects which have __add___"""
        return functools.reduce(lambda x, y: x + y, args)

    name_of_function_without_decorator = custom_sum.__name__
    doc_of_function_without_decorator = custom_sum.__doc__

    custom_sum = print_result(custom_sum)

    name_of_function_with_decorator = custom_sum.__name__
    doc_of_function_with_decorator = custom_sum.__doc__

    assert name_of_function_without_decorator == name_of_function_with_decorator
    assert doc_of_function_without_decorator == doc_of_function_with_decorator


def test_store_original_func():
    @print_result
    def custom_sum(*args):
        """This function can sum any objects which have __add___"""
        return functools.reduce(lambda x, y: x + y, args)

    assert custom_sum.__original_func.__eq__(custom_sum)


def test_print_out_without_decorator(capsys):
    def custom_sum(*args):
        """This function can sum any objects which have __add___"""
        return functools.reduce(lambda x, y: x + y, args)

    custom_sum(1)
    out, err = capsys.readouterr()
    assert out == ""


def test_print_out_with_decorator(capsys):
    @print_result
    def custom_sum(*args):
        """This function can sum any objects which have __add___"""
        return functools.reduce(lambda x, y: x + y, args)

    custom_sum(1)
    out, err = capsys.readouterr()
    assert out == "1\n"
