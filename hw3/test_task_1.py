from unittest.mock import Mock

from hw3.task_1 import cache


def test_function_returns_value_from_cache_on_second_call():
    mock = Mock()

    @cache(number_of_iterations=1)
    def func():
        mock()

    call_of_function = func()
    assert mock.call_count == 1
    cached_value = func()
    assert mock.call_count == 1


def test_function_returns_a_value_from_the_cache_only_required_number_of_times():
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


def test_function_returns_a_value_from_the_cache_with_positional_arguments():
    @cache(number_of_iterations=1)
    def func(*args):
        return args

    call_of_function = func(1, 2)
    cached_value = func(1, 2)
    assert call_of_function == cached_value


def test_function_returns_a_value_from_the_cache_with_keyword_arguments():
    @cache(number_of_iterations=1)
    def func(**kwargs):
        return kwargs

    call_of_function = func(a=1, b=2)
    cached_value = func(a=1, b=2)
    assert call_of_function == cached_value


def test_function_has_its_own_cache_for_each_result():
    mock = Mock()

    @cache(number_of_iterations=1)
    def func(*args):
        mock()

    call_of_function = func(1)
    assert mock.call_count == 1
    call_of_function_with_different_arguments = func(2)
    assert mock.call_count == 2
    cached_result = func(1)
    assert mock.call_count == 2
    cached_result_with_different_arguments = func(2)
    assert mock.call_count == 2
    assert call_of_function == cached_result
    assert (
        call_of_function_with_different_arguments
        == cached_result_with_different_arguments
    )
