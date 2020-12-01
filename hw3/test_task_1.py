from hw3.task_1 import cache


from unittest.mock import Mock




def test_my():
    mock = Mock()

    @cache(number_of_iterations=2)
    def func():
        mock()

    value_1 = func()
    assert mock.call_count == 1







# @cache(number_of_iterations=2)
# def funk(number):
#     return number + 1
#
#
# def test_cache_number_of_iterations():
#     arg_of_func = 2
#     results = []
#     result_call_of_func_1 = funk(arg_of_func)
#     results.append(result_call_of_func_1)
#
#     result_call_of_func_2 = funk(arg_of_func)
#     results.append(result_call_of_func_2)
#
#     result_call_of_func_3 = funk(arg_of_func)
#     results.append(result_call_of_func_3)
#
#     assert results == [3, 3, None]
#
#
# def test_cache_id_of_numbers():
#     arg_of_func = 2
#     result_call_of_func_1 = funk(arg_of_func)
#     result_call_of_func_2 = funk(arg_of_func)
#
#     assert result_call_of_func_1 is result_call_of_func_2
