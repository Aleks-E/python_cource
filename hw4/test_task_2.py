import urllib.error
import urllib.request
from unittest.mock import MagicMock

from hw4.task_2 import count_dots_on_i

import pytest


def test_count_dots_on_i(monkeypatch):
    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        MagicMock(
            return_value=[
                b"<html>",
                b"<head>",
                b"<title>iii</title>",
                b"</head>",
                b"<body>",
                b"ii",
                b"</body>",
                b"</html>",
            ]
        ),
    )
    assert count_dots_on_i("1") == 7


def test_unreachable_source(monkeypatch):
    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        MagicMock(side_effect=urllib.error.HTTPError(404, "NF", "", "", "")),
    )

    with pytest.raises(ValueError, match="Unreachable https://1"):
        count_dots_on_i("https://1")
