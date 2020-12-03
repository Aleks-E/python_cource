from unittest.mock import Mock

from hw3.task_1 import cache


def test_the_returned_value_from_the_function_and_from_the_cache_are_equal():
    @cache(number_of_iterations=1)
    def func(arg):
        return arg

    value_from_the_function = func(1)
    value_from_the_cache = func(2)
    assert value_from_the_function == value_from_the_cache


def test_the_function_returns_new_value_after_required_number_of_function_calls():
    @cache(number_of_iterations=1)
    def func(arg):
        return arg

    value_from_the_first_call = func(1)
    assert value_from_the_first_call == 1

    old_value_with_new_arg = func(2)
    assert old_value_with_new_arg == value_from_the_first_call

    new_value_from_the_function = func(2)
    assert new_value_from_the_function == 2


def test_the_function_returns_a_value_from_the_cache_required_number_of_times():
    mock = Mock()

    @cache(number_of_iterations=1)
    def func():
        mock()

    call_of_function = func()
    assert mock.call_count == 1
    return_cached_value = func()
    assert mock.call_count == 1
    new_call_of_function = func()
    assert mock.call_count == 2
