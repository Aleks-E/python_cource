import sqlite3

from hw8.task_2 import TableData

import pytest


@pytest.fixture()
def database_wrapper():
    return TableData(database_name="hw8/example.sqlite", table_name="presidents")


def test_len_of_database(database_wrapper):
    assert len(database_wrapper) == 3


def test_retrieve_single_data_row_with_name_from_name_column(database_wrapper):
    assert database_wrapper["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_if_president_with_the_same_name_exists_in_table(database_wrapper):
    assert "Yeltsin" in database_wrapper


def test_iteration(database_wrapper):
    it = iter(database_wrapper)
    president = next(it)["name"]
    assert president in database_wrapper
    president = next(it)["name"]
    assert president in database_wrapper


def test_calls_reflects_the_recent_data():
    with sqlite3.connect("hw8/example.sqlite") as conn:
        presidents = TableData(
            database_name="hw8/example.sqlite", table_name="presidents"
        )
        assert len(presidents) == 3
        cursor = conn.cursor()
        cursor.execute("INSERT INTO presidents VALUES ('1', '1', '1')")
        conn.commit()
        assert len(presidents) == 4
        cursor.execute("DELETE FROM presidents WHERE name = '1'")
        conn.commit()


def test_if_president_with_the_same_name_not_exists_in_table(database_wrapper):
    assert "1" not in database_wrapper


def test_retrieve_single_data_row_with_not_existent_name_from_name_column(
    database_wrapper,
):
    assert database_wrapper["1"] is None
