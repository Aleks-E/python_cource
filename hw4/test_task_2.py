import urllib.request

from unittest.mock import MagicMock

from hw4.task_2 import count_dots_on_i


import sys


# def test_count_dots_on_i(monkeypatch):
#     url = "https://example.com/"
#     monkeypatch.setattr(urllib.request, "urlopen", MagicMock(
#         return_value=[b"<html>", b"<head>", b"<title>iii</title>", b"</head>", b"<body>", b"ii", b"</body>",
#                       b"</html>"]))
#     assert count_dots_on_i(url) == 7





def test_count_dots_on_i(monkeypatch):
    url = "https://example.com/"

    this_module = sys.modules[__name__ = task_2]

    monkeypatch.setattr(this_module, "html_content", MagicMock(
        return_value=[b"<html>", b"<head>", b"<title>iii</title>", b"</head>", b"<body>", b"ii", b"</body>",
                      b"</html>"]))




    assert count_dots_on_i(url) == 7








